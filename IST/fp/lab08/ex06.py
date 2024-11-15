class CartaoTelefonico:
    def  __init__(self,tarif):
        self.tarif = tarif
        self.custo = 0
        self._chamada = 0

    def chamada(self,key,dur):
        if key not in self.tarif or dur <= 0:
            raise ValueError
        self.custo += self.tarif[key]*dur
        self._chamada += 1

    def consulta_custo(self):
        return self.custo
    
    def consulta_chamadas(self):
        return self._chamada
    
    def __repr__(self):
        return f'Despesa de {self.consulta_custo} céntimos em {self.consulta_chamadas} chamadas'