import numpy

myArr = numpy.array([7, 8, 3, 4], dtype=int)
print('my integer array: ', myArr, 'and length is: ', len(myArr))
print('sort: ', numpy.sort(myArr))

for i in range(len(myArr)-1, 0, -1):
    for j in range(i):
        print('value of j, i: ', i,j,'arr index values of j, i: ', myArr[j], myArr[i])
        if (myArr[j] > myArr[j+1]):

            temp = myArr[j]
            myArr[j] = myArr[j+1]
            myArr[j+1] = temp


print('new array is: ', myArr)
