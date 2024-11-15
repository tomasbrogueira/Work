def incrementa(valor):
    def incrementador(x):
        return x + valor
    return incrementador
