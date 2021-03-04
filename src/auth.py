from flask import Blueprint, render_template, request, flash, redirect, url_for

# from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

# from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)

# @auth.route('/login', methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         # email = request.form.get('email')
#         # password = request.form.get('password') DESIGN DATABASE FIRST
#         pass

#     return render_template('login.html')#, user=current_user)


# @auth.route('/logout')
# @login_required
# def logout():
#     # logout_user()
#     # return redirect(url_for('auth.login'))
#     pass

# @auth.route('/register', methods=["GET", "POST"])
# def register():
#     if request.method == "POST":
#         email = request.form.get("email")
#         username = request.form.get("username")
#         password = request.form.get("password")
#         confirm_password = request.form.get("confirm_password")

#     return render_template('register.html')#user=current_user
