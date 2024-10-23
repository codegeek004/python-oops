class Student:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math
            
    @property
    def percentage(self):
        return str((self.phy + self.che + self.math)/3) + "%"

        #percentage
s1 = Student(14, 56, 45)
print(s1.percentage)
s1.phy = 66
print(s1.percentage)

#now suppose you have entered marks for phy wrong and want to change. You can change the value in the variable but the overall percentage will not change.
#s1.phy = 66
#print(s1.phy)
#print(s1.percentage)
#for this reason we use property decorator. 
#one approach for this is we can create a function calculatePercentage and call this function in the main method. This will be perfectly alright but property decorator is much easier to implement
#this property decorator will return the latest changes to the object.
