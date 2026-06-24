import numpy as np # importing numpy as np
array1=np.array([1,2,3,4,5]) # assigning an array
array1=array1*3 # multiply array values with 3
print(array1)
array4=np.array('A')# 0 dimensional array
array2=np.array(['A','B','C']) # 1D array
array3=np.array([[1,2,3],[4,5,6],[7,8,9]]) # 2D array
array=np.array([[['A','B','C'],['D','E','F'],['G','H','I'], # 3D array
                 ['J','K','L'],['M','N','O'],['P','Q','R'],
                 ['S','T','U'],['V','W','X'],['Y','Z','_'],],])
print(array4.ndim)
print(array2.ndim)
print(array3.ndim)
print(array.ndim)
array =np.array([1,2,3,4,5,6,7], dtype=np.int16 ) #sets the datatype and assigns the number of bits
print(f"{array.nbytes} bytes")
array=np.array([[['A','B','C'],['D','E','F'],['G','H','I']], #layer 0
                 [['J','K','L'],['M','N','O'],['P','Q','R']],# layer 1
                 [['S','T','U'],['V','W','X'],['Y','Z','_']],]) # layer 2
print(array[0,0,0]) # it will print layer one's row one's index 0
word =array[0,0,0]+array[1,0,2]+array[0,2,2] # it will print word Ali
print(word)
myname= array[1,1,0]+array[0,0,0]+array[1,1,1]+array[0,0,0]+array[1,1,1]
print(myname)