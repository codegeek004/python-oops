class Student:
    def __init__(self, age):
        self.age = age
        print("default constructor initiated")

    def hello(self):
        print(f"hello {username}, your age is {self.age}")
    
    def get_age(self):
        return self.age

username = str(input("Enter the username: "))
s1 = Student(12)
s1.hello()
print(s1.get_age())
