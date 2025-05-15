# 🧠 Project Overview — AI Buddy for Kids

This is a **social-impact AI project** built to support children (especially those in low-income or orphanage settings) by providing a caring, psychologically-aware chatbot via WhatsApp.

---

## 🎯 Purpose

- Promote emotional expression in children through guided conversations
- Track emotional states using AI-generated insights
- Alert caregivers when patterns of sadness or emotional distress appear
- Work entirely through WhatsApp to remove access barriers — no app installs, logins, or devices required

---

## 👤 Target Users

- Children from underprivileged or high-risk backgrounds
- Teachers and volunteers at schools or NGOs
- Mental wellness professionals working in low-resource settings
- AI/tech contributors who want to build for good

---

## 🧠 Key Features

| Feature                        | Description                                                   |
|-------------------------------|---------------------------------------------------------------|
| 📱 WhatsApp Interface          | Chat with the child directly over WhatsApp (via Twilio)       |
| 🎨 Personality Quiz            | Gemini generates 5 random questions (psychologically guided)  |
| 🌤️ Mood Check-in              | Final 6th question captures emotional state                   |
| 🧠 Gemini Summarization        | Personality summary after quiz completion                    |
| 📊 Mood Inference             | Inferred mood + intent stored via Gemini                     |
| 🚨 Sadness Alerts              | Trigger if 2+ “sad” responses over multiple check-ins         |
| 📂 Local Database              | SQLite structured logging                                     |
| 🖥️ Streamlit Dashboard        | Teacher/volunteer view of mood logs, alerts, summaries        |
| 🤖 Gemini SQL Chatbot         | Ask dashboard questions (e.g. “when was this child sad?”)     |

---

## 📦 Folder Structure

<pre>

📁 ai-buddy-for-kids/
├── backend/
│   ├── app.py               # Flask + Twilio core logic
│   ├── gemini_agent.py      # Gemini-based personality, mood, summary logic
│   ├── mood_logs.db         # SQLite data store (auto-created)
│   └── settings.json        # Switch between quiz/mood_checkin modes
├── dashboard/
│   └── streamlit_app.py     # Streamlit dashboard + Gemini SQL assistant
├── .env                     # API keys (excluded from Git)
├── .gitignore
├── requirements.txt
└── README.md

</pre>

---

## 🧱 Architecture Overview

WhatsApp (Twilio)
↕
Flask Server (app.py)
↕
Gemini API + SQLite
↕
Streamlit Dashboard (teacher/volunteer view)

---

## 🗃️ Database Schema

### mood_logs

| Column     | Type    | Description                                 |
|------------|---------|---------------------------------------------|
| user_id    | TEXT    | WhatsApp number                             |
| message    | TEXT    | Message content                             |
| step       | INTEGER | Step number in quiz / mood                  |
| direction  | TEXT    | 'user' or 'bot'                             |
| mood       | TEXT    | Inferred mood (if applicable)               |
| intent     | TEXT    | Inferred intent (if applicable)             |
| timestamp  | TEXT    | ISO timestamp                               |

### alerts

| Column     | Type    | Description                                 |
|------------|---------|---------------------------------------------|
| user_id    | TEXT    | WhatsApp number                             |
| reason     | TEXT    | e.g. “Inferred sad mood 2+ times”           |
| timestamp  | TEXT    | When alert was logged                       |

---

## 🔀 Modes of Operation

Controlled by `backend/settings.json`:

```json
{
  "mode": "quiz"
}

Other option:

{
  "mode": "mood_checkin"
}

You can flip this manually or build a toggle in the dashboard later.

⸻

👨‍💻 How to Contribute

We welcome thoughtful contributions, especially in areas like:

🧠 Prompt Engineering
	•	Improve Gemini question phrasing and summary structure
	•	Add age-specific or trauma-informed question banks

📊 Data Visualization
	•	Add timeline charts, sentiment trackers, word clouds
	•	Dashboard enhancements for child-specific views

💻 Backend / Engineering
	•	Add teacher logins or authentication for dashboards
	•	Move SQLite to Postgres or cloud for production
	•	Add SMS fallback or Telegram support

🌍 Language Support / Accessibility
	•	Translate questions to local languages
	•	Add voice input/output (Twilio supports TTS)

⸻

🧪 Sample Contributions
	•	Improve mood classification prompt
	•	Auto-trigger alerts to teachers via email
	•	Add CSV export button to dashboard
	•	Deploy on Render or Streamlit Cloud
	•	Schedule check-ins with a cron + Twilio script

⸻

✅ Development Setup

git clone git@github.com:your-username/ai-buddy-for-kids.git
cd ai-buddy-for-kids
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Start Flask:

cd backend
python app.py

Expose with ngrok:

ngrok http http://127.0.0.1:5000

Start Streamlit dashboard:

cd dashboard
streamlit run streamlit_app.py


⸻

📫 Author

Vamsi Kalyan Reddy
🌍 Canada / India

⸻

❤️ Why This Matters

AI can be more than just a tool — it can be a friend, a listener, and a safety net. This project gives a voice to children and eyes to those who care for them.

Let’s build AI that protects, not replaces — and supports, not judges.

---
