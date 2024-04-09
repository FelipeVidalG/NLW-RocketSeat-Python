from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendees_handler import AttendeesHandler

attendees_route = Blueprint("attendees_route", __name__)

@attendees_route.route("/events/<event_id>/register", methods=["POST"])
def create_attendees(event_id):
  attendees_handler = AttendeesHandler()
  http_request = HttpRequest(param={"event_id": event_id}, body=request.json)

  http_response = attendees_handler.registry(http_request)
  return jsonify(http_response.body), http_response.status_code

@attendees_route.route("/attendees/<attendee_id>/badge", methods=["GET"])
def get_attendees(attendee_id):
  attendees_handler = AttendeesHandler()
  http_request = HttpRequest(param={"attendee_id": attendee_id}, body=request.json)

  http_response = attendees_handler.find_attendee_badge(http_request)
  return jsonify(http_response.body), http_response.status_code
