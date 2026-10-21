import numpy as np

zeros_arr = np.zeros((3, 4)) # 3 row and 4 coloumn
print("Zero array\n",zeros_arr)

ones_arr = np.ones((2, 3))
print("Ones array\n",ones_arr)

print()
range_arr=np.arange(1,10,2)
print("range array",range_arr)

linspace_arr = np.linspace(0, 1, 5)
print("\n Linear Space Array",linspace_arr,'\n')

identity_arr = np.eye(4)
print("Identity Matrix\n",identity_arr)

random_arr = np.random.rand(3, 3)  #array with random values of 0 to 1
print("\nRandom Array\n",random_arr)

random_int_arr=np.random.randint (1,10,(3,3))  #random number between 1-9
print("\n random Int Array 1-9\n",random_int_arr)

random_with_negative=np.random.randn(2,3)   # the values can be -ve or +ve
print("\n random with neg values \n",random_with_negative)

m=[1,2,3,4,8]
print("\n Before zero like\n", m)
n=np.zeros_like(m)
print("\n after zero like\n",n)
print("\n Ones like",np.ones_like(m))


print("Array creation & printing")
arr1 = np.array([[1, 2, 3]])
arr2=np.array([[1, 2, 3], [4, 5, 6]])
arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("\n one Dim Array \n",arr1)
print("\n Two Dim Array \n",arr2)
print("\n Three Dim Array \n",arr3)


arr = np.array([[1, 2, 3], [4, 5, 6]])
print("\n Array Shape: ",arr.shape,' Array data type: ',arr.dtype,' Array Dimension: ',arr.ndim)