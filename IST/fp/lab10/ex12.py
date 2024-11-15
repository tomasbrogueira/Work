def quadrado(n):
    if n == 1 :
        return 1
    

def quadrado3(n):
    quadrado= 0
    for i in range(n):
        if i % 2 == 1:
            quadrado += i
    return quadrado