#returns sum of area of polygon and square of its perimeter
from math import *
def area_poly(n,s):
    return(0.25 * n * (s ** 2)) / (tan(pi / n))
def polysum(n,s):
    x = area_poly(n,s) + ((n * s) ** 2)
    sum_formatd = float(format(x,'.4f')) #format fractional part length to 4 positions
    return(sum_formatd)
print(polysum(5,3))
