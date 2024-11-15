''' exercício 15 '''
from math import nan
def piecewise(lst, val):
    ''' comment '''
    itf = iter(lst) # throw exception if not iterable
    x_n = y_n = 0
    x_0, y_0 = nan, nan
    for x_n, y_n in itf: # throw exception if not a two item element, at least
        if not isinstance(x_n, (int,float)) or not isinstance(y_n, (int,float)):
            raise ValueError('Values not real.')
        if val < x_n:
            break
        x_0, y_0 = x_n, y_n
    if x_0 == nan or val > x_n:
        return nan
    if val == x_0 :
        return y_0
    return y_0 + (val - x_0) * (y_n - y_0) / (x_n - x_0)

if __name__ == '__main__':
    print("f(3.5) =", piecewise([(0,1),(2,2),(6,3),(7,1),(9,2),(12,0)], 3.5))
    print("f(4.5) =", piecewise([(0,1),(2,2),(6,3),(7,1),(9,2),(12,0)], 4.5))
    print("f(5.5) =", piecewise([(0,1),(2,2),(6,3),(7,1),(9,2),(12,0)], 5.5))
    print("f(9.0) =", piecewise([(0,1),(2,2),(6,3),(7,1),(9,2),(12,0)], 9.0))
    print("f(0.0) =", piecewise([(0,1),(2,2),(6,3),(7,1),(9,2),(12,0)], 0.0))
    print("f(9.5) =", piecewise([(0,1),(2,2),(6,3),(7,1),(9,2),(12,0)], 9.5))
    print("f(0.5) =", piecewise([(0,1),(2,2),(6,3),(7,1),(9,2),(12,0)], 0.5))
    print("f(12.0) =", piecewise([(0,1),(2,2),(6,3),(7,1),(9,2),(12,0)], 12.0))
    print("f(13.5) =", piecewise([(0,1),(2,2),(6,3),(7,1),(9,2),(12,0)], 13.5))
    print("f(-3.5) =", piecewise([(0,1),(2,2),(6,3),(7,1),(9,2),(12,0)], -3.5))
    try:
        piecewise('abc', 3.5)
    except ValueError:
        print("Invalid value: f('abc')")
    try:
        piecewise(True, 3.5)
    except TypeError:
        print("Invalid type: f(True)")
