Absolutely — here’s the complete, clean, professional README.md you can copy and paste directly into your GitHub repo.

Save this as README.md in your project root (ai-buddy-for-kids/):

⸻


# 🤖 AI Buddy for Kids (WhatsApp + Gemini + Streamlit)

A friendly AI-powered WhatsApp buddy that chats with children, tracks their moods, creates personalized summaries, and alerts caregivers when emotional help might be needed.

> 💡 Built for underprivileged children, NGOs, and school mental wellness programs.

---

## 🎯 Project Goals

- Encourage emotional self-expression in children
- Track moods gently and respectfully over time
- Alert adults when sadness or risk patterns appear
- Build trust via WhatsApp — no apps, no logins

---

## 🧠 Key Features

✅ 5-question randomized personality quiz  
✅ Mood check-in via a 6th question  
✅ Gemini-powered personality summary  
✅ Gemini-based mood + intent detection  
✅ Alert system for repeated sadness  
✅ Streamlit dashboard + AI chatbot (SQL via Gemini)  
✅ Fully local: SQLite, Flask, Streamlit (no cloud costs)

---

## 🧱 Tech Stack

| Feature            | Technology                     |
|--------------------|--------------------------------|
| Messaging          | Twilio WhatsApp                |
| AI logic           | Google Gemini 1.5 Flash        |
| Backend            | Python + Flask                 |
| Database           | SQLite (structured schema)     |
| Dashboard          | Streamlit                      |
| AI SQL Chatbot     | Gemini → SQL generation        |
| Deployment (local) | ngrok tunnel for Flask         |

---

## 📂 Folder Structure

ai-buddy-for-kids/
├── backend/
│   ├── app.py               # Flask + Twilio logic
│   ├── gemini_agent.py      # Gemini API calls
│   ├── mood_logs.db         # SQLite database (auto created)
│   └── settings.json        # Mode switch (quiz / mood check-in)
├── dashboard/
│   └── streamlit_app.py     # Mood dashboard + chatbot
├── .env                     # API keys (excluded from Git)
├── .gitignore
├── requirements.txt
└── README.md

---

## 🚀 How to Run

### 🔧 Install requirements

```bash
cd ai-buddy-for-kids
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


⸻

🧠 Run the backend (Flask)

cd backend
python app.py


⸻

🌐 Start ngrok (to expose local server)

ngrok http http://127.0.0.1:5000

Copy the HTTPS URL and paste into your Twilio WhatsApp sandbox (Webhook → POST URL).

⸻

📲 Test it

From your Twilio WhatsApp test number, send:

Hi

You’ll receive:
	•	A fun quiz if in "quiz" mode
	•	A mood check-in if in "mood_checkin" mode

⸻

📊 Launch Dashboard

cd dashboard
streamlit run streamlit_app.py

Then go to: http://localhost:8501

You’ll see:
	•	Mood trends (step 5 only)
	•	Mood breakdowns
	•	Alert history
	•	Gemini-powered chatbot to query mood_logs.db

⸻

🧠 Data Schema (SQLite)

mood_logs

Field	Type	Description
user_id	TEXT	WhatsApp number
message	TEXT	Message from user or bot
step	INT	Quiz step number (or 5 for mood)
direction	TEXT	‘user’ or ‘bot’
mood	TEXT	Gemini-inferred mood (if applicable)
intent	TEXT	Gemini-inferred intent
timestamp	TEXT	ISO timestamp

alerts

Field	Type	Description
user_id	TEXT	WhatsApp number
reason	TEXT	e.g. “Inferred sad mood 2+ times”
timestamp	TEXT	Triggered time


⸻

🛡️ TODO / In Progress
	•	Login protection for dashboard
	•	Better quiz questions (psychologically tuned)
	•	Parental/NGO dashboard roles
	•	Daily check-in script (Twilio scheduler)
	•	Multi-language support
	•	Export to CSV/Excel
	•	Deploy to Streamlit Cloud / Render

⸻

✨ Ideal Use Cases
	•	Orphanage AI buddy
	•	Volunteer mental health tool
	•	Primary school classroom assistant
	•	NGO monitoring dashboard
	•	Low-cost early warning system

⸻

👨‍💻 Author

Vamsi Kalyan Reddy
📫 kalyanvamsi202000@gmail.com
🌍 Canada / India
🎓 Data Engineer | Business Analyst | AI for Good Enthusiast

⸻

⭐ Contribute

Ideas? Want to help improve child AI systems?
Fork this repo and open a PR or issue — let’s build together. 💛

⸻

“The most important thing in communication is hearing what isn’t said.” — Peter Drucker

---

Let me know if you'd like:
- A version with shields.io badges (build, Python version, license)
- A GitHub Pages landing page version
- A `docs/README.md` that turns into a printable PDF

You're ready to go open source now ✨
