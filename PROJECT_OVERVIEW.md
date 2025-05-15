# 💠 Project Overview — AI Buddy for Kids

This is a **social-impact AI project** built to support children (especially those in low-income or orphanage settings) by providing a caring, psychologically-aware chatbot via WhatsApp.

---

## 🌟 Purpose

* Promote emotional expression in children through guided conversations
* Track emotional states using AI-generated insights
* Alert caregivers when patterns of sadness or emotional distress appear
* Work entirely through WhatsApp to remove access barriers — no app installs, logins, or devices required

---

## 👤 Target Users

* Children from underprivileged or high-risk backgrounds
* Teachers and volunteers at schools or NGOs
* Mental wellness professionals working in low-resource settings
* AI/tech contributors who want to build for good

---

## 🧠 Key Features

| Feature                 | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| 📱 WhatsApp Interface   | Chat with the child directly over WhatsApp (via Twilio)      |
| 🎨 Personality Quiz     | Gemini generates 5 random questions (psychologically guided) |
| ☁️ Mood Check-in        | Final 6th question captures emotional state                  |
| 🧠 Gemini Summarization | Personality summary after quiz completion                    |
| 📊 Mood Inference       | Inferred mood + intent stored via Gemini                     |
| 🚨 Sadness Alerts       | Trigger if 2+ “sad” responses over multiple check-ins        |
| 📂 Local Database       | SQLite structured logging                                    |
| 🖥️ Streamlit Dashboard | Teacher/volunteer view of mood logs, alerts, summaries       |
| 🤖 Gemini SQL Chatbot   | Ask dashboard questions (e.g. “when was this child sad?”)    |

---

## 📆 Folder Structure

```
ai-buddy-for-kids/
├── backend/
│   ├── app.py               # Flask + Twilio core logic
│   ├── gemini_agent.py      # Gemini-based personality, mood, summary logic
│   ├── mood_logs.db         # SQLite data store (auto-created)
│   └── settings.json        # Mode switch (quiz / mood_checkin)
├── dashboard/
│   └── streamlit_app.py     # Streamlit dashboard + Gemini SQL assistant
├── .env                     # API keys (excluded from Git)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠️ Development Setup

1. **Clone the repository and set up your virtual environment**:

```bash
git clone git@github.com:your-username/ai-buddy-for-kids.git
cd ai-buddy-for-kids
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. **Start Flask server**:

```bash
cd backend
python app.py
```

3. **Expose Flask locally using ngrok**:

```bash
ngrok http http://127.0.0.1:5000
```

Use the HTTPS URL from ngrok as your Twilio webhook.

4. **Start the Streamlit dashboard** (in a new terminal):

```bash
cd dashboard
streamlit run streamlit_app.py
```

---

## 🔀 Mode Switching (Quiz vs Mood Check-in)

Edit `backend/settings.json`:

```json
{
  "mode": "quiz"
}
```

To switch to mood check-in mode:

```json
{
  "mode": "mood_checkin"
}
```

---

## 🏛️ Database Schema

### mood\_logs

| Column    | Type    | Description                     |
| --------- | ------- | ------------------------------- |
| user\_id  | TEXT    | WhatsApp number                 |
| message   | TEXT    | Message content                 |
| step      | INTEGER | Step number in quiz / mood      |
| direction | TEXT    | 'user' or 'bot'                 |
| mood      | TEXT    | Inferred mood (if applicable)   |
| intent    | TEXT    | Inferred intent (if applicable) |
| timestamp | TEXT    | ISO timestamp                   |

### alerts

| Column    | Type | Description                       |
| --------- | ---- | --------------------------------- |
| user\_id  | TEXT | WhatsApp number                   |
| reason    | TEXT | e.g. “Inferred sad mood 2+ times” |
| timestamp | TEXT | Time of alert                     |

---

## ✨ Suggested Contributions

* Improve Gemini prompts for more psychological richness
* Add visualizations: mood trends, emotion clouds
* Enable dashboard user login (for teachers)
* Replace SQLite with PostgreSQL for scale
* Add multi-child profiles or session management
* Enable email alerts via SMTP or third-party APIs

---

## 📢 Author

**Vamsi Kalyan Reddy**
🌍 Canada / India

---

## ❤️ Why This Matters

AI can be more than just a tool — it can be a friend, a listener, and a safety net. This project gives a voice to children who may not otherwise be heard.

**Let’s build AI that protects, not replaces — and supports, not judges.**
