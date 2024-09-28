from datetime import datetime

from pydantic import BaseModel


class CreateAvailableDateDTO(BaseModel):
    doctor_id: str
    start_date: datetime
    end_date: datetime
    is_available: bool

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "doctor_id": "12345",
                    "start_date": "2024-09-25T09:00:00",
                    "end_date": "2024-09-25T10:00:00",
                    "is_available": True
                }
            ]
        }
    }


class AvailableDateResponse(BaseModel):
    doctor_id: str
    start_date: datetime
    end_date: datetime
    is_available: bool
