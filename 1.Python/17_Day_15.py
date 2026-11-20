
#OVERLOADING OPERATORS
class Number:
    def __init__(self, value):
        self.value = value

    def __mul__(self, other):
        return self.value * other.value, "multiplication overload"
        

    def __add__(self, other):
        return self.value + other.value, "addition overload"
    def __sub__(self, other):
        return self.value - other.value, "subtraction overload"
    def __truediv__(self, other):
        return self.value / other.value, "division overload"
    def __eq__(self, other):
        return self.value == other.value, "equal overload"
        
    

n1 = Number(int(input("Enter the first number: ")))
n2 = Number(int(input("Enter the second number: ")))
opt=input("Enter the operation you want to perform: +,-,*,/,= and E to exit")

if opt == "*":
        print(n1 * n2)
elif opt == "+":
        print(n1 + n2)
elif opt == "-":
        print(n1 - n2)
elif opt == "/":
         print(n1 / n2)
elif opt == "=":
        print(n1 == n2)
else:
        print("Invalid operator")