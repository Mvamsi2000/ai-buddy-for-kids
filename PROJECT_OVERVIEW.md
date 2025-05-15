# 🧠 AI Buddy for Kids — Project Overview & Contribution Guide

A real-world, social impact AI project that uses WhatsApp and Google Gemini to help children express emotions, track mood trends, and alert caregivers when emotional help may be needed.

---

## 🎯 Purpose

To build a friendly, psychologically supportive AI that:
- Helps children express their feelings naturally
- Tracks emotional patterns over time
- Notifies teachers or caregivers if sadness or risk trends appear
- Works entirely over WhatsApp — no app installs needed

---

## 👥 Who Is This For?

- 💻 Backend / AI engineers
- 🎨 UX designers for social tech
- 🧑‍🏫 Teachers and NGOs working with kids
- 🤝 Contributors who want to work on AI for Good

---

## 🚀 Key Features

- 🌈 Personality quiz (5 random, child-friendly questions)
- 🌤️ Mood check-in as a 6th question
- ✨ Gemini-generated summary of personality
- 🧠 AI mood + intent classification
- 🚨 Sad mood alert system (2+ sad answers)
- 📊 Streamlit dashboard with mood trends + chatbot
- 💬 SQL chatbot (query moods, alerts, logs)
- 💾 Modular, local-first (SQLite + ngrok + Flask)

---

## 🧱 System Architecture

Twilio WhatsApp
↕
Flask Server (app.py)
↕
Gemini API + SQLite DB
↕
Streamlit Dashboard (dashboard/streamlit_app.py)

---

## 📂 Project Structure

<pre>

📦 ai-buddy-for-kids/
├── backend/
│   ├── app.py               # Flask app for WhatsApp + logging
│   ├── gemini_agent.py      # Gemini API logic (summary, mood, Qs)
│   ├── mood_logs.db         # SQLite DB (auto created)
│   └── settings.json        # Mode toggle: quiz / mood_checkin
├── dashboard/
│   └── streamlit_app.py     # Dashboard UI + SQL chatbot
├── .env                     # API keys (excluded from Git)
├── .gitignore
├── requirements.txt
├── README.md
└── PROJECT_OVERVIEW.md

</pre>

---

## 🔄 Mode Switching

Use `backend/settings.json` to control the interaction type:

```json
{
  "mode": "quiz"
}

Change to "mood_checkin" for daily check-in only.

Future: Add a Streamlit toggle for this mode control.

⸻

📊 Database Tables

mood_logs

Column	Type	Description
user_id	TEXT	WhatsApp number
message	TEXT	User or bot message
step	INT	Quiz step or 999 for summary
direction	TEXT	‘user’ or ‘bot’
mood	TEXT	AI-inferred mood (if any)
intent	TEXT	AI-inferred intent (optional)
timestamp	TEXT	ISO format timestamp

alerts

Column	Type	Description
user_id	TEXT	WhatsApp number
reason	TEXT	e.g. “Inferred sad mood 2+ times”
timestamp	TEXT	Time alert was triggered


⸻

🧠 AI Logic Modules

gemini_agent.py
	•	get_personality_questions() → 5 randomized quiz questions
	•	get_gemini_summary() → Personality summary from answers
	•	get_inferred_mood(text) → Returns mood (“Happy”, “Sad”, etc.)
	•	get_inferred_intent(text) → Returns purpose of text (“Greeting”, “Question”, etc.)

⸻

📈 Streamlit Dashboard Features
	•	Mood frequency chart
	•	Mood logs viewer (filtered by step or mood)
	•	Alert history
	•	Gemini chatbot (asks and converts questions to SQL)

⸻

🔧 Setup Instructions

1. Clone the project and install dependencies:

git clone https://github.com/YOUR_USERNAME/ai-buddy-for-kids.git
cd ai-buddy-for-kids
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

2. Run Flask server (WhatsApp bot):

cd backend
python app.py

3. Run ngrok to expose Flask:

ngrok http http://127.0.0.1:5000

Paste the ngrok HTTPS URL in your Twilio sandbox webhook.

4. Run dashboard:

cd dashboard
streamlit run streamlit_app.py


⸻

🧪 Example Flow

User: Hi 👋
Bot: Question 1: If you could have any animal as a pet, what would it be?
...
User: Sad
Bot logs mood = "Sad", intent = "MoodUpdate"
If 2+ sad responses → 🚨 Alert inserted


⸻

🛠️ Suggested Contribution Areas

Area	Tasks You Can Help With
AI prompts	Better questions, better summaries
Dashboard UI	Login system, visual polish, export options
Scheduler	Daily check-in script (Twilio + cron or schedule)
Data design	Move from SQLite to Firebase/PostgreSQL
NLP	Improve mood/intent classification
Analytics	More advanced emotional trend tracking


⸻

🤝 How to Contribute
	1.	Fork this repo
	2.	Clone it and create a new branch
	3.	Submit a pull request with clear explanation
	4.	Bonus: Open an issue if you have questions or feature ideas

⸻

📫 Contact

Vamsi Kalyan Reddy
📧 kalyanvamsi202000@gmail.com
🌐 Canada / India | Open to meaningful collaboration

⸻

❤️ Why This Matters

Not every child has someone to talk to — but with the right AI, we can at least make sure they’re heard, seen, and supported.

“Mental health starts with listening. Even if it’s a bot — listening matters.”

⸻


