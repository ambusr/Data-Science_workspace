# #filter odd number from a tuple using filter function
# def odd(x):
#     if x % 2 != 0:
#         return True
#     else:
#         return False
# t=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# n=tuple(filter(odd,t))
# print("given tuple : ",t)
# print("filtered tuple is: ",n)


# # filter numbers greater than 10  
# l=[1,10,5,8,25,30,15,100]
# def greaterthan_10(x):
#     if x>10:
#         return True
#     else:
#         return False

# n=list(filter(greaterthan_10,l))
# print("given list : ",l)
# print("filtered list is: ",n)


######### Excercise ##########



# 1. filter number divisible by 5
l=[1,10,5,8,25,30,15,100]
def divisible_by_5(x):
    if x%5==0:
        return True
    else:
        return False

n=list(filter(divisible_by_5,l))
print("given list : ",l)
print("divisible by 5 filtered list is: ",n)


# 2.filter vowels from a string without lambda function

vowels="aeiou"
def fn_vowels(x):
    if x.lower() in vowels:
        return True
    else:
        return False
str=input("Enter a string: ")   
fil=list(filter(fn_vowels,str))
print("filtered vowels: ",fil)

# filter strings with length greater than 5
l=["apple","ball","cherry","dog","elephant"]
def fn_length(x):
    if len(x)>5:
        return True
    else:
        return False
fil=list(filter(fn_length,l))
print("filtered strings: ",fil)

# filter names starting with 'A' 
l=["Alice","Bob","Charlie","David","Eve"]
def fn_startswith_A(x):
    if x.startswith("A"):
        return True
    else:
        return False
fil=list(filter(fn_startswith_A,l))
print("filtered names: ",fil)

# filter negative numbers
nums=[-10, 5, -3, 8, -1, 0, 7]
def fn_negative(x):
    if x < 0:
        return True
    else:
        return False
fil=list(filter(fn_negative,nums))
print("filtered negative numbers: ",fil)

# filter positive numbers
def fn_positive(x):
    if x > 0:
        return True
    else:
        return False
fil=list(filter(fn_positive,nums))
print("filtered positive numbers: ",fil)

# filter numbers less than 50
def fn_less_than_50(x):
    if x < 50:
        return True
    else:
        return False
fil=list(filter(fn_less_than_50,nums))
print("filtered numbers less than 50: ",fil)


