import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def create_app():
    print("The app is running")
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    from .routes import main
    app.register_blueprint(main)
    return app
