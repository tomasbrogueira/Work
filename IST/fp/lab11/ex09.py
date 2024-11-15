from ex08 import lista_digitos
from ex04 import acumula

def produto_digitos(n,pred):
    '''n sei'''
    l = lista_digitos(n)
    return acumula(lambda x,y :x*y if pred(x) and pred(y) else l.remove(x),l)

def produto_digitos(n,pred):
    if n == 0:
        return 1
    if pred(n%10):
        return n%10*produto_digitos(n//10,pred)
    return produto_digitos(n//10,pred)

print(produto_digitos(12345, lambda x : x > 3))