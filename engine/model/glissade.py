from datetime import datetime
from car import EngineBase
class Glissade(EngineBase):
    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000
    def needs_service(self, threshold_years):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + threshold_years)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False

