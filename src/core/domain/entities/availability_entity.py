from datetime import datetime
from typing import Union

from pydantic import BaseModel, ConfigDict


class AvailabilityEntity(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Union[int, None] = None
    start_date: datetime
    end_date: datetime
    is_available: bool
    doctor_id: str
