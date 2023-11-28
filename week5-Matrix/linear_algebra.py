from builtins import object

import numpy as np

# define scaler C
C = int(5)
#define three dimentional vector A
A = np.array(object=[1,2,3], dtype=int)
#multiply scaler and the vector
# it is scaler multiplication.
B = C*A
print('Scaler C: ',C,'\nThree dimensional vector A: ',A ,'\nScaler multiplication result',B)

X = np.array([3,4,5], dtype=int) #vector X
Y = np.array([5,6,7], dtype=int) #vector Y
Z = np.add(X,Y) #sum two vector [(x1+y1), (x2+y2) --- (xn+yn)]
print('\t vector addition','\nVector X: ',X,'\nVector Y: ',Y ,'\nVector addition result: ',Z)

#dot product
dotX = np.array([1,2,3], dtype=int)
dotY = np.array([5,10,15], dtype=int)
#calculate dot product D
D = np.dot(dotX, dotY)
print('\tdot product','\nVector dotX: ',dotX,'\nVector dotY: ',dotY ,'\nDot Product: D',D)

