def seno(x,n):
    fact = 1
    for i in range(n) and z in range(2*n+1):
        fact = fact*z
        y = ((-1)**i*(x)**(2*i+1))/(fact)
    return y