from src.common.interfaces.AvailabilityRepositoryInterface import AvailabilityRepositoryInterface
from src.core.domain.entities.availability_entity import AvailabilityEntity
from src.external.database.sqlalchemy.session_mixin import use_database_session


class AvailabilityRepository(AvailabilityRepositoryInterface):
    def create(self, availability_entity: AvailabilityEntity) -> AvailabilityEntity:
        return availability_entity
