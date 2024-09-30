from typing import List

from src.common.interfaces.AvailabilityRepositoryInterface import AvailabilityRepositoryInterface
from src.core.domain.entities.availability_entity import AvailabilityEntity
from src.core.domain.exceptions import OperationalException, NotFoundError
from src.external.database.models.availiability_model import AvailabilityModel
from src.external.database.sqlalchemy.mappers import AvailabilityMapper
from src.external.database.sqlalchemy.mappers.AvailabilityMapper import AvailabilityMapper
from src.external.database.sqlalchemy.session_mixin import use_database_session


class AvailabilityRepository(AvailabilityRepositoryInterface):

    def change_available_status(self, date_id: int, is_available: bool):
        try:
            with use_database_session() as session:
                date = session.query(AvailabilityModel).filter_by(id=date_id, doctor_id="12345").first()

                if not date:
                    raise NotFoundError("Date not found")
                date.is_available = is_available
                session.commit()

                return AvailabilityMapper.model_to_entity(date)
        except Exception as error:
            raise error

    def create(self, availability_entity: AvailabilityEntity) -> AvailabilityEntity:
        try:
            with use_database_session() as session:
                model = AvailabilityMapper.entity_to_model(availability_entity)
                session.add(model)
                session.commit()

            return AvailabilityMapper.model_to_entity(model)
        except Exception as error:
            raise error

    def get_available_dates(self, doctor_id: str) -> List[AvailabilityEntity]:
        try:
            with use_database_session() as session:
                dates = session.query(AvailabilityModel).filter_by(doctor_id=doctor_id, is_available=True)
                return [AvailabilityMapper.model_to_entity(date) for date in dates]
        except Exception as error:
            raise error
