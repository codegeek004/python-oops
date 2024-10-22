class Car:
    @staticmethod
    def start():
         print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class Honda(Car):
    def __init__(self, name):
        self.name = name

class City(Honda):
    def __init__(self, type):
        self.type = type


car1 = Honda("City")
car2 = Honda("Amaze")

print(car1.name)
car1.start()
car2.stop()
City.stop()
