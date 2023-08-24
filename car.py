from abc import ABC, abstractmethod
from datetime import datetime

class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self, threshold_years):
        pass

class EngineBase(Car):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    @abstractmethod
    def engine_should_be_serviced(self):
        pass

    def needs_service(self, threshold_years):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + threshold_years)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False


