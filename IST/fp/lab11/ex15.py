def index(l):
    def inst(n):
        indice = 0
        for num in l:
            if n == num:
                return indice
            indice += 1
        return -1
    return inst
