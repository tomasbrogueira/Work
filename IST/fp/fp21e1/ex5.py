def conta_intervalo_1(l,inf,sup):
    if not l:
        return 0
    
    if l[0] >= inf and l[0] <= sup:
        return 1 + conta_intervalo_1(l[1:],inf,sup)

    return conta_intervalo_1(l[1:],inf,sup)

def conta_intervalo_2(l,inf,sup,num = 0):
    if not l:
        return num
    
    if l[0] >= inf and  l[0] <= sup:
        return conta_intervalo_2(l[1:],inf,sup,num+1)
    
    return conta_intervalo_2(l[1:],inf,sup,num)

def conta_intervalo_3(l,inf,sup):
    num = 0
    for valor in l:
        if valor >= inf and valor <= sup:
            num += 1
    
    return num

def filtra(tst,lst):
    return [x for x in [lst[0]] + filtra(tst, lst[1:]) if tst(x)] if lst else []


def conta_intervalo_4(l,inf,sup):
    return len(filtra(lambda x : x >= inf and x <= sup , l))

print(conta_intervalo_4(range(1,12),2,6))
