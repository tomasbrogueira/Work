def soma_n_vezes(a,b,n):
    if n == 0:
        return b
    return soma_n_vezes(a,b+a,n-1)