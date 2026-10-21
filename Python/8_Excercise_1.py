# # 1.find the largest number in a list using a for loop. 

# a=int(input("Enter the number of elements in the list: "))
# L=[]
# for i in range(a):
#     b=int(input("Enter the element: "))
#     L.append(b)
# largest=L[0]
# for i in L:
#     if i>largest:
#         largest=i
# print("Largest number is:",largest)

# # 2.Find the smallest number in a list.
# smallest=L[0]
# for i in L:
#     if i<smallest:
#         smallest=i
# print("Smallest number is:",smallest)

# # 3.Count the number of positive and negative numbers in a list.

# positive=0
# negative=0
# for i in L:
#     if i>0:
#         positive+=1
#     elif i<0:
#         negative+=1
# print("Total positive numbers is:",positive)
# print("Total negative numbers is:",negative)

# # 4.Count how many times a particular number occurs in a list.
# num=int(input("Enter the number to count: "))
# count=0
# for i in L:
#     if i==num:
#         count+=1
# print("Count of",num,"in list is",count)

# # 5.Reverse a string using a for loop.

# strg = input("Enter a string: ")
# rev = ""
# length=len(strg)
# for k in range(length-1, -1, -1):
#     rev += strg[k]

# print("Reversed string:", rev)
############################################
# # 6.Count the number of vowels in a string.
# vowels = "aeiou"
# vow_count = 0
# for char in strg.lower():
#     if char in vowels:
#         vow_count += 1
# print("Number of vowels:", vow_count)
########################################
# # 7.Find the sum of digits of a number.

# num = int(input("Enter a number: "))
# sum_digits = 0
# while num > 0:
#     digit = num % 10
#     sum_digits += digit
#     num = num // 10
# print("Sum of digits:", sum_digits)

# # 8.Check whether a number is prime.
# num = int(input("Enter a number to check fdor prime: "))
# if num < 2:
#     print(num, "is not a prime number")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")


# # 10.Print the following pattern: *,**,***,****,*****
# line = int(input("Enter the number of lines: "))
# for i in range(1, line + 1):
#     print("KANNAN " * i)

