def parte(lst, num):
    def aux(lst, num, menores, maiores):
        if not lst:
            return [menores, maiores]
        elif lst[0] < num:
            menores.append(lst[0])
            return aux(lst[1:], num, menores, maiores)
        else:
            maiores.append(lst[0])
            return aux(lst[1:], num, menores, maiores)
    return aux(lst, num, [], [])
