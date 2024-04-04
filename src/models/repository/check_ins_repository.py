from src.models.settings.connection import db_connection_handler
from sqlalchemy.exc import IntegrityError, NoResultFound

class CheckInRepository:
  def insert_check_in(self, attendee_id: str):
    with db_connection_handler as database:
      try:
        check_in = (
          check_in(attendee_id)
        )
        database.session.add(check_in)
        database.session.commit()
        return attendee_id
      except IntegrityError:
        raise Exception('Check in already registered.')
      except Exception as exception:
        database.session.rollback()
        raise exception
