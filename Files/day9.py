
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# even_numbers = list(filter(is_even, numbers))    # flter(function,sequence)

# print("Original list:", numbers)
# print("Even numbers:", even_numbers)


# -----------------------------------------
# Example 2: Filter odd numbers
# -----------------------------------------

# def is_odd(n):
#     if n % 2 != 0:
#         return True
#     else:
#         return False

# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# odd_numbers = list(filter(is_odd, numbers))



# print("\nOdd numbers:", odd_numbers)





# Function to find square
# def square(x):
#     return x * x

# numbers = [1, 2, 3, 4, 5]

# result =set( map(square, numbers))

# print("Original list:", numbers)
# print("Squares using map:", result)


# # -----------------------------------------
# # MAP example: Convert to uppercase
# # -----------------------------------------

# def to_upper(word):
#     return word.upper()

# words = ["python", "java", "html"]

# upper_words = list(map(to_upper, words))

# print("\nOriginal words:", words)
# print("Uppercase words:", upper_words)

# # -----------------------------------------
# # 1. Lambda function to print square of a number
# # -----------------------------------------

# square = lambda x: x * x       #variable_name=lambda arg-list: expression 

# num = 5
# print("Square using lambda:", square(num))      #variable_name(arg_list)


# # -----------------------------------------
# # 2. Lambda function example (addition)
# # -----------------------------------------

# add = lambda a, b,c: a + b+c

# print("Sum using lambda:", add(10, 20,60))


# # -----------------------------------------
# # 3. Map function with lambda (square of list)
# # -----------------------------------------

# numbers = [1, 2, 3, 4, 5]

# squares = list(map(lambda x: x * x, numbers))

# print("Squares using map:", squares)



# m=[1,2,3]
# print(m*m)



# # -----------------------------------------
# # 5. Recursive function to find factorial
# # -----------------------------------------

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print("Factorial using recursion:", factorial(5))


# # -----------------------------------------
# # 6. Recursive function to check prime number
# # -----------------------------------------

# def check_prime(n, i=2):
    
#     if n <= 1:
#         return False
    
#     if i == n:
#         return True
    
#     if n % i == 0:
#         return False
    
#     return check_prime(n, i + 1)


# num = 7

# if check_prime(num):
#     print(num, "is Prime number")
# else:
#     print(num, "is Not Prime number")




# def fib(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)    
# print(fib(10))