from typing import List

from fastapi import APIRouter

from src.common.controller.availability import AvailabilityController
from src.common.dto.availability_dto import CreateAvailableDateDTO, AvailableDateResponse, AvailableStatusDTO
from src.core.usecases.availability_usecase import AvailabilityUsecase
from src.external.database.repositories.AvailabilityRepository import AvailabilityRepository

router = APIRouter(tags=["availability"])

availability_repository = AvailabilityRepository()
availability_controller = AvailabilityController(availability_repository)


@router.post("/availability", response_model=AvailableDateResponse, response_model_exclude=None)
async def create_availability(create_availability_dto: CreateAvailableDateDTO):
    return availability_controller.create_order(create_availability_dto)


@router.put("/availability/{date_id}")
async def change_available_status(date_id: int, available_status_dto: AvailableStatusDTO):
    return availability_controller.change_available_status(date_id,
                                                           is_available=available_status_dto.is_available)


@router.get("/doctor/{doctor_id}", response_model=List[AvailableDateResponse], response_model_exclude=None)
async def get_available_dates(doctor_id: str):
    return availability_controller.get_available_dates(
        doctor_id=doctor_id,
    )
