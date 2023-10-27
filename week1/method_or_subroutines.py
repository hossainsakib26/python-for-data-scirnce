
x = float(input('input x: '))
y = float(input('input y: '))

#sum two variables using methode
def addition(a, b):
    return (a + b)

print('addition: ', addition(x,y))

#a divided by b using method
def a_devided_b(a, b):
    if b == 0:
        return 'b must be bigger than 0'
    else:
        c = (a / b)
        return c

print('a devided by b: ', a_devided_b(x, y))