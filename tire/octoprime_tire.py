from tire.tire import Tire 

class OctoprimeTire(Tire):
	def __init__(self,tire_values):

		self.tire_values=tire_values
		
	def needs_service(self):
		return sum(self.tire_values)>=3