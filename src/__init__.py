"""Setup Flask Application."""
from dotenv import load_dotenv
from flask import Flask

from src.application.service.service import Service

load_dotenv()


def create_app() -> Flask:
    """Return Flask Application.

    :return: Flask Application
    :rtype: Flask
    """
    app: Flask = Flask(__name__)

    service: Service = Service()
    res = service.execute()
    print(res)

    return app
