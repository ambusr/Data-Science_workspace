# 1
print('Triangele')
for i in range(1, 7):
    print('* '* i)
#2
print('inverted trainge')
for i in range(7,0,-1):
    print('* '*i)
#3
print('Pyramid ')
for i in range(1,11,2):
    print('* ' *i)

#4
print('Inverted Pyramid')
for i in range(10,0,-2):
    print('* ' *i)

#5
print('Diamond pattern')
for i in range(1,7):
     print('*  ' *i) 
for j in range(5,0,-1):
    print('*  '*j)

#6
print('square pattern')
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print('*',end=' ')
        else:
            print(' ', end=' ')
        
    print()

#7
print('full square pattern')
for i in range(5):
    print('* * * * * ' )

#8
print('right angle trangle by using numbers')
for i in range(1,7):
    print(' '.join(str(x) for x in range(1, i+1)))   

#9
