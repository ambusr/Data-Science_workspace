import module,math,calendar

# module.demo()
print("Sum is",module.add(5,5,5))
x=math.ceil(7.5)
y=math.floor(7.5)

print(x,y)

year = int(input("Enter year: "))
month=int(input("Enter month: "))

print(calendar.month(year,month))