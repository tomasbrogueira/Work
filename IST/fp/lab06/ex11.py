def agrupa_por_chave(lista):
    dic = {}
    for i in lista:
        if i[0] not in dic:
            dic[i[0]] = [i[1]]
        else:
            dic[i[0]].append(i[1])
    return dic