def piatorio(l_inf, l_sup, func, fprox):
    prod = 1
    while l_inf <= l_sup:
        prod *= func(l_inf)
        l_inf = fprox(l_inf)
    return prod

def fatorial(n):        
    return piatorio(1,n,lambda x : x , lambda x : x+1)
    

print(fatorial(3))