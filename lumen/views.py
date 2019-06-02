import logging
import os

from flask import Blueprint, jsonify


home_blueprint = Blueprint("home", __name__, url_prefix="")

logger = logging.getLogger(__name__)


@home_blueprint.route("/", methods=["GET"])
def index():
    return jsonify({"message": "hello world!"})
