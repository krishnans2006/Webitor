from os import path
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "]'/.;[pl,mkoijnbhuygvcftrdxzsewaq"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
# ohhh the problem is /google-auth won't load so Google Signin works but never gives any info to backend for some reason
#But does it work if we use a https link basically... b
# Good idea lemme try