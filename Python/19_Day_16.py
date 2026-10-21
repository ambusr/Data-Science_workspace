# 1.Student Class
# Create a Student class with private attributes name and mark.
# Use getter and setter methods to access and modify them.
class Student:
    __name = "Suresh"
    __mark = 85

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_mark(self):
        return self.__mark

    def set_mark(self, mark):
        if 0 <= mark <= 100:
            self.__mark = mark
        else:
            print("Invalid mark. Please enter a value between 0 and 100.")
a=Student()
print(a.get_name())
print(a.get_mark())
a.set_name("Ramesh")
a.set_mark(90)
print(a.get_name())
print(a.get_mark())

# 2.Bank Account
# Create a BankAccount class with a private balance.
# Create methods deposit(), withdraw(), and get_balance().
# Prevent withdrawal if the amount is greater than the balance.
class BankAccount:
    name = "Suresh"
    __balance = 1000
    deposit_amount = 0
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew: {amount}. New balance: {self.__balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")
    def get_balance(self):
        print("Current balance:", self.__balance)
user=BankAccount()
user.get_balance()
user.deposit(500)
user.withdraw(200)
user.get_balance()

# 3.Employee Salary
# Create an Employee class with private attributes name and salary.
# Allow salary to be changed only through a setter method.
# Reject negative salary values.
class Employee:
    __name="John"
    __salary=50000
    def show_salary(self):
        print(f"Employee Name: {self.__name}, Salary: {self.__salary}")
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
            print(f"Salary updated to: {self.__salary}")
        else:
            print("Salary cannot be negative.")
salary=Employee()
salary.show_salary()
salary.set_salary(60000)
salary.show_salary()

# 4.Product Price
# Create a Product class with private price.
# Create get_price() and set_price() methods.
# Do not allow the price to be negative.
class Product:
    product_name = "Laptop"
    __price=50000
    def get_price(self):
        print(f"Product: {self.product_name}, Price: {self.__price}")
    def set_price(self, price):
        if price>0:
            self.__price=price
            print("Price updated")
pro=Product()
pro.get_price()
pro.set_price(55000)
pro.get_price()

# 5.Person Age
# Create a Person class with private age.
# Use a setter to ensure age is between 1 and 100.
class person:
    name="Manu"
    __age=25
    def get_details(self):
        print(f"Name:{self.name},Age:{self.__age}")
    def set_age(self,age):
        if age>0:
            self.__age=age
            print("Age updated")
        else:
            print("Age must be positive")
per=person()
per.get_details()
per.set_age(28)
per.get_details()

# 6.Mobile Phone
# Create a Mobile class with private __price.
# Create methods to display and update the price.
# Do not allow a negative price.
class mobile:
    model="Samsung "
    __price=35000
    def display(self):
        print(f"Current price for {self.model} is {self.__price}")
    def update(self,cost):
        if cost>0:
            self.__price=cost
            print("price updated")
        else:
            print("invalid price")
mob=mobile()
mob.display()
x=int (input("Enter new price to update"))
mob.update(x)
mob.display()
# 7.ATM Account
# Create an ATM class with private __pin and __balance.
# Create methods to change PIN, deposit money, and withdraw money.
# Allow withdrawal only after correct PIN verification.

class ATM:
    cus_name="Arun"
    __pin=0000
    __balance=1000
    print("Default pin is 0000, kindly set a new pin")
    __balance=50000
    def change_pin(self):
        self.__pin=int(input("enter a new pin"))
    def deposit(self):
        amt=int(input("enter deposit amount"))
        if amt>0:
            self.__balance+=amt
            print("Amount successfully deposited")       
        else:
            print("invalid Amount")
    def withdraw(self):
        pin=int(input("enter your pin to withdraw"))
        if pin==self.__pin:
            amt=int(input("enter withdraw amount"))
            if amt>0 & amt<self.__balance:
                self.__balance-=amt
                print(f"Rs {amt} withdrawn and cussrent balance is {self.__balance}")
            else:
                print("Invalid amount")
        else:
            print("Incorrect pin")
    def check_bal(self):
        print(f"Account name:{self.cus_name}, balance Rs {self.__balance}/-")
        
cust=ATM()
cust.check_bal()
cust.change_pin()
cust.deposit()
cust.withdraw()
cust.check_bal()            
        
        
# 8.Car Speed
# Create a Car class with private __speed.
# Create accelerate() and brake() methods.
# Speed should never become negative.
# Student Marks
# Create a Student class with private __marks.
# Create a method to set marks.
# Accept marks only between 0 and 100.
# Display the marks using a getter.
# 9.Bank Account with Interest
# Create a BankAccount class with private __balance.
# Create methods for deposit, withdrawal, and calculating interest.
# The balance should not be directly accessible outside the class.

class check1:
    _protected=1
    __private=2
    public=3
    def disp1(self):
        print(f"Main Class - private={self.__private},protected={self._protected},publice={self.public}")
class check2(check1):
    def disp2(self):
            print(f"Main Class - private=,protected={self._protected},publice={self.public}")

a=check1()
b=check2()
a.disp1()
b.disp2()
print("direct call from main class",a._protected,a.public)
