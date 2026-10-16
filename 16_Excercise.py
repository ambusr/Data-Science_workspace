#  1.Student Class
# Create a Student class with a constructor that accepts name and age. Create two objects and display their details.
class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name," is ",self.age," years old")

p1=student("sanu",28)
p2=student("varun",32)
p1.display()
p2.display()

print()    
# 2.Employee Class
# Create an Employee class with name, id, and salary. Initialize these using a constructor and display the details.
class employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def display(self):
        print(self.name," with ID: ",self.id," is having salary of Rs.",self.salary)

e1=employee("Arun",2855,25000)
e2=employee("Malu",3255,33000)
e1.display()
e2.display()

print()
# 3.Car Class
# Create a Car class with brand, model, and price. Use a constructor to initialize the values.
class car:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
    def display(self):
        print("Brand:",self.brand,", Model:",self.model,", Price:Rs.",self.price)

c1=car("Hyundai","i20",800000)
c2=car("Maruti","swift",750000)
c1.display()
c2.display()

print()
# 4.Book Class
# Create a Book class with title and author. Create three objects and display their details.
class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        print("Book name:",self.title,", Author:",self.author)
b1=book("Mathilukal","Basheer")
b2=book("Randamoozham","M.T. Vasudevan")
b3=book("Aatujeevitham","Benyamin")
b1.display()
b2.display()
b3.display()

print()
# 5.Mobile Class
# Create a Mobile class with brand and price. Use a constructor to initialize the values.
class mobile:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Mobile Brand:",self.brand,", Price Rs.",self.price)
m1=mobile("Samsung s24", 95000)
m2=mobile("Oneplus 12",65000)
m1.display()
m2.display()  

print()
# 6.Bank Account
# Create a BankAccount class with: Account holder name, Account number, Balance
# Use a constructor and create methods for deposit() and withdraw(). 
class bank:
    def __init__(self,acc_name,acc_no,bal):
        self.acc_name=acc_name
        self.acc_no=acc_no
        self.bal=bal
        print("Account Name:",self.acc_name,",Account number:",self.acc_no,",Current Balance: Rs.",self.bal)
    def deposit(self,amt):
        self.amt=amt
        print("Deposited Rs.",self.amt,"and Current balance Rs.",self.bal+self.amt)
    def withdraw(self,deb):
        self.deb=deb
        print("Debited Rs.",self.deb,"from your acc & current balance is Rs",(self.bal+self.amt)-self.deb )
bnk1=bank("Adhvik",20120,25000)
bnk1.deposit(5000)
bnk1.withdraw(15000)

print()
# 7.Product Discount
# Create a Product class with name and price. Use a constructor and create a method to calculate a 10% discount.
class discount:
    discc=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        print("Product name:",self.name,", Price: Rs.",self.price)
    def disc_calc(self):
        discount.discc+=self.price-(self.price*.10)
        print("Original Price: Rs",self.price,"Price after 10% discount",self.discc)
d1=discount("Maggy",60)
d1.disc_calc()

print()
# 8.Rectangle
# Create a Rectangle class with length and width. Use a constructor and create methods to calculate:
# # Area # Perimeter
class rectangle:
    def __init__(self,len,wid):
        self.len=len
        self.wid=wid
        print("length of rectangle",self.len,"cm and width",self.wid,"cm")
    def area(self):
        print("Area of rectangle:",self.len*self.wid,"Sq.cm")
    def peri(self):
            print("Perimeter of rectangle:",2*(self.len+self.wid),"cm")
r1=rectangle(50,60)
r1.area()
r1.peri()
r2=rectangle(30,75)
r2.area()
r2.peri()

print()
# 9.Employee Salary
# Create an Employee class with name and salary. Use a constructor and create a method to calculate a 10% bonus.
class employee1:
    bon=0
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
        print("Employee name:",self.name,", Current Salary:Rs",self.sal)
    def bonus(self):
        employee1.bon+=self.sal+(self.sal*.10)
        print("Added bonus 10% and new salary: Rs",employee1.bon)
emp1=employee1("Dravid",35000)
emp1.bonus()

print()
# 10.Circle
# Create a Circle class with radius. Use a constructor and create methods to calculate area and circumference.
class circle:
    def __init__(self,radius):
        self.radius=radius
        print("Radius of circle is",self.radius)
    def area (self):
        print("Area of circle with radius",self.radius,"cm is",3.14159*(self.radius*self.radius),"Sq.cm")
    def circum(self):
        print("Circumference of circle with radius",self.radius,"cm is",2*3.14159*self.radius,"cm")
cir=circle(130)
cir.area()
cir.circum()