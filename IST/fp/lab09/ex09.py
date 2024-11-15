''' exercício 09 '''
def soma(lst):
    ''' comment '''
    if not isinstance(lst, (list, tuple)):
        raise ValueError('Argumento deve ser lista ou tuplo')
    tot = 0
    for i in lst:
        if not isinstance(i, (int, float)):
            raise ValueError('Elemento deve ser inteiro ou real')
        tot += i
    return tot
