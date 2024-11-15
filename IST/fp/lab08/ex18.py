class Numero:
    def __init__(self):
        self._valor = 0

    def obter(self):
        return self._valor

    def alterar(self,n2):
        self._valor = n2

    def __str__(self) -> str:
        return str(self._valor)
    
    def __eq__(self, n2: object) -> bool:
        return self._valor == n2._valor

class NumeroComMemoria(Numero):
    def __init__(self):
        super().__init__()
        self._valores_ant = []

    def alterar(self, n2):
        self._valores_ant.append(self._valor)
        super().alterar(self,n2)

    def desfazer(self):
        self._valor = self._valores_ant[-1]
        self._valores_ant.append(self._valor)

    def anterior(self):
        if not self._valores_ant:
            return self._valor

        return self._valores_ant[-1]
        