from src.common.dto.availability_dto import CreateAvailableDateDTO, AvailableDateResponse
from src.common.interfaces import AvailabilityRepositoryInterface
from src.core.usecases.availability_usecase import AvailabilityUsecase


class AvailabilityController:
    def __init__(
            self,
            availability_repository: AvailabilityRepositoryInterface,
    ) -> None:
        self.availability_repository = availability_repository

    def create_order(self, availability_date_dto: CreateAvailableDateDTO) -> AvailableDateResponse:
        return AvailabilityUsecase.create(
            availability_date=availability_date_dto,
            availability_repository=self.availability_repository,
        )
