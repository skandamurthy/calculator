class calculator():

    def __init__(self,name):
        self.name = name

    def add(self,a,b):
        return a + b

    def subtract(self,a,b):
        return a - b

    def multiply (self,a,b):
        return a * b

    def divide(self,a,b):
        if b ==0:
            print("Enter a non-divisible number")
            return 0
        else:
            return a / b

class ScientificCalculator(calculator):
    def power(self,a):
        return a * a


a=int(input("Enter First number:"))
b =int(input("Enter Second number:"))
function = input("Math Fuction:")
obj1 = ScientificCalculator("calculator1")
if function =="+":
    print(obj1.add(a,b))
elif function =='-':
    print(obj1.subtract(a,b))
elif function =='*':
    print(obj1.multiply(a,b))
elif function =='/':
    print(obj1.divide(a,b))
elif function =='power':
    print(obj1.power(a))
else:
    print("Invalid Function")


