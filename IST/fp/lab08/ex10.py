class Automovel:
    def __init__(self,cap,comb,autono):
        if cap <= 0 or comb < 0 or autono <= 0:
            raise ValueError
        self.combust = comb
        self.cap = cap
        self.auto = autono
        self.autonom = int((self.combust/self.auto*100)//1)

    def combustivel(self):
        return self.combust
    
    def capacidade(self):
        return self.cap
    
    def autonomia(self):
        return self.autonom
    
    def abastece(self,n_litros):
        if self.combust + n_litros > self.cap or n_litros < 0:
            raise ValueError
        else:
            self.combust += n_litros
            self.autonom = int((self.combust/self.auto*100)//1)
        return f'{self.autonom} Km até abastecimento'
    
    def percorre(self,n_km):
        if self.autonom < n_km:
            raise ValueError('Não tem autonomia para esta viagem')
        elif self.combust < n_km / self.auto:
            raise ValueError('Não tem combustível suficiente para esta viagem')
        self.combust -= n_km / self.auto
        self.autonom -= n_km
        return f'{self.autonom} Km até abastecimento'

'''
    porque nao basta:
     def abastece(self,n_litros):
        if self.combust + n_litros > self.cap or n_litros < 0:
            raise ValueError
        else:
            self.combust += n_litros
        return f'{self.autonom} Km até abastecimento'
    '''

