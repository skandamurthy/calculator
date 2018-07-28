class calculator():

    def __init__(self,name):
        self.name = name

    def add(self,a,b):
        return (a+b)

    def subtract(self,a,b):
        return (a-b)

    def multiply (self,a,b):
        return (a*b)

    def divide(self,a,b):
        if b ==0:
            print("Enter a non-divisible number")
            return 0
        else:
            return(a/b)


a=int(input("Enter First number:"))
b =int(input("Enter Second number:"))
obj1 = calculator("calculator1")
print(obj1.add(a,b))
print(obj1.subtract(a,b))
print(obj1.multiply(a,b))
print(obj1.divide(a,b))



