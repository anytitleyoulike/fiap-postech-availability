from pydantic import BaseModel
from sqlalchemy import Integer, String, DateTime, Boolean, Column


class Availability(BaseModel):
    __tablename__ = "availabilities"
    id = Column(Integer, primary_key=True, index=True)
    doctor_id = Column(String, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    is_available = Column(Boolean)