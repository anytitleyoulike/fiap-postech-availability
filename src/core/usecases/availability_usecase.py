from src.common.dto.availability_dto import AvailableDateResponse, CreateAvailableDateDTO
from src.common.interfaces.AvailabilityRepositoryInterface import AvailabilityRepositoryInterface
from src.core.domain.entities.availability_entity import AvailabilityEntity
from src.core.domain.exceptions import OperationalException, NotFoundError


class AvailabilityUsecase:
    @staticmethod
    def create(
            availability_date: CreateAvailableDateDTO,
            availability_repository: AvailabilityRepositoryInterface,
    ) -> AvailableDateResponse:
        new_date = availability_repository.create(availability_date)
        if not new_date:
            raise OperationalException("Error creating order")

        return AvailableDateResponse(
            id=new_date.id,
            doctor_id=new_date.doctor_id,
            start_date=new_date.start_date,
            end_date=new_date.end_date,
            is_available=new_date.is_available
        )

    @staticmethod
    def get_available_dates(doctor_id: str, availability_repository: AvailabilityRepositoryInterface):
        available_dates = availability_repository.get_available_dates(doctor_id)

        if not available_dates:
            raise NotFoundError(f"No available dates for {doctor_id}")

        return available_dates

    @staticmethod
    def change_available_status(date_id: int, is_available: bool, availability_repository: AvailabilityRepositoryInterface):
        return availability_repository.change_available_status(date_id=date_id, is_available=is_available)
