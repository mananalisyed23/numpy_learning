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
#-b-Data Filtration
#-c-Element-wise Comparison

Scores=np.array([100,55,34,67,76,80])
print(Scores==100) #will set 100 as true and all others as false
print(Scores>=60) #will set >=60 as true and all others as false
print(Scores<60) #will set 100 as true and all others as false
#--Now using subscript will assign zero to scores<60
Scores[Scores < 60] =0
print(Scores)

#---Broadcasting
#--In numpy broadcasting operations are performed on different shapes of arrays to expand them into a new
#-- virtual dimension
#---Rules:
#-a-Dimensions have same size
#-b-Or one of the dimension has size of 1

arr1=np.array([[1,2,7]])
arr2=np.array([[4],[6],[8]])

print(arr1.shape)
print(arr2.shape)
print(arr1*arr2)
myarray1=np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]])
myarray2=np.array([[4],
                   [6],
                   [8],
                   [10]])
print(myarray1.shape)
print(myarray2.shape)
print(myarray1*myarray2)

#--Displaying tables of 1 to 10

a1=np.array([[1,2,3,4,5,6,7,8,9,10]])
a2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(a1*a2)



