#super() method is used to access the elements of the parent class
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class Honda(Car):
    def __init__(self, name, type):
        self.name = name
        #calling the __init__ method from the super class with argument type
        super().__init__(type)

    
car1 = Honda("City", "electric")
print(car1.type)
