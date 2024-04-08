from flask import Blueprint, jsonify
event_route = Blueprint("event_route", __name__)

@event_route.route("/events", methods=["POST"])
def create_event():
    return jsonify({"ola": "mundo"}), 200
