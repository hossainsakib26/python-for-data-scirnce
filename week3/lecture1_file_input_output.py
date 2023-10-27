import numpy as np
import random as rnd

myAray = np.empty((3,2), dtype=int)
print(myAray)

for i in range(0, 3):
    for j in range(0, 2):
        myAray[i,j] = rnd.randint(1, 99)
        print(myAray[i,j], end=',')
    print("")

np.savetxt('myArray.csv', myAray, fmt='%d', delimiter=',')
