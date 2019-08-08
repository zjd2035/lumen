import logging

from flask import Blueprint, jsonify, request
from lumen.models import db, Property


home_blueprint = Blueprint("home", __name__, url_prefix="")
logger = logging.getLogger(__name__)


@home_blueprint.route("/", methods=["GET", "POST"])
def index():
    data = request.get_json()

    if data is None:
        return jsonify({"message": "Hello there. Be on your way. Nothing to see here."})

    if "owner" in data and "address" in data:
        new_property = Property(owner=data["owner"], address=data["address"])
        db.session.add(new_property)
        db.session.commit()
        return jsonify({"message": "Property created! (I hope.)"})
    elif "owner" in data:
        found_property = Property.query.filter(Property.owner == data["owner"]).first()
        return jsonify({"message": "Hello, " + found_property.owner + " of " + found_property.address})
    elif "address" in data:
        found_property = Property.query.filter(Property.address == data["address"]).first()
        return jsonify({"message": "Hello, " + found_property.owner + " of " + found_property.address})

    return jsonify({"message": "Failed. This is what we got:", "owner": data["owner"], "address": data["address"]})
