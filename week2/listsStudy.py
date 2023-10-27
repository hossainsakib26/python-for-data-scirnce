myList = [1, 32, 'sazzad', 'nakib', [1, 3], 32]

print(myList)
print(myList[3])
print(type(myList))

myList2 = [[1,2,3], [4,5,6]]

for i in range(0,2):
    for j in range(0, 3):
        print(myList2[i][j], '', end='')
    print('')

myDictionary = {
    'brand': 'Toyota',
    'model': '3d2',
    'year': '2015'
}

print(myDictionary)
print(myDictionary['brand'])