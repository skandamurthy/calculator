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





