"""Setup Flask Application."""
from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def create_app() -> Flask:
    """Return Flask Application.

    :return: Flask Application
    :rtype: Flask
    """
    app = Flask(__name__)

    return app
