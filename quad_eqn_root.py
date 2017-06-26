import math
def root_quadratic(a,b,c,x):
    D = ((b ** 2) - (4 * a * c)) / (2 * a)
    if (D > 0):
        x1 = (math.sqrt(D) - b) / (2 * a)
        return(x1)
    elif (D == 0):
        return(-b / (2 * a))
    elif (D < 0):
        D_im = -D
        x1 = complex((-b / (2 * a)),(D_im / (2 * a)))
        return(x1)
root = root_quadratic(2.15,2.5,2,'x')
print(root)
