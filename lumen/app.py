import os
from typing import List

from flask import Blueprint, Flask, jsonify

from lumen.views import home_blueprint


DEFAULT_BLUEPRINTS = [home_blueprint]

def create_app() -> Flask:
    app = Flask(__name__)

    if "FLASK_CONFIG" in os.environ:
        app.config.from_object(os.environ['FLASK_CONFIG'])
    else:
        app.config.from_object('lumen.settings.LocalConfig')

    # configure application
    configure_blueprints(app, DEFAULT_BLUEPRINTS)

    return app

def configure_blueprints(app: Flask, blueprints: List[Blueprint]) -> None:
    for blueprint in blueprints:
        app.register_blueprint(blueprint)
