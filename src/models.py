import firebase_admin
from firebase_admin import credentials, firestore

from werkzeug.security import check_password_hash, generate_password_hash

import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://jsonkeeper.com/b/" + os.getenv("creds")

req = requests.get(url, json=None).json()
cred = credentials.Certificate(req)
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


def d_gauth(email):
    if db.collection("Google-Users").document(email).get().exists:
        return True
    db.collection("Google-Users").document(email).set(
        {}
    )
    return False


def d_signup(username, email, password):
    if db.collection("Users").document(username).get().exists:
        return False
    email_match = list(db.collection("Users").where(
        "Email", "==", email).limit(1).stream())
    if email_match:
        return False
    db.collection("Users").document(username).set(
        {
            "Email": email,
            "Password": generate_password_hash(password)
        }
    )
    return True


def d_delete(username, email, password):
    print(username, email, password)
    if username:
        if not check_password_hash(get("Users", username, "Password"), password):
            return False
        user_sites = list(db.collection("Sites").where(
            "Creator", "==", db.collection("Users").document(username)).stream())
        print(user_sites, "Users/" + username)
        for site in user_sites:
            db.collection("Sites").document(site.id).delete()
        db.collection("Users").document(username).delete()
        return True
    user_sites = list(db.collection("Sites").where(
        "Creator", "==", db.collection("Google-Sites").document(email)).stream())
    print(user_sites, "Users/" + username)
    for site in user_sites:
        db.collection("Sites").document(site.id).delete()
    db.collection("Google-Users").document(email).delete()
    return True

def d_change_pwd(username, old, new):
    if not username:
        return False
    if not check_password_hash(get("Users", username, "Password"), old):
        return False
    db.collection("Users").document(username).update({
        "Password": generate_password_hash(new)
    })
    return True

def d_get_sites(username, email):
    if username:
        return list(db.collection("Sites").where("Creator", "==", db.collection("Users").document(username)).stream())
    return list(db.collection("Sites").where("Creator", "==", db.collection("Google-Users").document(email)).stream())

def d_create(username, email, sitename, html_code):
    if db.collection("Sites").document(sitename).get().exists:
        return False
    if username:
        db.collection("Sites").document(sitename).set(
            {
                "Creator": db.document("Users/" + username),
                "HTML": html_code,
                "Published": False
            }
        )
    else:
        db.collection("Sites").document(sitename).set(
            {
                "Creator": db.document("Google-Users/" + email),
                "HTML": html_code,
                "Published": False
            }
        )
    return True

def d_edit(username, email, sitename, html_code):
    if not db.collection("Sites").document(sitename).get().exists:
        return False
    if username:
        if not get("Sites", sitename, "Creator") == db.collection("Users").document(username):
            return False
    else:
        if not get("Sites", sitename, "Creator") == db.collection("Google-Users").document(email):
            return False
    db.collection("Sites").document(sitename).update(
        {
            "HTML": html_code
        }
    )
    return True


def d_get_site(username, email, sitename):
    if not db.collection("Sites").document(sitename).get().exists:
        return False
    if username:
        if not get("Sites", sitename, "Creator") == db.collection("Users").document(username):
            return False
    else:
        if not get("Sites", sitename, "Creator") == db.collection("Google-Users").document(email):
            return False
    return [sitename, db.collection("Sites").document(sitename).get().to_dict()]


def d_site(sitename):
    if not db.collection("Sites").document(sitename).get().exists:
        return False
    if not get("Sites", sitename, "Published"):
        return False
    return get("Sites", sitename, "HTML")

def d_publish(username, email, sitename):
    if not db.collection("Sites").document(sitename).get().exists:
        return False
    if username:
        if not get("Sites", sitename, "Creator") == db.collection("Users").document(username):
            return False
    else:
        if not get("Sites", sitename, "Creator") == db.collection("Google-Users").document(email):
            return False
    db.collection("Sites").document(sitename).update(
        {
            "Published": True
        }
    )
    return True


def d_unpublish(username, email, sitename):
    if not db.collection("Sites").document(sitename).get().exists:
        return False
    if username:
        if not get("Sites", sitename, "Creator") == db.collection("Users").document(username):
            return False
    else:
        if not get("Sites", sitename, "Creator") == db.collection("Google-Users").document(email):
            return False
    db.collection("Sites").document(sitename).update(
        {
            "Published": False
        }
    )
    return True

def d_get_published_sites():
    return list(db.collection("Sites").where("Published", "==", True).stream())
