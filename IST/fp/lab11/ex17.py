def acumula(l):
    if not isinstance(l,list):
        raise ValueError

    def soma(n):
        indice = 0
        for valor in l:
            l[indice] = valor + n
            indice += 1
        return l
    return soma
