class Vehicle:
	def __init__(self, brand, model, year):
		self.brand = brand
		self.model = model
		self.year = year

	def start(self):
		print('Vehicle is starting')
	def	stop(self):
		print('Vehicle is stopping')
class Car(Vehicle):
	def __init__(self, brand, model, year, number_of_doors, number_of_wheels):
		super().__init__(brand, model, year)
		self.number_of_doors = number_of_doors
		self.number_of_wheels = number_of_wheels

class Bike(Vehicle):
	def __init__(self, brand, model, year, number_of_wheels):
		super().__init__(brand, model, year)
		self.number_of_wheels = number_of_wheels

car = Car("BMW", "M340i", 2025, 3, 5)
bike = Bike("Triumph", "Speed 400", 2025, 2)
car.start()
car.stop()
bike.start()
bike.stop()
print(car.__dict__)
