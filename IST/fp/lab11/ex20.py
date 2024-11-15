def substitui(dicionario):
    def substituidor(chave_antiga, chave_nova):
        valor = dicionario.get(chave_antiga)
        if valor is not None:
            dicionario[chave_nova] = valor
            del dicionario[chave_antiga]
            return valor
    return substituidor
