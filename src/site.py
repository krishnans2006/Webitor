from flask import Blueprint, flash, redirect, render_template, request, url_for, session, current_app
from .models import *
from generator import generator
from google.oauth2 import id_token
from google.auth.transport import requests
import os
from dotenv import load_dotenv

load_dotenv()

site = Blueprint("site", __name__)

@site.before_app_request
def force_https():
    if request.endpoint in current_app.view_functions and request.headers.get('X-Forwarded-Proto', None) == 'http':
        return redirect(request.url.replace('http://', 'https://'))

@site.route('/', methods=["GET", "POST"])
def index():
    return render_template('Index/index.html', youtube=os.getenv("youtube"))

@site.route("/s/<sitename>")
def official_site(sitename):
    site_code = d_site(sitename)
    if not site_code:
        flash("This site either doesn't exist, or is not published yet. Please make sure the site name is correct!", category="error")
        return redirect(url_for("site.index"))
    return site_code

@site.route('/about', methods=["GET", "POST"])
def about():
    return render_template('About/about.html')


@site.route('/google-signin', methods=["GET", "POST"])
def google_signin():
    if session.get("logged_in"):
        return redirect(url_for('site.index'))
    return render_template('Google-Sign-In/google.html')

@site.route("/google-auth", methods=["GET", "POST"])
def google_auth():
    if request.method == "GET":
        return redirect(url_for("site.login"))
    token = request.form.get("idtoken")
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(
        ), "337745045052-c19u56smhk30nck0dat09vigoe7fcolf.apps.googleusercontent.com")
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


@site.route('/login', methods=["GET", "POST"])
def login():
    if session.get("logged_in"):
        return redirect(url_for("site.index"))
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')
        result = d_login(email, password)
        if email and password:
            if result:
                session["logged_in"] = True
                session["username"] = result["Username"]
                session["email"] = result["Email"]
                flash(f"You are now logged in as {session['username']}!", category='success')
                return redirect(url_for("site.index"))
            else:
                flash("Invalid Username or Password!", category='error')
                return redirect(url_for("site.login"))
        else:
            flash("Please fill in the empty fields!", category="error")
            return redirect(url_for('site.login'))

    return render_template('Login/login.html')


@site.route('/register', methods=["GET", "POST"])
def register():
    if session.get("logged_in"):
        return redirect(url_for("site.index"))
    if request.method == "POST":
        email = request.form.get("email")
        fname = request.form.get("first-name")
        lname = request.form.get("last-name")
        password = request.form.get("password")
        if len(email) < 4:
            flash('Your email must be greater than 3 characters!', category='error')
        elif len(password) < 8:
            flash('Your password should be 8 characters or more!', category='error')
        else:
            username = fname + lname
            f_username = username
            num = None
            while not d_signup(f_username, email, password):
                if not num:
                    num = 0
                num += 1
                f_username = username + str(num)
            session["logged_in"] = True
            session["username"] = f_username
            session["email"] = email
            flash(
                f"Successfully Registered as {f_username}!", category='success')
            return redirect(url_for("site.index"))
    return render_template('Register/register.html')


@site.route('/logout')
def logout():
    if not session.get("logged_in"):
        flash("You are already logged out!", category='error')
        return redirect(url_for('site.login'))
    else:
        session.clear()
        flash("You have been successfully logged out!", category='success')
        return redirect(url_for("site.login"))

@site.route('/change-password', methods=["GET", "POST"])
def change_password():
    if request.method == "POST":
        old_pass = request.form.get('current-password')
        new_pass = request.form.get('new-password') 
        result = d_change_pwd(session.get("username"), old_pass, new_pass)
        if result:
            flash("Password has been changed!", category='success')
            return redirect(url_for('site.index'))
        flash("Password change has failed", category='error')
        return redirect(url_for('site.index'))
    return render_template('Change/change.html')

@site.route('/delete-account', methods=["GET", "POST"])
def delete_account():
    if request.method == "POST":
        password = request.form.get('password')

        if d_delete(session.get("username"), session.get("email"), password):
            session.clear()
            flash("Account deleted!", category="success")
            return redirect(url_for('site.register'))
        else:
            flash("Account deletion unsuccessful!", category="error")
            return redirect(url_for("site.delete_account"))
    return render_template('Delete/delete.html')


@site.route('/projects', methods=["GET", "POST"])
def projects():
    if not session.get('logged_in'):
        flash('You must be logged in to view your projects!', category='error')
        return redirect(url_for('site.login'))
    return render_template('Profile/profile.html', sites=d_get_sites(session.get("username"), session.get("email")))


@site.route('/create', methods=["GET", "POST"])
def create():
    if not session.get('logged_in'):
        flash("You must login to create a website!", category='error')
        return redirect(url_for("site.login"))
    else:
        if request.method == "POST":
            web_name = request.form.get("web-name")
            gen_code = generator()
            if d_create(session.get('username'), session.get('email'), web_name, gen_code):
                flash(f"Successfully created site {web_name}!", category='success')
                return redirect(url_for("site.edit", sitename=web_name))
            else:
                flash(f"A site with this name already exists! Please try again with another sitename.", category='error')
                return redirect(url_for("site.create"))
        else:
            return render_template('Create/create.html')


@site.route('/edit/<sitename>', methods=["GET", "POST"])
def edit(sitename=None):
    if not session.get('logged_in'):
        flash("You must be logged in to edit your projects!", category='error')
        return redirect(url_for('site.login')) 
    if not sitename:
        flash("An Internal Error Occured! This has been reported and will be resolved soon. Thanks for the patience!", category="error")
    if request.method == "POST":
        new_code = request.form.get("code")
        d_edit(session.get("username"), session.get("email"), sitename, new_code)
        return ""
    site = d_get_site(session.get("username"), session.get("email"), sitename)
    return render_template('Edit/edit.html', name=site[0], code=site[1]["HTML"], published=site[1]["Published"])

@site.route('/publish/<sitename>', methods=["GET", "POST"])
def publish(sitename=None):
    if not session.get('logged_in'):
        flash("You must be logged in to edit your projects!", category='error')
        return redirect(url_for('site.login'))
    if not sitename:
        flash("An Internal Error Occured! This has been reported and will be resolved soon. Thanks for the patience!", category="error")
    if request.method == "POST":
        if d_publish(session.get("username"), session.get("email"), sitename):
            flash("Successfully published!", category="success")
            return redirect(url_for("site.official_site", sitename=sitename))
        flash("Site was not published.", category="error")
        return redirect(url_for("site.edit", sitename=sitename))
    return render_template("Publish/publish.html", site=sitename)


@site.route('/unpublish/<sitename>', methods=["GET", "POST"])
def unpublish(sitename=None):
    if not session.get('logged_in'):
        flash("You must be logged in to edit your projects!", category='error')
        return redirect(url_for('site.login'))
    if not sitename:
        flash("An Internal Error Occured! This has been reported and will be resolved soon. Thanks for the patience!", category="error")
    if request.method == "POST":
        if d_unpublish(session.get("username"), session.get("email"), sitename):
            flash("Successfully unpublished!", category="success")
            return redirect(url_for("site.edit", sitename=sitename))
        flash("Site is still published.", category="error")
        return redirect(url_for("site.official_site", sitename=sitename))
    return render_template("Unpublish/unpublish.html", site=sitename)
