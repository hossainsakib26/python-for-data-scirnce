num = 3.14
print(type(num))

t = True
f = False

print('or: ',(t or f), '\nand: ',(t and f))

myTxt = 'Hello Vodais'
print('text is: ', myTxt, 'and type is', type(myTxt))

#string can be treated as array
myTxt2 = 'hello big man'
#get specific position's character
print('0th place: ', myTxt2[0], 'and 3rd place: ', myTxt2[3], '\nwhole text is: ', myTxt2)

#get specific position's character using riverse counter
print('5th place: ', myTxt2[-5], 'and 3rd place: ', myTxt2[-3], '\nwhole text is: ', myTxt2)

#slice the string
newText = myTxt2[3: 10]
print(newText)

#concatination
newText2 = 'by sazzad'
print(myTxt + ' ' + newText2)

newPrint = "hello\n\'world'" #example of quation mark.
print(newPrint)

#character encoding system
print('char: ',chr(65), 'and ord: ',ord('A'))

#converting datatypes
a = 5.55
print('value of a:', a,'type of a',type(a))
b = int(a)
print('int(a) will be integer: ',b, 'type: ',type(b))
string_b = str(b)
print('str(b): ', string_b, 'type is: ',type(string_b))