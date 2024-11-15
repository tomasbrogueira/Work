def expon(x,n):
    y = 1
    fact = 1
    for i in range(1,n):
        fact = fact*i
        y = y+(x**i)/fact
    return y
