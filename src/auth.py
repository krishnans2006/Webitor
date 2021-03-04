from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import session
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from .models import *

auth = Blueprint("auth", __name__)


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
    return render_template('login.html')


@auth.route('/logout')
def logout():
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
            flash('Your username must be greater than 5 characters!',
                  category='error')
        elif len(password) < 8:
            flash('Your password should be 8 characters or more!', category='error')
        else:
            d_signup(username, email, password=generate_password_hash(password))
            flash("Successfully Registered!", category='success')
            return redirect(url_for("views.index"))
    return render_template('register.html')

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
        else:
            return render_template('create.html', styles=styles, types=types)