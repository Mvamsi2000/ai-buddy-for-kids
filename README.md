# 🤖 AI Buddy for Kids (WhatsApp + Gemini + Streamlit)

A friendly AI-powered WhatsApp buddy that chats with children, tracks their moods, creates personalized summaries, and alerts caregivers when emotional help might be needed.

> 💡 Built for underprivileged children, NGOs, and school wellness programs.

---

## 🎯 Project Goals

- Encourage emotional self-expression in children
- Track moods gently and respectfully over time
- Alert caregivers when sadness or risk patterns appear
- Deliver this entirely over WhatsApp — no apps or logins

---

## 🧠 Features

- ✅ 5-question personality quiz (Gemini-generated)
- ✅ 6th mood check-in question with AI-inferred emotion
- ✅ Personality summary powered by Gemini 1.5 Flash
- ✅ Mood + intent classification
- ✅ Alert system (e.g., 2+ sad moods = trigger)
- ✅ SQLite for local, structured logging
- ✅ Streamlit dashboard + Gemini-powered chatbot
- ✅ Zero monthly cost: runs locally with ngrok

---

## 📦 Folder Structure

<pre>

📁 ai-buddy-for-kids/
├── backend/
│   ├── app.py               # Flask app, Twilio integration
│   ├── gemini_agent.py      # Gemini prompt logic
│   ├── mood_logs.db         # SQLite DB (auto-created)
│   └── settings.json        # Mode switch (quiz / mood_checkin)
├── dashboard/
│   └── streamlit_app.py     # Streamlit dashboard + chatbot
├── .env                     # API keys (excluded from Git)
├── .gitignore
├── requirements.txt
└── README.md

</pre>

---

## 🚀 How to Run the App

### 1. 📦 Install dependencies

```bash
cd ai-buddy-for-kids
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


⸻

2. ⚙️ Start the Flask server

cd backend
python app.py


⸻

3. 🌐 Start ngrok to expose your local server

ngrok http http://127.0.0.1:5000

Copy the HTTPS URL and paste it into the Twilio Sandbox Webhook for inbound messages.

⸻

4. 📲 Test on WhatsApp

From your registered Twilio sandbox WhatsApp number, send:

Hi

AI Buddy will:
	•	Start a quiz or mood check-in (based on mode)
	•	Log answers
	•	Respond using Gemini-generated replies

⸻

📊 How to Launch the Dashboard

In a new terminal:

cd dashboard
streamlit run streamlit_app.py

Visit http://localhost:8501 to view:
	•	All mood logs
	•	Mood frequency bar chart (filtered to step 5)
	•	Alert history
	•	Gemini-powered SQL chatbot

⸻

🗃️ Database Structure

mood_logs Table

Field	Type	Description
user_id	TEXT	WhatsApp number
message	TEXT	Message content
step	INT	Step number (0–5) or 999 for summary
direction	TEXT	‘user’ or ‘bot’
mood	TEXT	Inferred mood from Gemini (optional)
intent	TEXT	Inferred intent (optional)
timestamp	TEXT	ISO datetime

alerts Table

Field	Type	Description
user_id	TEXT	WhatsApp number
reason	TEXT	Reason for alert (e.g. sad x2)
timestamp	TEXT	Time of alert


⸻

⚙️ Project Modes (Quiz vs Mood Check)

Edit backend/settings.json to switch modes:

{
  "mode": "quiz"
}

Or:

{
  "mode": "mood_checkin"
}

You can add a Streamlit toggle later for UI control.

⸻

🔒 To-Do (Next Features)
	•	Add login to dashboard for teachers
	•	Upgrade personality question quality
	•	Auto daily reminders via script
	•	CSV / Excel export
	•	Streamlit Cloud or Render deployment
	•	Parental dashboard with child summaries

⸻

👨‍💻 Author

Vamsi Kalyan Reddy
📧 kalyanvamsi202000@gmail.com
🌍 Canada / India
🎓 Data Engineer • AI-for-Good Enthusiast

⸻

🧡 Why This Matters

This project helps kids express themselves safely and lets caregivers track emotional health early — even in underserved communities. Built with empathy, AI, and zero cloud cost.

⸻

“The most important thing in communication is hearing what isn’t said.” — Peter Drucker