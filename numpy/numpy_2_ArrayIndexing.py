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



