import numpy as np
print("1 Dim array indexing\n")
arr=np.array([0,1,2,3,4,5])
print("Value in  index [0] is ",arr[0],"\nvalue in index[4] is ",arr[4])

print("\n 1D Array slicing\n")
print(arr[0:4])
print(arr[:3])
print(arr[2:])
print(arr[::2])
print(arr[::-2])
print(arr[::-1])

print("\n 2 Dim array indexing\n")
arr2d = np.array([[0,0,0],[1,2,3],[4, 5, 6]])
print(arr2d)
print("cord 0,0 :",arr2d[0, 0])
print("cord1,2 :",arr2d[1, 2])
print("cord -1,-1 :",arr2d[-1, -1])
print("cord -1,-2 :",arr2d[-1, -2])
print("cord -2,-1 :",arr2d[-2, -1])

print("\nBoolean Indexing")

bool_arr = np.array([5, 10, 15, 20, 25])
print("Intial array ",bool_arr)
print("Number > 15 using boolean index:",bool_arr[bool_arr > 15])

print("\nFancy Indexing")

fancy_indx = np.array([100, 200, 300, 400])
print("Intial array ",fancy_indx)
print("Fancy Index [0,2]: ",fancy_indx[[0, 2]])

print("\nModify Values Using Indexing")

arr3 = np.array([1, 2, 3, 4])
print("Intial array ",arr3)
arr3[1] = 20
print("after index modifying ",arr3)


print("\nConditional Update")

arr4 = np.array([10, 20, 30, 40])
print("Initial Array ",arr4)
arr4[arr4 % 20 == 0] = 0
print ("assign 0 to numbers divisible by 20:",arr4)




