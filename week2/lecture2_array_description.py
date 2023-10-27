import numpy

myArr = numpy.array(['apple', 'pineapple', 'orange', 'banana', 'mango'], dtype=str)

print('declared array: ',myArr, '\narray length: ', len(myArr))

#for loop
print('with break: ')
for x in myArr:
    if x == 'orange':
        break #break is used to stop the loop after getting specific element
    print(x)

print('\nwith continue: ')
for x in myArr:
    if x == 'orange':
        continue
    print(x)
        #continue is used to continue the loop
        # after getting specific element which will not be printed

print('\nloop with range: ', '\nmy Arr: ', myArr)
for i in range(0, len(myArr), 2):
    print(myArr[i])