class Student:
    #default constructor
    def __init__(self):
        print("default constructor initiated")
    college = 'vit'
    #parameterized constructor
    def __init__(self, fullname, marks):
        #we can also name self to any other name but we should necessarily have it because it is the reference to the object 
        self.name = fullname
        self.marks = marks
#python automatically creates an __init__() function which is called constructor
s1 = Student("yash", 13)
s2 = Student("ajay",14)
s3 = Student("gurpreet",15)
print(s1.name, s1.marks,s1.college)
print(s2.name, s2.marks, s2.college)
print(s3.name, s3.marks, s3.college)
print(Student.college)
