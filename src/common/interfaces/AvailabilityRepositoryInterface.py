import abc
from typing import List

from src.core.domain.entities.availability_entity import AvailabilityEntity


class AvailabilityRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(
            self,
            availability_entity: AvailabilityEntity,
    ) -> AvailabilityEntity:
        raise NotImplementedError

    @abc.abstractmethod
    def get_available_dates(self, doctor_id: str) -> List[AvailabilityEntity]:
        raise NotImplementedError

    @abc.abstractmethod
    def change_available_status(self, date_id: int, is_available: bool):
        raise NotImplementedError
