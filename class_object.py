class Student:
    def __init__(self, fullname):
        #we can also name self to any other name but we should necessarily have it because it is the reference object
        print(self)
        self.name = fullname
#python automatically creates an __init__() function which is called constructor
s1 = Student("yash")
s2 = Student("ajay")
s3 = Student("gurpreet")
print(s1.name, s2.name, s3.name)
