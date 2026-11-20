# List comprehension to create a list of even numbers from 1 to 10
even_numbers = [i for i in range(1,11 ) if i % 2 == 0]
print("Even numbers from 1 to 10:", even_numbers)
# create a list of given numbers and print the original list
x=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(1,n+1):
    i=int(input("Enter the element: "))
    x.append(i)
print("Original list:", x)

# for loop to retrieve elements from a dictionary
dict= {"a":"apple","b":"ball","c":"cat","d":"doll"}
for i in dict.keys():
    print(i)
for j in dict.values():
    print(j)
for i,j in dict.items():
    print("key:",i," value: ",j)

#occurrence of each letter in a string
strg=input("enter a string: ")
d={}
for i in strg:
    d[i]=d.get(i,0)+1
print(d)

# print prime numbers upto given number
n=int(input("Enter a number: "))
for i in range(2,n+1):
    count=0
    for j in range(1,i+1):
        if (i%j)==0:
            count+=1
    if (count==2):
        print('\t',i,end="")

#print fibonacci series upto given number
n=int(input("Enter a number: "))
a=0
b=1
if n==1:
    print(a)
elif n<=0:
    print("sorry given number is less than or equal to 0")    
elif n==2:
    print(a,b,end=" ")
else:
    print(a,b,end=" ")
    for i in range(1,n-1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
