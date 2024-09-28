from src.core.domain.entities import availability_entity
from src.core.domain.entities.availability_entity import AvailabilityEntity
from src.external.database.models.availiability_model import AvailabilityModel


class AvailabilityMapper:
    @staticmethod
    def entity_to_model(entity: AvailabilityEntity):
        return AvailabilityModel(
            doctor_id=entity.doctor_id,
            start_date=entity.start_date,
            end_date=entity.end_date,
            is_available=entity.is_available
        )

    @staticmethod
    def model_to_entity(model: AvailabilityModel):
        return AvailabilityEntity(
            id=model.id,
            doctor_id=model.doctor_id,
            start_date=model.start_date,
            end_date=model.end_date,
            is_available=model.is_available
        )