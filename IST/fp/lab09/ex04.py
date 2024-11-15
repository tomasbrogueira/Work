''' exercício 04 '''
def gcd(a__, b__):
    ''' comment '''
    if a__ <= 0 or b__ <= 0 :
        return 0
    mul,div,i = a__,1,2
    if a__ > b__ :
        mul = b__
    while i <= mul :
        if a__ % i == 0 and b__ % i == 0 :
            div = i
        i += 1
    return div
