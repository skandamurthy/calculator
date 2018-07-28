from calculator import ScientificCalculator

a = int(input("Enter First number:"))
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