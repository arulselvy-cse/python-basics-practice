import numpy as np
arr1 = np.array([10,20,30,40])
print("1D array:",arr1)
arr2 = np.array([[1,2,3],[4,5,6]])
print("2D array:",arr2)

//array properties
print("Shape of arr2:",arr.shape)
print("Data ypes of arr2:",.dtype)
print("Number of dimensions:",ndim)

//array operations 
arr = np.array([10,20,30,40,50])
print(arr + 5) #15....
print(arr * 2) #20...
print("Sum:", arr.sum())
print("Mean:",arr.mean())

//Indexing & slicing
arr = np.array([10,20,30,40,50])
print(arr[0])  #10
print(arr[-1]) #50
print(arr[1:4])  #20 20 40

