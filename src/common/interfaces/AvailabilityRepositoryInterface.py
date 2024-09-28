import abc

from src.core.domain.entities.availability_entity import AvailabilityEntity


class AvailabilityRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(
            self,
            availability_entity: AvailabilityEntity,
    ) -> AvailabilityEntity:
        raise NotImplementedError