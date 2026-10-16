# Vehicle class with brand & model, car class inherited from vehicle. display car brand, model & type.

class vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class car(vehicle):
    
    def __init__(self,brand,model,type):
        super().__init__(brand,model)
        self.type=type
    def display (self):
        print(f"car brand is {self.brand},model {self.model}, type:{self.type}")
obj=car("ford",2015,"Petrol")
obj.display()


## Excercise ##
# 1.Animal → Cat
class animal:
    def __init__(self,name):
        self.name=name
class cat(animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color
    def display(self):
        print(f"cat name is {self.name}, color:{self.color}")
c=cat("Tom","Grey")
c.display()
# 2.Vehicle → Bike
class vehicle:
    def __init__(self,brand):
        self.brand=brand
class bike(vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model
    def display(self):
        print(f"Vehicle Brand:{self.brand}, and Model:{self.model}")
b=bike("Bajaj","Pulsar")
b.display()

# 3.Person → Employee
# 4.Employee → Manager
# 5.Account → SavingsAccount
# 6.Product → DiscountProduct
# 7.School → Student
# 8.Shape → Circle
# 9.Vehicle → Car → ElectricCar
class vehicle1:
    def __init__(self,veh_type):
        self.veh_type=veh_type
class car(vehicle1):
    def __init__(self,veh_type,c_type):
        super().__init__(veh_type)
        self.c_type=c_type
class Ecar(car):
    def __init__(self,veh_type,c_type,range):
        super().__init__(veh_type,c_type)
        self.range=range
    def display(self):
        print(f"Vehicle type:{self.veh_type}, Car type:{self.c_type}, range:{self.range}KM")
veh=Ecar("Car","electric",150)
veh.display()
    
# 10.Person → Teacher and Student
class person:
    def __init__(self,name):
        self.name=name
class teacher(person):
    def __init__(self,name,role):
        super().__init__(name)
        self.role=role
    def display (self):
        print(f"Person name: {self.name}, role:{self.role}")
class student(person):
    def __init__(self,name,role):
        super().__init__(name)
        self.role=role
    def display (self):
        print(f"Person name: {self.name}, role:{self.role}")
t=teacher("Anitha","Teacher")
t.display()
s=student("arun","student")
s.display()
# 11.animal → Dog → Puppy
# 12.Father + Mother → Child (multiple inheritance)
class father:
    def __init__(self,F_initial):
        self.F_initial=F_initial
class mother:
    def __init__(self,M_initial):
            self.M_initial=M_initial
class child(father,mother):
    def __init__(self,F_initial,M_initial,name):
        father.__init__(self,F_initial)
        mother.__init__(self,M_initial)
        self.name=name
    def display(self):
        print(f"Child name is {self.name}.{self.F_initial}.{self.M_initial}")
ch=child("S","R","AMBU")
ch.display()