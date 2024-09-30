from typing import List

from fastapi import APIRouter

from src.common.dto.availability_dto import CreateAvailableDateDTO, AvailableDateResponse, AvailableStatusDTO
from src.core.usecases.availability_usecase import AvailabilityUsecase
from src.external.database.repositories.AvailabilityRepository import AvailabilityRepository

router = APIRouter(tags=["availability"])

availability_repository = AvailabilityRepository()


@router.post("/availability", response_model=AvailableDateResponse, response_model_exclude=None)
async def create_availability(create_availability_dto: CreateAvailableDateDTO):
    return AvailabilityUsecase().create(create_availability_dto, availability_repository)


@router.put("/availability/{date_id}")
async def change_available_status(date_id:str, available_status_dto: AvailableStatusDTO):
    return AvailabilityUsecase().change_available_status(date_id,
                                                         is_available=available_status_dto.is_available,
                                                         availability_repository=availability_repository)


@router.get("/doctor/{doctor_id}", response_model=List[AvailableDateResponse], response_model_exclude=None)
async def get_available_dates(doctor_id: str):
    return AvailabilityUsecase().get_available_dates(
        doctor_id=doctor_id,
        availability_repository=availability_repository
    )
