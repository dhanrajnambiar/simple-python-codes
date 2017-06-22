
def nth_root(x_float,n):
    tolerance = .001
    step = .0001
    guess = 0.0
    neg_flag = False
    if (x_float < 0):
        neg_flag = True
        x_float = 0 - x_float
    while (abs(guess ** n - x_float) > tolerance):
        guess += step
    if (neg_flag):
        print('The '+ str(n) + 'th root of ' + str(x_float) + ' is: i ' + str(guess))
    else:
        print('The '+ str(n) + 'th root of ' + str(x_float) + ' is: ' + str(guess))
a = float(input('Enter number\n'))
b = int(input('Enter the root factor\n'))
nth_root(a,b)

