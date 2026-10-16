# # list_comparison.py

# # ------------------------------------
# # 1. Create list using for loop
# # ------------------------------------
# list1 = []

# for i in range(1, 11):
#     list1.append(i)

# print("List created using for loop:", list1)


# # ------------------------------------
# # 2. Create same list using list comprehension
# # ------------------------------------
# list2 = [i for i in range(1, 11)]

# print("List created using list comprehension:", list2)


# # ------------------------------------
# # 3. Create another list (example)
# # ------------------------------------
# list3 = [2, 4, 6, 8, 10,12,45]
# list4 = [2, 4, 6, 8, 10]

# print("Second List:", list3)


# ------------------------------------
# 4. Find elements present in list1 but not in list3
# ------------------------------------
# difference = [x for x in list3 if x not in list4]

# print("Elements in list1 but not in list3:", difference)





# -----------------------------------
# 1. Reverse number using inbuilt function
# -----------------------------------

# num = 12345

# # Convert number to string and use slicing (inbuilt)
# reversed_num = int(str(num)[::-1])

# print("Original Number:", num)
# print("Reversed (Using Inbuilt):", reversed_num)


# # -----------------------------------
# # 2. Reverse number without using inbuilt function
# # -----------------------------------

# num2 = 123
# reverse = 0

# while num2 > 0:
#     digit = num2 % 10          # Get last digit
#     reverse = reverse * 10 + digit
#     num2 = num2 // 10          # Remove last digit

# print("Reversed (Without Inbuilt):", reverse)

# #Amstrong using while loop

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


# #Fibnocci using if elif else

# n = int(input("Enter number of terms: "))

# if n <= 0:
#     print("Please enter a positive number")

# elif n == 1:
#     print("Fibonacci series:")
#     print(0)

# else:
#     a = 0
#     b = 1
#     print("Fibonacci series:")
#     print(a, b, end=" ")

#     for i in range(2, n):
#         c = a + b
#         print(c, end=" ")
#         a = b
#         b = c


# #prime no using 2 for loop



# n = int(input("Enter the limit: "))

# print("Prime numbers up to", n, ":")

# for i in range(2, n + 1):        # Outer loop
#     count = 0
    
#     for j in range(1, i + 1):    # Inner loop
#         if i % j == 0:
#             count += 1

#     if count == 2:               # Prime numbers have exactly 2 divisors
#         print(i, end=" ")


# #Count occuernce(user input list)

# x = []

# n = int(input("Enter number of elements: "))

# for i in range(n):
#     num = int(input("Enter number: "))
#     x.append(num)

# print("List:", x)

# v = int(input("Enter number to count occurrence: "))
# c = 0

# for i in x:
#     if i == v:
#         c += 1

# print("Occurrence:", c)


# #common elelmets of two list (using set)

# l = [1, 2, 3, 4, 5]
# j = [1, 2, 3, 4, 5, 6, 7]

# s = set(l)
# d = set(j)

# k = s.intersection(d)
# m = list(k)

# print("Common Elements:", m)




