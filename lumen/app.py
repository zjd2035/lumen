import os
import sys
import logging
from typing import List

from flask import Blueprint, Flask, jsonify

from lumen.views import home_blueprint

DEFAULT_BLUEPRINTS = [home_blueprint]

logger = logging.getLogger()


def create_app() -> Flask:
    app = Flask(__name__)

    if "FLASK_CONFIG" in os.environ:
        app.config.from_object(os.environ["FLASK_CONFIG"])
    else:
        # default to LocalConfig
        app.config.from_object("lumen.settings.LocalConfig")

    logger.info("Creating the application")

    # configure application
    configure_logging()
    configure_blueprints(app, DEFAULT_BLUEPRINTS)
    configure_error_handlers(app)

    return app


def configure_logging() -> None:
    """
    Configures the python standard logger
    """

    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    werkzeug_logger = logging.getLogger("werkzeug")
    werkzeug_logger.setLevel(logging.ERROR)


def configure_blueprints(app: Flask, blueprints: List[Blueprint]) -> None:
    """
    Each of the provided blueprints will be registed to the application instance
    Without this, the routes defined on the blueprints will not be accessible to the application
    """
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_error_handlers(app: Flask):
    @app.errorhandler(Exception)
    def handle_base_exceptions(e):
        """
        When instances of BaseException are raised during a request lifecycle, the flask application
        will use this function as a handler. This allows us to consolidate error handling, and
        prevent raw exceptions from being returned to the client.
        """

        logger.error(f"An instance of Base Exception was raised: {e}")
        return jsonify({"message": "There was an error", "error": str(e)})
