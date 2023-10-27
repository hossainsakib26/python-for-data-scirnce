import numpy

#define total elements of array
totalElements = 50

#declare an array to allocate 50 elements randomly.
myArray = numpy.empty(totalElements, int)

print('declare array with empty method: ',myArray)

#initialise an array with 10 rendom integer value
myArray2 = numpy.random.randint(-5, 5, 10, int)
print(myArray2)
print(myArray2.shape[0])

# a = numpy.array([112, 23, 0, 4, 9, 321], dtype=int)
# print(a.shape[0])

print('Now print MyArray2 using for loop: ')
for index in range(0, len(myArray2), 1):
    print('index: ', index, 'value: ', myArray2[index])

print('Now print MyArray2 using while loop: ')
indx = int(0)
while (indx < len(myArray2)):
    print('index: ', indx, 'value: ', myArray2[indx])
    indx += 1