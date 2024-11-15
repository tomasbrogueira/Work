from ex04 import filtra, transforma, acumula
from ex08 import lista_digitos

def apenas_digitos_impares(n):
    return acumula(lambda x,y:x*10+y,filtra(lambda x: x%2 ==1,lista_digitos(n)))

print(apenas_digitos_impares(1234567890))
