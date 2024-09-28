from src.common.dto.availability_dto import AvailableDateResponse, CreateAvailableDateDTO
from src.common.interfaces.AvailabilityRepositoryInterface import AvailabilityRepositoryInterface
from src.core.domain.entities.availability_entity import AvailabilityEntity
from src.core.domain.exceptions import OperationalException


class AvailabilityUsecase:
    @staticmethod
    def create(
            availability_date: CreateAvailableDateDTO,
            availability_repository: AvailabilityRepositoryInterface,
    ) -> AvailableDateResponse:
        new_date = availability_repository.create(availability_date)
        ## order_repository.create(availability_date)
        ##if not new_date.id:
         ##raise OperationalException("Error creating order")

        return AvailableDateResponse(
            doctor_id=availability_date.doctor_id,
            start_date=availability_date.start_date,
            end_date=availability_date.end_date,
            is_available=availability_date.is_available
        )
