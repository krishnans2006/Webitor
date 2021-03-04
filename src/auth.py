from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
# from . import db
# from .models import User

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
