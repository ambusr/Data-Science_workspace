import math
import random
import calendar
import mymodule

print("Write a program using the math module to find the square root.")
sqr1=float(input ("enter a number"))
print("square root of ",sqr1," is ",math.sqrt(sqr1))
print()


print("Write a program using the random module to generate a random number.")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
ran=random.randint(a,b)
print(f"random number between {a} and {b} is {ran}")
print()

print("Write a program using the calendar module to display a calendar.")
month=int(input("enter a month 1 -12"))
year=int(input("enter year in YYYY format"))
print(calendar.month(year,month))
print()

print("Create a user-defined module and import it into another program.:")
a=int(input ("enter 1st number"))
b=int(input ("enter 2nd number"))
print(f"additin of {a},{b} using user module. Sum of {a},{b} is  {mymodule.add(a,b)}")
print(f"Subtraction of {a},{b} using user module. difference of {a},{b} is  {mymodule.sub(a,b)}")
print()

print("Handle division by zero using try-except.")
print("Use finally in a Python program.")
a=int(input ("enter 1st number"))
b=int(input ("enter 2nd number"))
try:
    div=float(a/b)
    print(f"{a} divided by {b} is {div}")
except ZeroDivisionError:
    print("Zero division error detected")
finally:
    print("wrote in finally")
print()
    

print("Handle invalid input using exception handling.")
try:
    a=int(input("enter only integer"))
    print("no exceptions detected, intiger entered is",a)
except ValueError:
    print("you entered an invalid intiger ")
print()


print("Raise an exception when a number is negative.")

try:
    a=int(input("enter a number: "))
    if (a<0):
        raise ValueError
    else:
        print("No exceptions detected, number entered is ",a)
except ValueError:
    print ("You entered a negative number")
print()

print("Handle multiple exceptions in one program.")

try:
    a=int(input("enter first intiger"))
    b=int(input("enter 2nd digit(non zero)"))
    c=float(a/b)
    print(f"No Exceptions occured.{a}/{b} is {c}")
except ValueError:
    print("error:Not an intiger")
except ZeroDivisionError:
    print("Error: zero division")
print()

# Write a program to handle invalid integer input.