# main.py

# Import full module
import mymodule

# Call function
mymodule.greeting("Sona")

# Call add function
result = mymodule.add(10, 5)
print("Addition:", result)

# Access variable
print("Person Name:", mymodule.person1["name"])
print("Person Age:", mymodule.person1["age"])


# Import module with alias
import mymodule as mx

mx.greeting("Anu")


# Import specific function
from mymodule import add

print("Addition using from import:", add(20, 30))


# Built-in module example
import platform

print("System:", platform.system())


# dir() function example
print("Platform module contents:")
print(dir(platform))
