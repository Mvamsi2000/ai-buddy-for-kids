# 🧠 AI Buddy for Kids

An open-source, social-impact AI project designed to support the **emotional well-being of underprivileged children** via WhatsApp. The goal is to create a child-friendly AI companion that can chat daily, understand personality traits, detect mood trends, and alert caregivers if sadness is detected repeatedly.

---

## 🔧 Key Features

* 📱 **WhatsApp Chatbot** (via Twilio + Flask)
* 🎨 **AI-generated Personality Quiz** (randomized, child-safe)
* 🌤️ **Daily Mood Check-in** with Gemini-based inference
* 🧠 **Positive Personality Summary Generation**
* 💾 **SQLite Logging** with mood, message, intent & timestamps
* 🚨 **Sad Mood Detection & Alerting System**
* 📊 **Streamlit Dashboard** for teachers/volunteers
* 🤖 **Gemini-powered SQL Chatbot** for querying the mood database

---

## 📁 Folder Structure

```
ai-buddy-for-kids/
├── backend/
│   ├── app.py               # Main Flask + Twilio interaction
│   ├── gemini_agent.py      # Gemini prompt handling and logic
│   ├── settings.json        # Mode toggle (quiz / mood_checkin)
│   └── mood_logs.db         # SQLite DB (auto-created)
├── dashboard/
│   └── streamlit_app.py     # Teacher-facing mood dashboard
├── .env                     # Secrets for Gemini & Twilio (not committed)
├── .gitignore
├── requirements.txt         # All dependencies
├── README.md
└── PROJECT_OVERVIEW.md      # Contribution-oriented guide
```

---

## 🧠 How It Works

1. **Child sends a message on WhatsApp**
2. **AI buddy replies with quiz/mood question**
3. **Gemini generates personality insights + detects mood**
4. **All chats are stored in SQLite**
5. **Alerts are raised if multiple "sad" moods are detected**
6. **Dashboard shows logs, summaries, alerts, trends**

---

## 🧰 Tech Stack

| Layer      | Tech Used                  |
| ---------- | -------------------------- |
| Backend    | Flask, Twilio, SQLite      |
| AI Engine  | Google Gemini (via API)    |
| Frontend   | Streamlit (for dashboard)  |
| Scheduler  | Python `schedule` (manual) |
| Deployment | Localhost + ngrok tunnel   |

---

## ⚙️ Local Setup

```bash
git clone git@github.com:your-username/ai-buddy-for-kids.git
cd ai-buddy-for-kids
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Start the Flask server:

```bash
cd backend
python app.py
```

Expose your local server to Twilio:

```bash
ngrok http http://127.0.0.1:5000
```

Run the dashboard:

```bash
cd dashboard
streamlit run streamlit_app.py
```

---

## 🔀 Mode Switching (Quiz vs Mood Check-in)

Edit `backend/settings.json` to switch modes:

```json
{
  "mode": "quiz"
}
```

or:

```json
{
  "mode": "mood_checkin"
}
```

---

## 🗃️ Database Schema

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
| reason    | TEXT | e.g. "Inferred sad mood 2+ times" |
| timestamp | TEXT | Time of alert                     |

---

## ✅ MVP Goals

* [x] WhatsApp-based personality quiz
* [x] Mood tracking with SQLite
* [x] Alert system if child reports "sad" multiple times
* [x] Teacher-facing dashboard with visualizations
* [x] AI assistant to run SQL queries via Gemini

---

## 🗓️ Roadmap

* [ ] User profile system with multi-session tracking
* [ ] Dashboard logins for teachers/NGO staff
* [ ] Advanced prompt tuning for richer summaries
* [ ] Support for multiple languages (Hindi, Telugu, etc.)
* [ ] Deploy on Render or Streamlit Cloud
* [ ] Add export to CSV / PDF features

---

## 🤝 Contributions Welcome

If you're a developer, psychologist, teacher, or AI enthusiast interested in helping children through technology, feel free to fork this repo or submit a pull request.

---

## 📬 Contact

**Author:** Vamsi Kalyan Reddy
**Location:** Canada / India

---

## ❤️ Why This Matters

This project is created with the intention to:

* Give children a voice
* Help educators detect early signs of distress
* Explore how GenAI can assist in real-world emotional wellness

**AI should heal, not harm. Let’s build something that matters.**
