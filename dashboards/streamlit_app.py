import streamlit as st
import sqlite3
import pandas as pd
import os
import google.generativeai as genai
import re

st.set_page_config(page_title="AI Buddy Dashboard", layout="centered")
st.title("📊 AI Buddy Dashboard")

db_path = os.path.abspath("../backend/mood_logs.db")

try:
    conn = sqlite3.connect(db_path)
    df = pd.read_sql("SELECT * FROM mood_logs", conn)
    conn.close()

    if df.empty:
        st.warning("No logs yet.")
    else:
        st.dataframe(df)

        st.subheader("📈 Mood Trends (step 5 only)")
        mood_df = df[(df["step"] == 5) & (df["mood"].notnull())]

        users = mood_df["user_id"].unique()
        selected = st.selectbox("Select a user", users)

        user_df = mood_df[mood_df["user_id"] == selected].copy()
        user_df["timestamp"] = pd.to_datetime(user_df["timestamp"])
        user_df["date"] = user_df["timestamp"].dt.date

        trend = user_df.groupby("date")["mood"].first().reset_index()
        st.line_chart(trend.set_index("date"))

        st.subheader("📊 Mood Breakdown")
        st.bar_chart(mood_df["mood"].value_counts())

        st.subheader("🧠 Alert History")
        try:
            conn = sqlite3.connect(db_path)
            alerts = pd.read_sql("SELECT * FROM alerts", conn)
            conn.close()
            st.dataframe(alerts)
        except:
            st.info("No alerts yet.")

except Exception as e:
    st.error(f"Data load error: {e}")

# Gemini Chatbot
st.subheader("🤖 Ask AI")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

query = st.text_input("Ask about mood trends, summaries, or alerts:")

if query:
    with st.spinner("Thinking..."):
        try:
            prompt = f"""
You have two tables:
1. mood_logs(user_id, message, step, direction, mood, intent, timestamp)
2. alerts(user_id, reason, timestamp)

Write a SQLite query to answer:
{query}
Only return the query.
"""
            raw = model.generate_content(prompt).text.strip()
            sql = re.sub(r"^```sql|```$", "", raw, flags=re.IGNORECASE).strip()
            st.code(sql, language="sql")

            with sqlite3.connect(db_path) as conn:
                result = pd.read_sql(sql, conn)
                st.dataframe(result)

        except Exception as e:
            st.error(f"Error: {e}")