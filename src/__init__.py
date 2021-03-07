from flask import Flask
from flask_talisman import Talisman
from os import path
from authlib.integrations.flask_client import OAuth

def create_app():
  app = Flask(__name__)
  Talisman(app)
  oauth = OAuth(app)
  # oauth.register(

  # )
  app.config['SECRET_KEY'] = "test123"

  from .views import views
  from .auth import auth

  app.register_blueprint(views, url_prefix="/")
  app.register_blueprint(auth, url_prefix="/")

  return app
