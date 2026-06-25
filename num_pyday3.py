import numpy as np
#---Scalar Arithmetics
#--Scalar is a linear algebra term and this performs simple arithmetic functions on array
array =np.array([1,2,3])
print(array+1)
print(array-1)
print(array*2)
print(array/2)
print(array**4)
#---Vector Math functions
#--Vector Math functions are used to apply math functions on linear algebra equations in python
arr =np.array([2.4,4.6,6.8])
print(np.sum(arr))
print(np.sqrt(arr))
print(np.round(arr))
print(np.floor(arr))
print(np.ceil(arr))
#--Now combining scalar functions with vector functions
radius=np.array([4,5,6])
print(np.pi*radius**2) #Will calculate the area of a circle

#---Element-wise operations
#--In element-wise operations each element of array one performs action with each element of second array
array1=np.array([3,4,7])
array2=np.array([4,2,7])
print(array1+array2)
print(array2-array1)
print(array2*array1)
print(array2/array1)
print(array2**array1)

#---Comparison Operations
#--Through Comparison Operations we can perform:
#-a-Creations of Boolean Array
#-b-Data Filteration
#-c-Element-wise Comparison






