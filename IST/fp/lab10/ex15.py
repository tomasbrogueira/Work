def espelho(n,esp=0):
    if n == 0:
        return esp
    esp = esp*10 + n%10
    return espelho(n//10,esp)