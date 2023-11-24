import numpy as np
#make square matrics 3 x 3

M = np.array([[1,2,3], [2,3,4], [2,5,6]])

#calculate the determinant of M
D = np.linalg.det(M)
print('\t Determinant of a square matrics', '\nMatrics M: ', M, '\nDeterminent of M is D:', D)

#calculate rank of a matrics
R = np.linalg.matrix_rank(M)
print('\t Rank of a matrics', '\nR: ', R)

#trace of a matrics
N = np.array([[1,2,3], [2,3,4], [4,6,8]])
T = np.trace(N)
print('\n trace of a matrices', '\nTrace: ', T)

#inverse matrics
InverseMatrics = np.linalg.inv(M)
print('\n inverse matrics', '\nresult of Inverse Matrics of M is: ', InverseMatrics)

#initialise matrics c on inverse matrics
C = np.array([[2], [4], [7]])

X = np.matmul(InverseMatrics, C)

print('matrics X: ', X)