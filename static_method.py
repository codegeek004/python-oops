class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @staticmethod 
    def hello():
        print("hello")

s1 = Student("yash", 123)
s1.hello()


