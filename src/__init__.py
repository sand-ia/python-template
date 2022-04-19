"""Fantastic Brocolli setup."""
import os
from dotenv import load_dotenv
from flask import Flask
from .dependencies import configure
from flask_injector import FlaskInjector

# Load enviroment variables
load_dotenv()


def create_app() -> Flask:
    """Start Flask Application.

    :return: Flask Application.
    :rtype: Flask
    """
    isDevelopment = os.environ.get("FLASK_ENV") == "development"
    if isDevelopment:
        print("Application Started")

    app: Flask = Flask(__name__)

    # Start DB Connection

    # Start Controllers

    # Start Dependency Injections
    FlaskInjector(app=app, modules=[configure])

    # Start Broker Consumers

    return app
