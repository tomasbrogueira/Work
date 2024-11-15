def logn(x,n):
    soma = 0
    for i in range(n):
        soma = (soma+(1/(2*i+1))*((x-1)/(x+1))**(2*i+1))
    return 2*soma