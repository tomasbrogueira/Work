from ex04 import filtra,transforma,acumula

def soma_quadrados_impares(l):
    n_l = filtra(lambda x : x % 2 ==1,l)
    quad = transforma(lambda x : x**2,n_l)
    return acumula(lambda x,y : x+y , quad)

print(soma_quadrados_impares([1, 2, 3, 4, 5, 6]))