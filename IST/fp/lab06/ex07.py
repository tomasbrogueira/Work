def seq_racaman(n):
    sequencia = []
    for i in range(n):
        if i == 0 :
            sequencia.append(0)
        elif sequencia[i-1] > i and (sequencia[:i-1:].count(sequencia[i-1]-i) == 0):
            sequencia.append(sequencia[i-1]-i)
        else:
            sequencia.append(sequencia[i-1]+i)
    return sequencia