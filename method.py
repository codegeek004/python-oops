class Student:
    def __init__(self):
        print("default constructor initiated")

    def hello(self):
        print(f"hello {username}")

username = str(input("Enter the username: "))
s1 = Student()
s1.hello()
