import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("helpers/creds.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def get(coll, doc, field):
    return db.collection(coll).document(doc).get({field}).to_dict()[field]

def d_login(email, password):
    if "@" in email and "." in email:
        match = list(db.collection("Users").where("Email", "==", email).limit(1).stream())[0].to_dict()
    else:
        if db.collection("Users").document(email).get().exists:
            return {
                "Username": email,
                "Email": get("Users", email, "Email")
            }
        else:
            return False

def d_signup(username, email, password):
    if db.collection("Users").document(username).get().exists:
        return False
    db.collection("Users").document(username).set(
        {
            "Email": email,
            "Password": password
        }
    )