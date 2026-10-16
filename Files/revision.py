"""BASIC LEVEL (1–15)"""

# 1. Print Hello World
# print("Hello World")


# #2. Add two numbers
# a, b = 10, 20
# print(a + b)


# #3. Swap two numbers
# a, b = 5, 10
# a, b = b, a
# print(a, b)


# 4. Check even or odd
# n = int(input())
# print("Even" if n % 2 == 0 else "Odd")


# 5. Find largest of three numbers
# a, b, c = 10, 25, 15
# print(max(a, b, c))


# 6. Factorial using loop
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)


# 7. Multiplication table
# n = 5
# for i in range(1, 11):
#     print(n*i)


# 8. Sum of first N numbers
# n = 10
# print(n*(n+1)//2)



# 9. Reverse number
# n = 123
# rev = 0
# while n:
#     rev = rev*10 + n%10
#     n//=10
# print(rev)
# 10. Count digits
# n = 12345
# print(len(str(n)))



# 11. Check positive, negative or zero
# n = -5
# if n > 0:
#     print("Positive")
# elif n < 0:
#     print("Negative")
# else:
#     print("Zero")


# 12. Print numbers 1 to N
# n = 5
# for i in range(1, n+1):
#     print(i)

# 13. Print even numbers 1 to 50
# for i in range(2, 51, 2):
#     print(i)

# 14. Sum of digits
# n = 123
# s = 0
# while n:
#     s += n%10
#     n//=10
# print(s)

# 15. Check palindrome number
# n = 121
# print("Palindrome" if str(n)==str(n)[::-1] else "Not Palindrome")

"""-----------------------------------------day2----------------------------"""

# 🔹 STRING PROGRAMS (16–25)

# 16. Reverse string

# s = "python"
# print(s[::-1])

# 17. Check palindrome string
# s = "madam"
# print("Palindrome" if s==s[::-1] else "Not")

# 18. Count vowels
# count=0
# s = "hello"
# for ch in s:
#     if ch in "aeiou":
#         count=count+1
# print(count)

# 19. Count consonants

# count=0
# s = "hello12"
# for ch in s:
#     if ch.isalpha():

#         if ch not in "aeiou":
#             count=count+1
# print(count)

# 20. Count words
# s = "I love python"
# print(len(s.split()))

# 21. Convert uppercase to lowercase
# s = "HELLO"
# print(s.lower())

# 22. Remove spaces
# s = "hello world"
# print(s.replace(" ", ""))

# 23. Find string length without len()
# s = "python"
# count = 0
# for i in s:
#     count += 1
# print(count)

# 24. Count character frequency
# s = "hello"
# d = {}
# for ch in s:
#     d[ch] = d.get(ch,0)+1
# print(d)

# 25. Check anagram
# s1 = "listen"
# s2 = "silent"
# print(sorted(s1)==sorted(s2))

# 🔹 LIST PROGRAMS (26–35)

# 26. Find largest element
# lst = [4,7,1,9]
# print(max(lst))

# 27. Find smallest element
# print(min(lst))

# 28. Sum of list
# print(sum(lst))

# 29. Remove duplicates
# lst = [1,2,2,3]
# print(list(set(lst)))

# 30. Reverse list
# lst.reverse()
# print(lst)


# 31. Sort list
# lst.sort()
# print(lst)
# 32. Second largest element
# lst = [10,20,30,40]
# lst.sort()
# print(lst[-2])

# 33. Merge two lists
# a = [1,2]
# b = [3,4]
# print(a+b)

# 34. Find even numbers in list
# lst = [1,2,3,4]
# print([x for x in lst if x%2==0])

# 35. Count occurrence
# lst = [1,2,2,3]
# print(lst.count(2))

"""-----------------------------------------day2----------------------------"""

"""-----------------------------------------day3----------------------------"""

# 🔹 FUNCTION PROGRAMS (36–42)
# 36. Function to add numbers
# def add(a,b):
#     return a+b
# print(add(5,3))

# 37. Function factorial
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# 38. Function palindrome
# def is_pal(s):
#     return s==s[::-1]
# print(is_pal("madam"))

# 39. Function to find max
# def maximum(lst):
#     return max(lst)
# print(maximum([1,5,3]))

# 40. Function sum of list
# def sum_list(lst):
#     return sum(lst)
# print(sum_list([1,2,3]))

# 41. Function prime check
# def prime(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return True
# print(prime(7))

# 42. Fibonacci function
# def fib(n):
#     a,b=0,1
#     for i in range(n):
#         print(a)
#         a,b=b,a+b
# fib(5)

# 🔹 INTERVIEW LEVEL PROGRAMS (43–50)
# 43. Prime number
# def check_prime(n, i=2):
    
#     if n <= 1:
#         return False
    
#     if i == n:
#         return True
    
#     if n % i == 0:
#         return False
    
#     return check_prime(n, i + 1)


# 44. Fibonacci series using recursion 
# def fib(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)    
# print(fib(10))

# 45. Armstrong number
# num = int(input("Enter a number: "))

# temp = num
# digits = len(str(num))
# sum = 0

# while temp > 0:
#     digit = temp % 10
#     sum += digit ** digits
#     temp = temp // 10

# if sum == num:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")


# 47. Find missing number
# lst=[1,2,4,5]
# n=5
# print(sum(range(1,n+1))-sum(lst))

# 48. Count even and odd
# numbers = [10, 15, 20, 25, 30, 33, 40]

# even_count = 0
# odd_count = 0

# for num in numbers:
#     if num % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1

# print("Even count:", even_count)
# print("Odd count:", odd_count)

# 49. Find duplicate elements
# numbers = [10, 20, 30, 20, 40, 10, 50]

# duplicates = []

# for num in numbers:
#     if numbers.count(num) > 1 and num not in duplicates:
#         duplicates.append(num)

# print("Duplicate elements:", duplicates)

# 50. Find largest using loop
# lst=[3,7,2,9]
# maxi=lst[0]
# for i in lst:
#     if i>maxi:
#         maxi=i
# print(maxi)