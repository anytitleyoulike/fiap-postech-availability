from pydantic import BaseModel
from sqlalchemy import Integer, String, DateTime, Boolean, Column

from src.external.database.sqlalchemy.orm import Base


class AvailabilityModel(Base):
    __tablename__ = "availabilities"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    doctor_id = Column(String, index=True, nullable=False)
    start_date = Column(DateTime, unique=True, nullable=False)
    end_date = Column(DateTime, unique=True, nullable=False)
    is_available = Column(Boolean, nullable=False)
