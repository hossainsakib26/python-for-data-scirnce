import numpy as np
#start task 1
A = np.random.randint(0, 100, 10, int)
print('The Array A: ',A)

# index = int(0)
# while (index < len(A)):
#     print('index: ', index, '[',A[index],']')
#     index += 1

for i in range(0, len(A)):
    print(i,'',A[i])

#end task 1

#start task 2
def sumArrayElements(arr):
    r = 0
    for i in range(0, len(arr)):
        r += arr[i]
    return r

def averageValueOfArray(arr):
    r = 0
    for i in range(0, len(arr)):
        r += arr[i]
    return r/len(arr)

print('sum of array: ',sumArrayElements(A), '\naverage of array: ', averageValueOfArray(A))

#end task 2

#start task 3
def getMinMaxValinArray(arr):
    # maxValue = arr.max() #ok
    np_arr = np.array(arr)
    max_value = np.max(np_arr)
    min_value = np.min(np_arr)

    return ('max value: ', max_value, 'from index no:', np.argmax(np_arr),
            'min value: ', min_value, 'from index no: ', np.argmin(np_arr))

print(getMinMaxValinArray(A))
#end task 3

#start task 4
def ascending_reverse_sortArray(arr, is_descending = False):
    np_arr = np.array(arr)
    result = np.sort(np_arr) if (is_descending == False) else np.flip(np.sort(np_arr))
    return result

B = ascending_reverse_sortArray(A, False)
print('Ascending: ',B)
C = ascending_reverse_sortArray(A, True)
print('Descending: ', C)
#end task 4

# start task 5
#get the max
def get_max_num(arr):
    np_arr = np.array(arr)
    max_num = np_arr[0]
    for i in range(0, len(np_arr)):
        if (max_num < np_arr[i]):
            max_num = np_arr[i]
    return max_num

print('max num is: ', get_max_num(A))

#get the min
def get_min_num(arr):
    np_arr = np.array(arr)
    min_num = np_arr[0]
    for i in range(0, len(np_arr)):
        if (min_num > np_arr[i]):
            min_num = np_arr[i]
    return min_num

print('max num is: ', get_min_num(A))

#ascending sort
print('Array A: ', A)
for i in range(0, len(A)):
    for j in range(i+1, len(A)):
        if(A[i] > A[j]):
            temp = A[i]
            A[i] = A[j]
            A[j] = temp

print('ascending: ', A)
print('ascending: ', A[::-1]) # start:end:step

# End task 5

# start task 6

for i in range(0, 10, 1):
    print(i,'----',A[i],'----',B[i],'----',C[i] )

# end task 6

# start task 7



# end task 7

D = np.empty(shape=10, dtype=int )
D[0] = 10
for i in range(1, 10):
    D[i] = D[i-1] + 4
print(D)

