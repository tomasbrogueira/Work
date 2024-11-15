def codifica(x):
    pares = ()
    impares = ()
    for i in str(x) :
        if x.index(i) % 2 == 0 :
            pares.append(x[i])
        else :
            impares.append(x[i])
    return pares + impares

