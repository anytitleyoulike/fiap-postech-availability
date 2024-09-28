from typing import List

from fastapi import APIRouter

from src.common.dto.availability_dto import CreateAvailableDateDTO, AvailableDateResponse
from src.core.usecases.availability_usecase import AvailabilityUsecase
from src.external.database.repositories.AvailabilityRepository import AvailabilityRepository

router = APIRouter(tags=["availability"])

availability_repository = AvailabilityRepository()


@router.post("/", response_model=AvailableDateResponse, response_model_exclude=None)
async def create_availability(create_availability_dto: CreateAvailableDateDTO):
    return AvailabilityUsecase().create(create_availability_dto, availability_repository)
