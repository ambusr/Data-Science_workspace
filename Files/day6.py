# ==================================================
# PYTHON CONTROL STATEMENTS
# File Name: control_statements.py
# ==================================================


# print(6)
# print(7)

# # 1. IF STATEMENT
# # --------------------------------------------------
# x = 4

# if x > 5:        
#     print("x is greater than 5")


# n=1
# if n==1:
#     print("yes")
#     print("uidyuifuiduidf")

# print("\n-----------------------------\n")

# # 2. IF-ELSE
# # --------------------------------------------------
# age = 17

# if age >= 18:
#     print("Eligible to vote")
# else:
#     print("Not eligible to vote")

# a=int(input("enter a no"))
# if a%2==1:                    
#     print("odd number")
# else:
#     print("even number")

# print("\n-----------------------------\n")

# # 3. IF-ELIF-ELSE
# # --------------------------------------------------
# a=int(input("enter a no"))
# if a>0:
#     print("+ve no")
# elif a<0:
#     print("-ve no")
# else:
#     print("the given no 0")



# marks = 75

# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")

# else:
#     print("Fail")


# print("\n-----------------------------\n")

# # 4. NESTED IF
# # --------------------------------------------------
# num = 1

# if num > 0:
#     if num % 2 == 0:
#         print("Positive Even Number")
#     else:
#         print("Positive Odd Number")
# else:
#     print("u entered -ve no")

# print("\n-----------------------------\n")

# # 5. FOR LOOP
# # --------------------------------------------------
# print("For Loop Example")

# for i in range(1, 6):     
#     print(i)


# s="python"
# for p in s:     
#     print(p)

# s="python"
# n=len(s)

# for i in range(n):  
   
#     print(s[i])   


# for i in range (10,4,-2):
#     print(i)

# n=7
# for i in range(1,11):    
#     print(n,'*',i,"=",n*i)


# l=(1,2,3,4,5)
# sum=0
# for i in l:
#     sum=sum+i    
#     print(sum)


# for i in range(2,5):     
#     print(i)


# print("\n-----------------------------\n")

# # 6. WHILE LOOP
# # --------------------------------------------------
# print("While Loop Example")

# count = 1        
# while count <= 5:
#     print(count)
#     count += 1  

# n=5
# sum=0
# i=1
# while i <=n:
#     sum=sum+i
#     i=i+1
# print(sum)

# s=1
# while s>0:
#     print(s)
#     s=s+1

# print("\n-----------------------------\n")









# # 7. BREAK STATEMENT
# # --------------------------------------------------
# print("Break Example")

# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)

# print("\n-----------------------------\n")

# # 8. CONTINUE STATEMENT
# # --------------------------------------------------
# print("Continue Example")

# for i in range(1, 10):
#     if i == 5 or i==8:
#         continue
#     print(i)

# print("\n-----------------------------\n")

# # 9. PASS STATEMENT
# # --------------------------------------------------
# print("Pass Example")

# for i in range(3):
#     pass
     # Placeholder (does nothing)

# l=[-1,-2,0,1,2]
# for i in l:
#     if i>=0:
#         pass
#     else:
#         print(i)
# print("Loop executed with pass")

# print("\n-----------------------------\n")

# # 10. ASSERT STATEMENT
# # --------------------------------------------------
# print("Assert Example")

# a = 10
# b = 15

# assert a > b, "a should be greater than b"

# print("Assertion passed")

# print("\n-----------------------------\n")

# # 11. LOOP WITH ELSE
# # --------------------------------------------------
# print("Loop with else Example")

# for i in range(3):
#     print(i)
# else:
#     print("Loop completed successfully")

# print("\n--- END OF CONTROL STATEMENTS ---")




# for i in range(1,3):       
#     for j in range (4):
#         print("i=",i,"\t","j=",j)



# for i in range(1,6):
#     print("*"*i)



# for i in range(1,6):    
#     for j in range(1,i+1):  
#         print("*",end="")
#     print()