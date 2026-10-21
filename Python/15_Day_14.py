class bank:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        
    def output(self):
        print("name: ",self.name)
        print("balance",self.balance)
ob1=bank("Akhil",50000)
ob2=bank("sunil",45000)
ob1.output()
ob2.output()

# Constructr with default value
class bank:
    def __init__(self,name,balance=80000):
        self.name=name
        self.balance=balance
        
    def output(self):
        print("name: ",self.name)
        print("balance",self.balance)
ob1=bank("Akhil")
ob2=bank("sunil",45000)
ob1.output()
ob2.output()

#Destructor
class Student:

    def __init__(self, name):
        self.name = name
        print(self.name,"Object Created")

    def __del__(self):
        print("Object Destroyed")


s1 = Student("Anu")
del s1

#constructor / destructor
class product:
    count=1
    def __init__(s,name,price):
        s.name=name
        s.price=price
        
        s.count=product.count #stores 1 in count
        product.count+=1      #incriments count using class attribute
         
    def display(s):
        print(s.name)
        print(s.price)
        print(s.count)
    def __del__(s):
        print("product destroyed")
p1=product("cpu",50000)
p2=product("ups",25000)
p1.display()
p2.display()
del p1
del p2

