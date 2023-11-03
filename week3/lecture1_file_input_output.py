#reading and save file using numpy
import numpy as np
import random as rnd

myAray = np.empty((3, 4), dtype=int)
print(myAray)

for i in range(0, 3):
    for j in range(0, 4):
        myAray[i,j] = rnd.randint(1, 99)
        print(myAray[i,j], end='')
    print('')

#save my text
np.savetxt('myArray.csv', myAray, fmt='%d', delimiter=',')
#read my file
reading_file = np.genfromtxt('MyArray.csv', delimiter=',', dtype='unicode')
print('generated array: ',reading_file, '\nshape: ',reading_file.shape)