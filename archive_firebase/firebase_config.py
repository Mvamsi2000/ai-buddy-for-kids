import os
from dotenv import load_dotenv
from firebase_admin import credentials, firestore, initialize_app

# Load .env file
load_dotenv()

# Initialize Firebase
cred = credentials.Certificate(os.getenv("FIREBASE_CREDENTIALS_PATH"))
initialize_app(cred)
db = firestore.client()

# Save quiz answers and personality summary
def log_personality_result(user_id, answers, summary):
    db.collection("users").document(user_id).set({
        "quiz_answers": answers,
        "summary": summary
    }, merge=True)
