class Car:
    def __init__(self, model, brand, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("car is starting")

    def stop(self):
        print("car is stopping")

class Bike:
    def __init__(self, model, brand, year):
        self.model = model
        self.brand = brand
        self.year = year
    
    def start_bike(self):
        print("Starting...")

    def stop_bike(self):
        print("Stopping...")

vehicles = [
        Car("Ford", "Mustang", 1970),
        Bike("Yamaha", "FZ", 2005)

        ]

for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model}  ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()
    elif isinstance(vehicle, Bike):
        print(f"Inspecting {vehicle.brand} {vehicle.model}  ({type(vehicle).__name__})")
        vehicle.start_bike()
        vehicle.stop_bike()
    else:
        raise Exception("Object is not valid")

