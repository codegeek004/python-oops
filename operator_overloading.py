#when same operator is allowed to have different characteristics according to the definition.
#functions containing __ in starting are called dunder functions.
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def show_num(self):
        print(self.real, "i +", self.img, "j")
#currently we are able to add numbers by calling this function in the main method we cannot just say num1+num2. For this we can use operator overloading using dunder function.
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)

num1 = Complex(12, 6)
num2 = Complex(14, 11)
num1.show_num()
num2.show_num()
num3 = num1 + num2
num3.show_num()
num4 = num1 - num2
num4.show_num()

