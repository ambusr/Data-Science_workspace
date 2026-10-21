# 1.Create Person, Student, and Teacher classes and demonstrate method overriding.
class Person:
    def display(self,name):
        print("Person name is",name)
class Student():
    def display(self,name):
        print("Student name is",name)
class Teacher():
    def display(self,name):
        print("Teacher name is",name)
p1=Person()
s1=Student()
t1=Teacher()   
p1.display("Aneesh")
s1.display("Arun")
t1.display("Suma")


# 2.Create Bank, SBI, and HDFC classes with different interest_rate() methods.
class Bank:
    def interest_rate(self):
        return 0

class SBI(Bank):
    def interest_rate(self):
        return 10.5

class HDFC(Bank):
    def interest_rate(self):
        return 8.0

bnk=Bank()
sbi=SBI()
hdfc=HDFC()
print("Bank interest rate:", bnk.interest_rate())
print("SBI interest rate:", sbi.interest_rate())
print("HDFC interest rate:", hdfc.interest_rate())

# 3.Create Employee, Manager, and Developer classes with different work() methods.
class Employee:
    def work(self):
        print("Employee class")

class Manager(Employee):
    def work(self):
        print("Manager class")

class Developer(Employee):
    def work(self):
        print("Developer class")
emp=Employee()
man=Manager()
dev=Developer()

emp.work()
man.work()
dev.work()

# 4. Create Animal, Dog, Cat, and Cow classes with different sound() methods.
class Animal:
    def sound(self):
        print("Default sound")

class Dog(Animal):
    def sound(self):
        print("bow bow")

class Cat(Animal):
    def sound(self):
        print("Meow")

class Cow(Animal):
    def sound(self):
        print("Moo")
ani=Animal()
dog=Dog()
cat=Cat()
cow=Cow()
ani.sound()
dog.sound()
cat.sound()
cow.sound()


# 5.Create Food, Pizza, and Burger classes with different price() methods.
class Food:
    def price(self):
        print("Default price")
class Pizza(Food):
    def price(self):
        print("Pizza price is 200")

class Burger(Food):
    def price(self):
        print("Burger price is 100")
f=Food()
p=Pizza()
b=Burger()
f.price()
p.price()
b.price()


# 6.Create Notification, Email, and SMS classes with different send() methods.
class Notification:
    def send(self):
        print("Message sent")
class Email(Notification):
    def send(self):
        print("Email sent")
class SMS(Notification):
    def send(self):
        print("SMS sent")

n=Notification()
e=Email()
s=SMS()
n.send()
e.send()
s.send()
# 7.Create Shape, Square, and Triangle classes with different area() methods.
class Shape:
    def area(self):
        print("Default area")
class Square(Shape):
    def area(self, side):
        print("Area of square is", side * side)
class Triangle(Shape):
    def area(self, base, height):
        print("Area of triangle is", 0.5 * base * height)
sh=Shape()
sq=Square()
tr=Triangle()
sh.area()
sq.area(5)
tr.area(4,6)
# 8.Create Account, SavingsAccount, and CurrentAccount classes with different withdraw() methods.
class Account:
    def withdraw(self):
        print("Default withdraw")
class SavingsAccount(Account):
    def withdraw(self, amount):
        print(f"Withdrawn {amount} from savings account")
class CurrentAccount(Account):
    def withdraw(self, amount):
        print(f"Withdrawn {amount} from current account")
acc=Account()
sav=SavingsAccount()
cur=CurrentAccount()
acc.withdraw()
sav.withdraw(1000)
cur.withdraw(2000)       
