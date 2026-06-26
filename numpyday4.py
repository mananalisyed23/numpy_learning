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
array6= np.arange(2,100,2) #it takes 3 arguments start,stop, step
print(array6) # can also accept floating values as step

#---linspace Function
#Also for printing values within a range but only specific amount given in argument
array7= np.linspace(0,10,5)
print(array7)

#--- Aggregate Functions
#It includes multiple functions like sum,mean,
#variance,minimum, maximum ,adding columns values or rows
arr = np.array([[1,2,3],[3,4,5]])
print(np.sum(arr))
print(np.mean(arr))
print(np.std(arr))
print(np.var(arr))
print(np.min(arr))
print(np.max(arr))
print(np.argmin(arr)) # index of minimum value
print(np.argmax(arr)) # index of maximum value
print(np.sum(arr, axis=0)) # will sum all column's values
print(np.sum(arr, axis=1)) # will sum all row's values

#---Filtering:
#It is used to print values which meet specific conditions
students_ages =np.array([[21,33,17,41,14],
               [33,15,71,50,15]])
teenagers = students_ages[students_ages<18]
adults = students_ages[(students_ages>=18) & (students_ages<60)]
new_adults= np.where(students_ages>=18, students_ages, 0)
print(teenagers)
print(adults)
print('New Adults: ')
print(new_adults)