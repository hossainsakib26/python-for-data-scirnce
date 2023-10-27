import math

# a = int(input('add value for coefficient a: '))
# b = int(input('add value for coefficient b: '))
# c = int(input('add value for coefficient c: '))

a = float(input('add value for coefficient a: '))
b = float(input('add value for coefficient b: '))
c = float(input('add value for coefficient c: '))

def makeSquareValue(x):
    return x * x

def multiplication(x, y):
    return x * y

def getSqrtValue(x, y, z):
    global result #could declare result globally
    b_square = makeSquareValue(y)
    a_c_with_4 = (4 * multiplication(x, z))
    d = int((b_square - a_c_with_4))
    if d >= 0:
        return math.sqrt(b_square - a_c_with_4)
    else:
        print('minus real number never allow in square root')
    # return result

# now get the result of X1 & X2
X1 = ((-b + getSqrtValue(a, b, c)) / (2 * a))
X2 = ((-b - getSqrtValue(a, b, c)) / (2 * a))

print('result X1: ', X1, '\nresult X2: ', X2)
