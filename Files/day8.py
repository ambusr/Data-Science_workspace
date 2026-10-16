# fn definition,fn call

# -----------------------------------------
# 1. Simple Function (No argument, No return)
# -----------------------------------------

# def hello():
#     print("Hello, Welcome to Python Functions")

# hello()
# hello()


# def sem1(a,b):
#     f=a+b
#     return f

# def sem2(c,d):
#     m=c+d
#     return m

# a=int(input("enter sem1 a:"))
# b=int(input("enter sem1 b"))
# c=int(input("enter sem2 a:"))
# d=int(input("enter sem2 b"))
# sem1_mark=sem1(a,b)
# sem2_mark=sem2(a,b)
# total=sem1_mark+sem2_mark
# print(total)

    








# # -----------------------------------------
# # 2. Function with argument, No return
# # -----------------------------------------

# def greet(name):
#     print("Hello", name)

# greet("Sona")
# greet("anu")


# # -----------------------------------------
# # 3. Function with argument and return value
# # -----------------------------------------

# def add(a, b):
#     return a + b

# result = add(10, 20)
# print("Sum:", result)






# # -----------------------------------------
# # 4. Function without argument but with return
# # -----------------------------------------

# def get_number():
#     a=int(input("enter value:"))
#     return a

# num = get_number()
# print("Returned number:", num)


# # -----------------------------------------
# # 5. Function to check Even or Odd
# # -----------------------------------------

# def check_even_odd(n):
#     if n % 2 == 0:
#         print(n, "is Even")
#     else:
#         print(n, "is Odd")
# n=int(input("enter no to check"))
#check_even_odd(n)


# n=78
# if n % 2 == 0:
#     print(n, "is Even")
# else:
#     print(n, "is Odd")


# # -----------------------------------------
# # 6. Function to find square
# # -----------------------------------------

# def square(n):
#     return n * n

# print("Square:", square(5))


# # -----------------------------------------
# # 7. Function to find factorial
# # -----------------------------------------

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i       
#     return fact

# print("Factorial:", factorial(3))


# # -----------------------------------------
# # 8. Function to check Prime number
# # -----------------------------------------

# def check_prime(n):
#     count = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             count += 1
#     if count == 2:
#         print(n, "is Prime")
#     else:
#         print(n, "is Not Prime")

# check_prime(7)
# check_prime(10)


# # -----------------------------------------
# # 9. Function to reverse a number
# # -----------------------------------------

# def reverse_number(n):    
#     rev = 0
#     while n > 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n = n // 10
#     return rev

# print("Reversed number:", reverse_number(1234))






# 1. Palindrome Number      

# Write a program to check whether a given number is a palindrome or not.

# Example:
# Input: 121
# Output: Palindrome

# def reverse_number(n):
#     rev = 0
#     while n > 0:
#         digit = n % 10
#         rev = rev * 10 + digit
#         n = n // 10
#     return rev
# n=int(input("enter no to check"))
# # print("Reversed number:", reverse_number(n))
# rev_ans=reverse_number(n)

# if n==rev_ans:
#     print("palindrome")
# else:
#     print("not palindrome")









# 2. Multiplication Table

# Write a program to print multiplication table of a given number.

# Example:
# Input: 5
# Output:
# 5 × 1 = 5
# 5 × 2 = 10
# ...
# 5 × 10 = 50

# 3. Sum of N Numbers

# Write a program to find the sum of first N natural numbers.

# Example:
# Input: 5
# Output: 15

# 4. Reverse a Number

# Write a program to reverse a given number.

# Example:
# Input: 1234
# Output: 4321

# 5. Prime Number Check

# Write a program to check whether a number is prime or not.

# Example:
# Input: 7
# Output: Prime

# 6. Fibonacci Series

# Write a program to print Fibonacci series up to N terms.

# Example:
# Input: 5
# Output: 0 1 1 2 3

# 7. Armstrong Number

# Write a program to check whether a number is Armstrong or not.

# Example:
# Input: 153
# Output: Armstrong

# 8. Factorial of a Number

# Write a program to find factorial of a number.

# Example:
# Input: 5
# Output: 120

# 9. Count Digits in a Number

# Write a program to count number of digits in a given number.

# Example:
# Input: 12345
# Output: 5

# 10. Find Largest of Two Numbers

# Write a program to find the largest of two numbers.

# Example:
# Input: 10, 20
# Output: 20 is largest







# # -----------------------------------------
# # 10. Function using default argument
# # -----------------------------------------


#defualt argument
# def country(name="India"):
#     print("Country:", name)

# country()
# country("USA")



# def shop(product,cost=0):
#     print("product",product)
#     print("cost:",cost)
# shop("flour",200)
# shop("curd")
# shop('milk')


#positional argument

# def attach(s1,s2):
#     s3=s1+s2
#     print(s3)
# attach("com","puter")

#keyword argument

# def attach(s1,s2):
#     s3=s1+s2
#     print(s3)
# attach(s1="com",s2="puter")
# attach(s2="ble",s1="ta")



#variable lenth argument

# def add(*a):
#     sum=0
#     for i in a:
#         sum=sum+i
#     print(sum)
# add(1,2,3,4,5)
# add(3,4)



# # -----------------------------------------
# # 11. Function using keyword argument
# # -----------------------------------------

# def student(name, age):
#     print("Name:", name)
#     print("Age:", age)

# student(age=20, name="Anu")




# # -----------------------------------------
# # 12. Function to find maximum of two numbers
# # -----------------------------------------

# def find_max(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# print("Maximum:", find_max(10, 25))





