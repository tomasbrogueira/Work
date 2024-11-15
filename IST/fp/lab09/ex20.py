''' exercício 20 '''
from math import sqrt
def roots(a__, b__, c__):
    ''' comment '''
    if b__**2 < 4 * a__ * c__:
        return ()
    x__ = sqrt(b__**2 - 4 * a__ * c__)
    return (-b__+x__)/(2*a__), (-b__-x__)/(2*a__)
