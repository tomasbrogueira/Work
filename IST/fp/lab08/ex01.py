class Estacionamento:
    def __init__(self, lotacao_maxima):
        self._lotacao_maxima = lotacao_maxima
        self._lotacao = 0

    def entrar(self):
        if self._lotacao < self._lotacao_maxima:
            self._lotacao += 1
            return True
        return False

    def sair(self):
        if self._lotacao > 0:
            self._lotacao -= 1

    def lotacao_maxima(self):
        return self._lotacao_maxima

    def lotacao(self):
        return self._lotacao

    def __repr__(self):
        return f'Lotacao: {self._lotacao} de {self._lotacao_maxima} lugares'
