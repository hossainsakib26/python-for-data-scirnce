#import library
import math

#example of conditions
a = int(input('value a: '))

if a >= 0:
    result = math.sqrt(a)
    print('square root value for a: ', result)
else:
    print('negative value not allow because negative numbers donot have real square root.')
