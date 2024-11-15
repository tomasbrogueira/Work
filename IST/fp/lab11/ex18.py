def atualiza(dicionario):
    def atualizador(chave, valor):
        antigo_valor = dicionario.get(chave)
        dicionario[chave] = valor
        return antigo_valor
    return atualizador
