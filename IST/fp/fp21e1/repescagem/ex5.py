def tuplo_quadrados_maiores(l,n):
    if not l:
        return ()

    if l[0]**2 > n:
        '''
        pq n funciona tuple(l[0])?
        '''
        return (l[0],) + tuplo_quadrados_maiores(l[1:],n)
    
    return tuplo_quadrados_maiores(l[1:],n)
'''
print(tuplo_quadrados_maiores([54, 3.5, 12, 8., 14], 100))
print( tuplo_quadrados_maiores([54, 3.5, 12, 8., 14], 1000)
)
'''

def tuplo_quadrados_maiores_2(l,n,tuplo = ()):
    if not l:
        return tuplo
    
    if l[0]**2 > n:
        return tuplo_quadrados_maiores_2(l[1:],n,tuplo + (l[0],))
    
    return tuplo_quadrados_maiores_2(l[1:],n,tuplo)

'''
print(tuplo_quadrados_maiores_2([54, 3.5, 12, 8., 14], 100))
print( tuplo_quadrados_maiores_2([54, 3.5, 12, 8., 14], 1000)
)
'''

def tuplo_quadrados_maiores_3(l,n):
    t_final = ()

    for elemento in l:
        if elemento**2 > n :
            '''
            ha outra maneira de adicionar elementos a tuplos? .append()?
            '''
            t_final += (elemento,)
    
    return t_final

'''
print(tuplo_quadrados_maiores_3([54, 3.5, 12, 8., 14], 100))
print( tuplo_quadrados_maiores_3([54, 3.5, 12, 8., 14], 1000)
)
'''
from math import sqrt

# nao funciona :(

def tuplo_quadrados_maiores_4(l,n):
    return transforma(lambda x : sqrt(x),filtra(lambda x : x > n ,transforma(lambda x : x**2,l)))


print(tuplo_quadrados_maiores_4([54, 3.5, 12, 8., 14], 100))
print( tuplo_quadrados_maiores_4([54, 3.5, 12, 8., 14], 1000)
)








def filtra(tst,lst):
    if not lst:
        return []
    return [x for x in lst if tst(x)]

    return [x for x in [lst[0]] + filtra(tst, lst[1:]) if tst(x)] if lst else []
    
    if not lst:
        return []
    return [lst[0]] if tst(lst[0]) else [] + filtra(tst,lst[1:])
    
    return [e for e in lst if tst(e)]

def transforma(fn,lst):
    if not lst:
        return []
    return [fn(lst[0])] + transforma(fn,lst[1:])

def acumula(fn,lst):
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    return fn(lst[0], acumula(fn, lst[1:]))
