from datetime import datetime
from car import EngineBase
#from engine.sternman_engine import SternmanEngine


class Palindrome(EngineBase):
    def engine_should_be_serviced(self):
        return self.warning_light_is_on
    def needs_service(self, threshold_years):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + threshold_years)
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
