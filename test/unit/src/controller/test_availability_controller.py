from unittest import TestCase
from datetime import datetime
from unittest.mock import Mock

from src.common.controller.availability import AvailabilityController
from src.common.dto.availability_dto import CreateAvailableDateDTO, AvailableDateResponse
from src.common.interfaces.AvailabilityRepositoryInterface import AvailabilityRepositoryInterface
from src.core.usecases.availability_usecase import AvailabilityUsecase


class TestAvailabilityController(TestCase):
    def setUp(self):
        self.start_date_ts = datetime.strptime("2024-09-25T10:00:00", "%Y-%m-%dT%H:%M:%S")
        self.end_date_ts = datetime.strptime("2024-09-25T11:00:00", "%Y-%m-%dT%H:%M:%S")

        self.create_available_date_dto = CreateAvailableDateDTO(
            doctor_id="123456",
            start_date=self.start_date_ts,
            end_date=self.end_date_ts,
            is_available=True
        )

        self.available_date_response = AvailableDateResponse(
            id=1,
            doctor_id=self.create_available_date_dto.doctor_id,
            start_date=self.create_available_date_dto.start_date,
            end_date=self.create_available_date_dto.end_date,
            is_available=self.create_available_date_dto.is_available
        )

        self.availability_repository = Mock(spec=AvailabilityRepositoryInterface)
        self.availability_controller = AvailabilityController(availability_repository=self.availability_repository)

    def test_create_available_date_with_success(self):
        AvailabilityUsecase.create = Mock(return_value=self.available_date_response)
        result = self.availability_controller.create_order(self.create_available_date_dto)
        AvailabilityUsecase.create.reset_mock()
        self.assertEqual(result, self.available_date_response)

    def test_get_available_dates(self):
        AvailabilityUsecase.get_available_dates = Mock(return_value=[self.available_date_response])
        result = self.availability_controller.get_available_dates(self.available_date_response.doctor_id)
        AvailabilityUsecase.get_available_dates.reset_mock()
        assert result == [self.available_date_response]

    def test_change_available_status(self):
        self.date_response_status_changed = self.available_date_response
        self.date_response_status_changed.is_available = False

        AvailabilityUsecase.change_available_status = Mock(return_value=self.date_response_status_changed)
        result = self.availability_controller.change_available_status(date_id=1, is_available=False)

        self.assertFalse(result.is_available)
