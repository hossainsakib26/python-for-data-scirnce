import numpy as np

#initilize matrix
A = np.array([[2,5,1], [4,3,7], [1,3,2]], dtype=int)
print(A)
#now find the determinent, the trace and the inverse of matrix

#determinant of A
determinant_A = np.linalg.det(A) #linear algoridon class has a function name det which is needed to get determinant.
print('determinant value of A: ',round(determinant_A, 2))

#calculate Trace
traceA = np.trace(A)
print('Trace of A: ', traceA)

#calculate the inverse of A only applicable in square matrix
inverseA = np.linalg.inv(A)
print('Inverse value Of A: \ns', inverseA)