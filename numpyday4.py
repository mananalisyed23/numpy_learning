import numpy as np
#---Zero's function
#fills 1D array with having all zeros in all columns
array1= np.zeros(10)
print(array1)

#---One's function
#fills 2D array with having all ones in 2 layers, 3 rows and 10 columns
array2= np.ones((2,3,10))
print(array2)

#---Full function
#Fills 2D array with having all 5's in 2 layers, 3 rows and 10 columns
array3= np.full((2,3,10),5)
print(array3)

#---Eye function
#It is also called identity function puts 1 in diagonal and others as 0
array4= np.eye(3)
print(array4)

#---Empty function
#It assigns garbage values in metrics
array5= np.empty((2,3))
print(array5)

#---Arrange function
#This function will arrange all values in a matrics inside the given range
array6= np.arange(2,100,2)
print(array6)


