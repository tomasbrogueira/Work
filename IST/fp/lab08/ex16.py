class Vetor:
    def __init__(self,x,y):
        self._abcissa = x
        self._ordenada = y

    def abcissa(self):
        return self._abcissa

    def ordenada(self):
        return self._ordenada

    def nulo(self):
        return self._abcissa == 0 and self._ordenada == 0

    def iguais(self,v2):
        return self._abcissa == v2._abcissa and self._ordenada == v2._ordenada

    def produto_escalar(self,v2):
        return self._abcissa * v2._abcissa + self._ordenada * v2._ordenada