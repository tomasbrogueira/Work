def soma_cumulativa(lista):
    if lista == [] : return []
    n_lista = [lista[0]]
    for i in range(1,len(lista)):
        valor = n_lista[i-1]+lista[i]
        n_lista.append(valor)
    return n_lista
