import firebase_admin
from firebase_admin import credentials, firestore

from werkzeug.security import check_password_hash

cred = credentials.Certificate("creds.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


def get(coll, doc, field):
    return db.collection(coll).document(doc).get({field}).to_dict()[field]


def d_login(email, password):
    if "@" in email and "." in email:
        match = list(db.collection("Users").where(
            "Email", "==", email).limit(1).stream())
        if match:
            return {
                "Username": match[0].id,
                "Email": match[0].to_dict()["Email"]
            }
        else:
            return False
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
    return d_login(username, password)