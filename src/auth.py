from flask import Blueprint, flash, redirect, render_template, request, url_for, session, current_app
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
from .models import *

from google.oauth2 import id_token
from google.auth.transport import requests

auth = Blueprint("auth", __name__)

@auth.before_app_request
def force_https():
    if request.endpoint in current_app.view_functions and request.headers.get('X-Forwarded-Proto', None) == 'http':
        return redirect(request.url.replace('http://', 'https://'))

@auth.route('/google-signin', methods=["GET", "POST"])
def google_signin():
    if session.get("logged_in"):
        flash("You are already signed in!", category='error')
        return redirect(url_for('views.index'))
    
    return render_template('Google-Sign-In/google.html')

@auth.route("/google-auth", methods=["GET", "POST"])
def google_auth():
    if request.method == "GET":
        return redirect(url_for("auth.login"))
    token = request.form.get("idtoken")
    print(token)
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(
        ), "337745045052-c19u56smhk30nck0dat09vigoe7fcolf.apps.googleusercontent.com")
        print("Email", idinfo["email"])
        result = d_gauth(idinfo["email"])
        if result:
            flash(f"You have successfully logged back in as {idinfo['email']}!", category='success')
        else:
            flash(f"Your account has successfully been created and you are now logged in as {idinfo['email']}!", category='success')
        session["logged_in"] = True
        session["g_auth"] = True
        session["email"] = idinfo["email"]
        return "Success!"
    except ValueError:
        flash("Your login was invalid! Make sure you have provided permissions to access your email address", category='error')
        return "Error!"


@auth.route('/login', methods=["GET", "POST"])
def login():
    if session.get("logged_in"):
        return redirect(url_for("views.index"))
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        result = d_login(email, password)
        if result:
            session["logged_in"] = True
            session["username"] = result["Username"]
            session["email"] = result["Email"]
            flash("You are successfully logged in!", category='success')
            return redirect(url_for("views.index"))
        else:
            flash("Invalid Username or Password!", category='error')
            return redirect(url_for("auth.login"))
    return render_template('Login/login.html')


@auth.route('/logout')
def logout():
    if not session.get("logged_in"):
        flash("You are already logged out!", category='error')
        return redirect(url_for('auth.login'))
    else:
        session.clear()
        flash("You have been successfully logged out!", category='success')
        return redirect(url_for("auth.login"))


@auth.route('/register', methods=["GET", "POST"])
def register():
    if session.get("logged_in"):
        return redirect(url_for("views.index"))
    if request.method == "POST":
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        if len(email) < 4:
            flash('Your email must be greater than 3 characters!', category='error')
        elif len(username) <= 5:
            flash('Your username must be greater than 5 characters!', category='error')
        elif len(password) < 8:
            flash('Your password should be 8 characters or more!', category='error')
        else:
            if d_signup(username, email, password=password):
                flash("Successfully Registered!", category='error')
                flash(f"You are now logged in as {username}!", category='success')
                return redirect(url_for("views.index"))
            else:
                flash("Someone is already registered with this username or password!", category='error')
    return render_template('Register/register.html')


@auth.route('/projects', methods=["GET", "POST"])
def projects():
    if not session.get('logged_in'):
        flash('You must be logged in to view your projects!', category='error')
        return redirect(url_for('auth.login'))
    return render_template('Profile/profile.html', sites=d_get_sites(session.get("username"), session.get("email")))

@auth.route('/create', methods=["GET", "POST"])
def create():
    if not session.get('logged_in'):
        flash("You must login to create a website!", category='error')
        return redirect(url_for("auth.login"))
    else:
        styles = [{'style':'Cool Breeze'}, {'style':'Sun Rise'}, {'style':'Dark Mountains'}]
        types = [{'type':'Test One'}, {'type':'Test Two'}, {'type':'Test Three'}]

        if request.method == "POST":
            web_name = request.form.get("web-name")
            web_style = request.form.get("web-style")
            web_type = request.form.get("web-type")
            #READY TO ADD TO DATABASE
            flash("Test Flash Message", category='success')
            # Add ID to database for editing later on
        else:
            return render_template('Create/create.html', styles=styles, types=types)


@auth.route('/edit', methods=["GET", "POST", "PUT", "DELETE"]) #<int:id>
def edit():
    if not session.get('logged_in'):
        flash("You must be logged in to edit your projects!", category='error')
        return redirect(url_for('auth.login'))
    
    return render_template('Edit/edit.html')
