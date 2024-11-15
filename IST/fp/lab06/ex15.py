def conta_palavras(string):
    contagem = {}
    lista = string.split()
    for palavra in lista:
        if palavra not in contagem:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    return contagem

