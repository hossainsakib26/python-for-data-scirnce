import numpy

myArr = numpy.array([1,2,4,7,2,14,10,1,2], dtype=int)
print('my integer array: ', myArr, 'and length is: ', len(myArr))

for i in range(0, len(myArr)):
    print(i, '=', myArr[i]) #displaing values against index

maxVal = myArr[0] #consider the first value of array as a max value

for i in range(1, len(myArr), 1): #use range for counting from 1
    if maxVal < myArr[i]:
        maxVal = myArr[i]

print('max value is: ', maxVal)