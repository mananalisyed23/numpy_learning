import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(arr)
#---Now using reshape function we will reshape our arra
print("Reshaped array:")
arr=arr.reshape(2,6)
print(arr)
#---We can also convert the array into 3-dimensional array by passing layer number
arr=arr.reshape(3,2,2)
print(arr)
#--- Now we will see slicing index
array= np.array([[1,2,3,4],[5,6,7,8],
                 [9,10,11,12],[13,14,15,16]])
#---Row selection method
print(array[0:]) #will print all indices
print("Step statement:")
print(array[0:4:2]) #prints every index after gap of 2
#---Column selection method
print(array[:,0]) # will give every row's column 0 index value
print(array[:, 0:3]) # it means first select all rows and then start from index 0 of column upto index 2
print(array[:,1:4])  #this will skip 1st column and goes upto column 4
print(array[:,1::2])# all rows 2nd column upto last with the gap of 2
print(array[:,::-1])# all values will be reversed
print(array[:,::-2])# all values will be reversed with gap of 2
print(array[2:,2:])# shows the last 2 rows and last 2 columns