
def bissecao(f,a,b,n,feps,neps):
    n = 100
    i = 1
    while i <= n and feps > 1e-6 and neps > 1e-6 :
        c = f((a+b)/2)
        if a < 0 :
            b = c
        else:
            a = c
        i += 1
        feps = c
        neps = a-b
    return (c,n)