#to make any member private use __ in starting of the variable or a method.
#example1
class Account:
    def __init__(self, acc_no, pin):
        self.acc_no = acc_no
        self.__pin = pin
    def reset_pin(self):
        print(a1.__pin)
a1 = Account(122345, "peihfiwobg")
print(a1.acc_no)
a1.reset_pin()

#example2
class Person:
    __name = "He who must not be named"
    
    def __hello(self):
        return "Hello I am Tom Riddle"
        

    def welcome(self):
        print(self.__name)
        print(self.__hello())
        
p1 = Person()

p1.welcome()


