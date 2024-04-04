from .attendees_repository import AttendeesRepository
from src.models.settings.connection import db_connection_handler
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="New register in database")
def test_insert_attendee():
  event_id = "meu-uuid"
  attendees_info = {
    "uuid": "meu_uuid_atteendee",
    "name": "attendee name",
    "email": "email@emai.com.br",
    "event_id": event_id,
  }

  attendees_repository = AttendeesRepository()
  response = attendees_repository.insert_attendee(attendees_info)
  print(response)

@pytest.mark.skip(reason="It is not necessary")
def test_get_attendee_badge_by_id():
  attendee_id = "meu_uuid_atteendee"
  attendees_repository = AttendeesRepository()
  attendee = attendees_repository.get_attendee_badge_by_id(attendee_id)
  print(attendee)


