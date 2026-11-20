# factorial of a given number
num=int(input("Enter a numberto find factorial of: "))
while num<0:
    print("Sorry, factorial does not exist for negative numbers")
    num=int(input("Enter a positive number: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print("Factorial of",num,"is",fact)


#Program to find the cube root of a perfect cube
num=int(input("Enter a number: "))
cube=0
while cube**3<abs(num):
    cube+=1

if cube**3!=abs(num):
    print(num,"is not a perfect cube")
else:
    if (num<0):
        cube=-cube
    print(num,"is a perfect cube and its cube root is",cube)





