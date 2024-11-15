def acrescenta(dic):
    def insere(chave,valor):
        if chave in dic:
            dic[chave].append(valor)
        else:
            dic[chave] = [valor]
        return len(dic[chave])
    return insere
