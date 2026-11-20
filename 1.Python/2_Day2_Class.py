                        # 1. STRING INTRODUCTION

# 2. STRING AS ARRAY (INDEXING)
s="Hello World"
print(s)
print(s[0],s[2],s[-1])

# 3. STRING LENGTH
print("length method 1=",len(s))
print("length method 2=",s.__len__())
print("character at -5=",s[len(s)-5])

# 4. STRING CHECK METHODS
s="Hello"
print("isalpha():",s.isalpha())
print("isalnum():",s.isalnum())
print("isdigit():",s.isdigit())
print("islower():",s.islower())
print("isupper():",s.isupper())
print("istitle():",s.istitle())

# 5. PYTHON STRING SLICING  [start:stop:step]
s="0123456789"
print("start 2, stop 5:",s[2:5])
print("start not defined, stop 5:",s[:5]) 
print("start 6, stop not defined:",s[6:])
print("start -5, stop not defined:",s[-5:])
print("start not defined, stop -5:",s[:-5])
print("start 0,stop 8,step 2:",s[0:8:2])

# 6. MODIFY STRINGS
s ="hello world HELLO world hello world"
print(s)
print("capitalize:",s.capitalize())
print("lower:",s.lower())
print("upper:",s.upper())
print("swapcase:",s.swapcase())
print("casefold:",s.casefold())#casefold
print("replace world with python:",s.replace("world", "python"))
print("replace world with python 2 times:",s.replace("world", "python", 2))
d="111"
print("D=",d,"zfill(5)=",d.zfill(5))#zfill
print("rjust:",d.rjust(10, "*"))#rjust
print("ljust:",d.ljust(10, "*"))#ljust
print("center:",d.center(10, "*"))#center
print("count of 'world' in s:",s.count("world"))#count
print("count of 'world' between (0-20):",s.count("world", 0,20))
s = "hello world"
print(s.split())# split() splits by space
s = "hello w-orld"
print(s.split("-"))#split by charactor
