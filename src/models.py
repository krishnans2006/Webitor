import firebase_admin
from firebase_admin import credentials, firestore

from werkzeug.security import check_password_hash, generate_password_hash

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
            if check_password_hash(match[0].to_dict()["Password"], password):
                return {
                    "Username": match[0].id,
                    "Email": match[0].to_dict()["Email"]
                }
            return False
        return False
    else:
        username = email
        if db.collection("Users").document(username).get().exists:
            if check_password_hash(get("Users", username, "Password"), password):
                return {
                    "Username": username,
                    "Email": get("Users", username, "Email")
                }
            return False
        return False


def d_signup(username, email, password):
    if db.collection("Users").document(username).get().exists:
        return False
    email_match = list(db.collection("Users").where("Email", "==", email).limit(1).stream())
    if email_match:
        return False
    db.collection("Users").document(username).set(
        {
            "Email": email,
            "Password": generate_password_hash(password)
        }
    )
    return True

def d_create(username, sitename, html_code):
    if db.collection("Sites").document(sitename).get().exists:
        return False
    db.collection("Sites").document(sitename).set(
        {
            "Sitename": sitename,
            "Creator": db.document("Users/" + username),
            "HTML": html_code,
            "Published": False
        }
    )
    return True

def d_edit(username, sitename, html_code):
    if not db.collection("Sites").document(sitename).get().exists:
        return False
    if not get("Sites", sitename, "Creator").path.split("/")[1] == username:
        return False
    db.collection("Sites").document(sitename).update(
        {
            "HTML": html_code
        }
    )

def d_publish(username, sitename):
    if not db.collection("Sites").document(sitename).get().exists:
        return False
    if not get("Sites", sitename, "Creator").path.split("/")[1] == username:
        return False
    db.collection("Sites").document(sitename).update(
        {
            "Published": True
        }
    )