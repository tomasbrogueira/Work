def valor(q,j,n):
    if 0 < j < 1 and q//1 == q and n > 0 and n//1 == n : 
        return round(q*(1+j)**n,14)
    else:raise ValueError()
def duplicar(q,j):
    n = 0
    while 2 < (1+j)**n :
        n = n+1
    return n