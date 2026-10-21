# # vehicle class , abs method start. sub class car & bike
from abc import *
# class vehicle (ABC):
#     @abstractmethod
#     def start(self,x):
#         pass
# class car (vehicle):

#     def start(self, x):
#         print(f"{x} started")
# class bike (vehicle):

#     def start(self, x):
#         print(f"{x} started")

# c=car()
# b=bike()
# c.start("Swift")
# b.start("Pulsar")

# class payment, abs method pay, sub class credit card & upi

# from abc import *
# class payment(ABC):
#     @abstractmethod
#     def pay(self,x):
#         pass
# class credit_card(payment):
#     def pay(self,x):
#         print(f"Payment done through Credit card")
# class upi(payment):
#     def pay(self):
#         print("Payment done through UPI")
# pay1=credit_card()
# pay2=upi()
# print("payment 1")
# pay1.pay()
# print("payment 2")
# pay2.pay()



# class payment():
    
#     def pay(self):
#         pass
# class credit_card(payment):
#     def pay(self):
#         print("Payment done through Credit card")
# class upi(payment):
#     def pay(self):
#         print("Payment done through UPI")
# pay1=credit_card()
# pay2=upi()
# print("payment 1")
# pay1.pay()
# print("payment 2")
# pay2.pay()

# Abstract Class – Example Questions
# 1.Shape and Circle
# Create an abstract class Shape with an abstract method area().
# Create a Circle class that inherits from Shape.
# Calculate and display the area of the circle.


class shape (ABC):
    @abstractmethod
    def area(self,x):
        pass
class circle (shape):
    def area(self,x):
        print(f"Area of circle with radious {x} is {(3.14159*(x**2)):.2f}")
c=circle()
c.area(5)




# 2.Vehicle
# Create an abstract class Vehicle with an abstract method start().
# Create Car and Bike classes that implement start().
# Display how each vehicle starts.

class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car started with key")
class bike(vehicle):
    def start(self):
        print("Bike started with kicker")
car=car()
bike=bike()
car.start()
bike.start()
    
# 3.Employee
# Create an abstract class Employee with an abstract method calculate_salary().
# Create FullTimeEmployee and PartTimeEmployee.
# Calculate salary for both.
class employee(ABC):
    @abstractmethod
    def calculate_salary(self,x):
        pass
class FullTimeEmployee(employee):
    def calculate_salary(self, x):
        print("Full time employee")
        print(f"Basic pay Rs {x}, Full time employee benifit Rs 5000. Total salary Rs {x+5000}")
class PartTimeEmployee(employee):
    def calculate_salary(self, x):
        print("part time employee")
        print(f"Basic pay Rs {x}, Full time employee benifit - NA Total salary Rs {x}")
e1=FullTimeEmployee()
e2=PartTimeEmployee()
e1.calculate_salary(25000)
e2.calculate_salary(25000)


# 4.Animal
# Create an abstract class Animal with an abstract method sound().
# Create Dog and Cat classes.
# Display their sounds.
class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        print("Dog Sound : Bow Bow")
class cat(animal):
    def sound(self):
        print("Cat sound: Meww")
dog=dog()
cat=cat()
dog.sound()
cat.sound()

# 5 Bank Account
# Create an abstract class BankAccount with an abstract method calculate_interest().
# Create SavingsAccount and CurrentAccount.
# Calculate interest for each account.
class BankAccount(ABC):
    @abstractmethod
    def calculate_interest(self,x):
        pass
class SavingsAccount(BankAccount):
    def calculate_interest(self, x):
        print("Savings account balance Rs ",x)
        print(f"2% interest on saving account. Balance Rs {(x+(x*0.02)):.2f}")
class CurrentAccount(BankAccount):
    def calculate_interest(self, x):
        print("Current account balance Rs ",x)
        print(f"3% interest on current account. Balance Rs {(x+(x*.03)):.2f}")
sb=SavingsAccount()
ca=CurrentAccount()
sb.calculate_interest(25000)
ca.calculate_interest(25000)
# 1.Printable Interface
# Create an interface-like class Printable with print_data().
# Create Student and Employee classes.
# Implement print_data() in both.

class printable(ABC):
    @abstractmethod
    def print_data(self):
        pass
class students(printable):
    def print_data(self):
        print("Students Class")
class Employees(printable):
    def print_data(self):
        print("Employee Class")
s1=students()
E1=Employees()
s1.print_data()
E1.print_data()

# 2.Database Interface
# Create an interface-like class Database with connect() and disconnect().
# Create MySQLDatabase and MongoDBDatabase.
# Implement both methods.

class database(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def disconnect(self):
        pass
class MySQLDatabase(database):
    def connect(self):
        print("MySQL batabase connected successfully")
    def disconnect(self):
            print("MySQL batabase disconnected successfully")
class MongoDBDatabase(database):
    def connect(self):
            print("MongoDB batabase connected successfully")
    def disconnect(self):
                print("MongoDB batabase disconnected successfully")
db1=MySQLDatabase()
db2=MongoDBDatabase()
db1.connect()
db2.connect()
db1.disconnect()
db2.disconnect()


# 3.Notification Interface
# Create an interface-like class Notification with send().
# Create EmailNotification and SMSNotification.
# Display how each notification is sent.

class notification(ABC):
    @abstractmethod
    def send (self,x,y):
        pass
class EmailNotification(notification):
    def send(self,x,y):
        print(f"EMail message:{y}  - send to {x}")
class SMSNotification(notification):
    def send(self,x,y):
            print(f"Sms:{y} - send to {x}")
mail=EmailNotification()
sms=SMSNotification()
mail.send("Arun","Hi, How are you")
sms.send("Vishnu","This is my new number")


# 4.Remote Control Interface
# Create an interface-like class RemoteControl with turn_on() and turn_off().
# Create TV and AC classes.
# Implement both methods.

class RemoteControl(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    @abstractmethod
    def turn_off(self):
        pass
class TV(RemoteControl):
    def turn_on(self):
        print("Tv turned on")
    def turn_off(self):
            print("TV turned off")
class AC(RemoteControl):
    def turn_on(self):
        print("AC turned on")
    def turn_off(self):
            print("AC turned off")
Tv=TV()
Ac=AC()
Tv.turn_on()
Tv.turn_off()
Ac.turn_on()
Ac.turn_off()                