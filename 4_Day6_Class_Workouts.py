#For Loop
# 1.Print number from 1 to 100 using For Loop
print("Print number from 1 to 100 using For Loop")
for i in range(1, 101):
    print(i)
# 2.Print all even numbers between 1 and 50
print("Print all even numbers between 1 and 50")
for i in range(2, 51, 2):
    print(i)
#  3.Find the sum of numbers from 1 to 100  
print("Find the sum of numbers from 1 to 100")
sum=0
for i in range(1,101):
    sum=sum+i
print("Sum of numbers from 1 to 100 is:",sum)
# 4.Ask the user for a number and check whether it is positive, negative, or zero.
print("Ask the user for a number and check whether it is positive, negative, or zero")
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Number is zero")

#   5.print the multiplication table of a number entered by the user.
print("Print the multiplication table of a number entered by the user")
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num," * ",i," = ",num*i)



 #6.Count how many vowels are in a word.

#7.Find the largest number in a list.
num = [36, 57, 2, 82, 11, 93, 45]
largest = num[0]
for i in num:
    if i > largest:
        largest = i
print("The largest number in the list is:", largest)

#8.Print numbers from 10 down to 1 using a while loop.
i = 10
while i >= 1:
    print(i)
    i -= 1
# 9.Ask for a student's marks and display their grade using if-elif-else.
marks = int(input("Enter the  mark: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Failed")

word=(input("Enter a word: "))
word=word.lower()
vowels = "aeiou"
vowel_count = 0
for i in word:
    for j in vowels:
        if i == j:
            vowel_count += 1
print("The number of vowels in the word is:", vowel_count)