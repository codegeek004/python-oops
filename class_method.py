#method cannot change the class member so we need the class method for this
class Person:
    name = "Yash"
    def ChangeName(self, name):
        Person.name = name
        #another approach
        #self.__class__.name = "Ajay"
    #another way
    @classmethod
    #here cls is not self, it is referring to the class
    def changeName(cls, name):
        cls.name = name
p1 = Person()
p1.ChangeName("Ajay")
print(Person.name)
print(p1.name)
