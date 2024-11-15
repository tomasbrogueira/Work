from math import gcd
def cria_racional(n1,n2):
    if not isinstance(n1,int) or not isinstance(n2,int):
        raise ValueError('os números devem ser inteiros')
    if n2 == 0:
        raise ValueError('o denominador não pode ser 0')
    divisor = gcd(n1,n2)
    if n2 < 0 :
        n2 = -n2
        n1 = -n1
    return {'n':n1//divisor,'d':n2//divisor}

def escreve_racional(dic):
    return f"{dic['n']}/{dic['d']}"

def soma_racionais(dic1,dic2):
    numerador = dic1['n']*dic2['d'] + dic2['n']*dic1['d']
    denominador = dic1['d']*dic2['d']

    divisor = gcd(numerador,denominador)

    return {'n':numerador//divisor,'d':denominador//divisor}
