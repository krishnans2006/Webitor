from os import path
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "]'/.;[pl,mkoijnbhuygvcftrdxzsewaq"
    app.config["SESSION_COOKIE_PATH"] = '/'

    from .views import views
    from .auth import auth
    from .sites import sites

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(sites, url_prefix='/')

    return app
