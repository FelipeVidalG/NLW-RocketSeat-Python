from src.models.settings.base import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from sqlalchemy.sql import func

class CheckIns(Base):
  __tablename__ = "check_ins"

  id = Column(Integer, primary_key=True)
  attendeeId = Column(String, ForeignKey("attendees.id"))
  created_at = Column(DateTime, default=func.now())

  def __repr__(self):
    return f"CheckIns [attendeeId={self.attendeeId}]"

