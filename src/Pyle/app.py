from flask import Flask

from src.Pyle.config import (
    DevConfig,
    TestConfig,
    ProdConfig
    )
from src.Pyle.views import app_view

def create_app(config_set=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_set)

    app.register_blueprint(app_view)

    return app