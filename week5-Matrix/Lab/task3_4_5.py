import numpy as np

#𝟑𝒙 + 𝟐𝒚 − 𝒛 = 𝟐𝟓
#𝟐𝒙 − 𝒚 + 𝟒𝒛 = 𝟏𝟗
#𝟒𝒙 − 𝟐𝒚 + 𝟑𝒛 = 𝟏𝟖

#M [[3, 2, -1], [2, -1, 4], [4, -2, 3]]
#value V = [[25],[19],[18]]

M = np.array([[3, 2, -1], [2, -1, 4], [4, -2, 3]], dtype='int')

V = np.array([[25],[19],[18]], dtype=int)

#inverse matrix of M
inverseMatrix_M = np.linalg.inv(M)
print('inverse matrix of M: \n',inverseMatrix_M)

#multiply inverseM and V
X = np.matmul(inverseMatrix_M, V)
print('X: \n', X)

#value of x,y,z is
print('value of x: ', X[0,0])
print('value of y: ',  X[1,0])
print('value of z: ',  X[2,0])