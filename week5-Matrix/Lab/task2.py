import numpy as np


#create two matrix B & C

B = np.array([[4,7,2],[3,2,5],[6,4,3]], dtype=int)
C = np.array([[3,1,9],[7,5,8],[2,1,1]], dtype=int)

print('Matrix B: \n',B,'\nMatrix C: \n',C)

#product p for matrix B and C
productPof_BC = np.matmul(B,C)

print('Product [multiply] of B and C [b x c]: \n', productPof_BC)

