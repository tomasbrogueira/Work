def numero_digitos(n):
    if n // 10 == 0:
        return 1
    return 1+numero_digitos(n/10)

def numero_digitos2(n,dig = 1):
    if n // 10 == 0:
        return dig
    return numero_digitos2(n/10,dig+1)

def numero_digitos3(n):
    dig = 0
    while n != 0:
        dig += 1
        n = n//10
    return dig