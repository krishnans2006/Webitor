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
            flash("1You are successfully logged in!")
            return redirect(url_for("views.index"))
        else:
            flash("0Invalid Username or Password!")
            return redirect(url_for("auth.login"))
    return render_template('login.html')


@auth.route('/logout')
def logout():
    if not session.get("logged_in"):
        flash("0You are already logged out!")
        return redirect(url_for('auth.login'))
    else:
        session.clear()
        flash("1You have been successfully logged out!")
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
            flash('0Your email must be greater than 3 characters!')
        elif len(username) <= 5:
            flash('0Your username must be greater than 5 characters!')
        elif len(password) < 8:
            flash('0Your password should be 8 characters or more!')
        else:
            d_signup(username, email, password=generate_password_hash(password))
            flash("1Successfully Registered!")
            return redirect(url_for("views.index"))
    return render_template('register.html')

@auth.route('/projects', methods=["GET", "POST"])
def projects():
    if not session.get('logged_in'):
        flash('0You must be logged in to view your projects!')
        return redirect(url_for('auth.login'))
    else:
        return render_template('profile.html')

@auth.route('/create', methods=["GET", "POST"])
def create():
    if not session.get('logged_in'):
        flash("0You must login to create a website!")
        return redirect(url_for("auth.login"))
    else:
        styles = [{'style':'Cool Breeze'}, {'style':'Sun Rise'}, {'style':'Dark Mountains'}]
        types = [{'type':'Test One'}, {'type':'Test Two'}, {'type':'Test Three'}]

        if request.method == "POST":
            web_name = request.form.get("web-name")
            web_style = request.form.get("web-style")
            web_type = request.form.get("web-type")
            #READY TO ADD TO DATABASE
            flash("1Test Flash Message")
        else:
            return render_template('create.html', styles=styles, types=types)