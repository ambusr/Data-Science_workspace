# 1.Write a Python program to print numbers from 1 to 10.
print("Numbers from 1 to 10:", end=' ')
for i in range(1, 11):
    print(i, end=' ')
print()

# 2.print numbers from 10 to 1.
print("Numbers from 10 to 1:", end=' ')
for i in range(10, 0, -1):
    
    print(i, end=' ')
print()

# 3.Print all even numbers from 1 to 20.
print("Even numbers from 1 to 20:", end=' ')
for i in range(2, 21, 2):
    print(i, end=' ')
print()
# or
print("Even numbers from 1 to 20,Method2:", end=' ')
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=' ')
print()

# 4.Print all odd numbers from 1 to 20.
print("Odd numbers from 1 to 20:", end=' ')
for i in range(1, 21):
    if i % 2 != 0:
        print(i, end=' ')
print()

# 5.Print the multiplication table of a number entered by the user.
num = int(input("Enter a number to get multiplication table: "))
for i in range(1, 11):
    print(i, "x", num, "=", i * num)


# 6.Find the sum of numbers from 1 to 100.
sum = 0
for i in range(1, 101):
    sum += i
print("Sum of numbers from 1 to 100:", sum)

# 7.Find the sum of even numbers from 1 to 50.
sum = 0
for i in range(1,51):
    if i % 2 == 0: 
     sum += i
print("Sum of even numbers from 1 to 50:", sum)

# 8.find the factorial of a given number.
num = int(input("Enter a number to find factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("Factorial of", num, "is", factorial)

# 9.Count how many numbers between 1 and 100 are divisible by 5.
count = 0
for i in range(1, 101):
    if i % 5 == 0:
        count += 1
print("Count of numbers between 1 and 100 divisible by 5:", count)

# 10.Print the squares of numbers from 1 to 10.
print("Squares of numbers from 1 to 10:")
for i in range(1, 11):
    print(i, "* ", i, "=", i ** 2)