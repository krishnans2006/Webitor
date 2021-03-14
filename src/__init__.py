from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "]'/.;[pl,mkoijnbhuygvcftrdxzsewaq"
    app.config["SESSION_COOKIE_PATH"] = '/'

    from .site import site

    app.register_blueprint(site, url_prefix='/')
    return app
