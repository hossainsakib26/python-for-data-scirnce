print('hello world \nhello world') #\n for new line


# qs2 is done
a = float(input('input a number for a: '))
b = float(input('input a number for b: '))

def addition(x, y):
    c = (x + y)
    return c

def subtractio(x, y):
    c = x - y
    return c

def multiplication(x, y):
    return '0 is not exceptable for multiplication' if y == 0 else (x * y)
    #c = x * y
    #return round(c, 2)

def division(x, y):
    if y == 0:
        return '0 is not excepted!'
    else:
        c = x / y
        return round(c, 2)

print('result for addition: ', addition(a, b),
      '\nresult for subtractio: ', subtractio(a,b),
      '\nresult for multiplication: ', multiplication(a,b),
      '\nresult for division: ', division(a,b))