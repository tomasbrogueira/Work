def filtra_pares(x):
    t = ()
    if isinstance(x,tuple):
        for i in range(len(x)):
            if x[i] % 2 == 0 :
                t += (x[i],)
            continue
    return t