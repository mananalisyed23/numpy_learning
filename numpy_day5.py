import numpy as np

#--- Random function
#-- This function generates random values within a range of numbers
rng = np.random.default_rng(1)
print(rng.integers(1,7))
print(rng.integers(1,101,3))
print(rng.integers(1,101,(3,2)))

#---floating points
#-- This function generates random floating point values within a range of numbers
np.random.seed(seed=1) # will give same outputs
print(np.random.uniform(1,4,(3,3)))

#---Array shuffle
#-- Shuffle method is used to shuffle the array's values
rng =np.random.default_rng()
array =np.array([1,2,3,4,5,6])
rng.shuffle(array)
print(array)

#---Random Choice
#-- This function is used to choose a random value from an array
rng=np.random.default_rng()
fruits =np.array(['🍎','🍊','🥥','🍌','🍑'])
fruit =rng.choice(fruits)
fruits =rng.choice(fruits,size=(3,4))
print(fruit)
print(fruits)

#---Save function
#-- This is used to save the values of numpy array in a file
array =np.array([[1,2,3],
                 [4,5,6]])
np.save('C:\\Users\\lenovo\\OneDrive\\Desktop\\Data',array)
print('Array was saved')

#---load function
#-- This is used to load the values of numpy array in a file
array2= np.load('C:\\Users\\lenovo\\OneDrive\\Desktop\\Data.npy')
print(array2)


#---Savez function
#-- This is used to save the values of multiple numpy array in a file
arr1 =np.array([[1,2,3],
                 [4,5,6]])
arr2 =np.array([1.1,2.2,3.3])
np.savez('MAData',arr1,arr2)
np.savez_compressed('MAData2',arr1,arr2)
print('Multiple Arrays were saved')

#--- Multiple values through array key can be loaded
arrays= np.load('MAData.npz')
new_arr1=arrays['arr_0']
new_arr2=arrays['arr_1']
print(new_arr1,new_arr2)
