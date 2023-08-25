from tire.tire import Tire 



class CarriganeTire(Tire):
	def __init__(self,tire_values):
		self.tire_values=tire_values
	def needs_service(self):
		for tire in self.tire_values:
			if tire>=0.9:
				return True 
		return False