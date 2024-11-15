def mais_antigo(l):
    antigo = 2022
    for livro in l:
        if livro['ano'] < antigo:
            antigo = livro['ano']
            titulo = livro['titulo']
    return titulo
    