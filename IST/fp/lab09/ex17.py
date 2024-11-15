''' exercício 17 '''
class SkiRental:
    ''' comment '''
    def __init__(self, ski, snowb, skunits, sbunits):
        ''' comment '''
        self._price = ski, snowb
        self._stock = [skunits, sbunits]
        self._equip = tuple(self._stock)
        self._use = [0, 0]
        self._reserved = [0, 0]
        self._reserves = {}
        self._sales = 0
    def preco_ski(self):
        ''' comment '''
        return self._price[0]
    def preco_snowboarsd(self):
        ''' comment '''
        return self._price[1]
    def stock(self):
        ''' comment '''
        return tuple(self._stock)
    def reserva(self, nome, skis, snowbs):
        ''' comment '''
        if skis > self._stock[0] - self._reserved[0]:
            skis = self._stock[0] - self._reserved[0]
        if snowbs > self._stock[1] - self._reserved[1]:
            snowbs = self._stock[1] - self._reserved[1]
        self._reserved[0] += skis
        self._reserved[1] += snowbs
        self._reserves[nome] = skis, snowbs, False
        return self._price[0] * skis + self._price[1] * snowbs
    def aluga(self, nome, skis, snowbs):
        ''' comment '''
        if nome not in self._reserves:
            self._reserves[nome] = 0, 0, False
        if self._reserves[nome][2]:
            return 0
        if skis < self._reserves[nome][0]:
            self._reserved[0] -= self._reserves[nome][0] - skis
        if snowbs < self._reserves[nome][1]:
            self._reserved[1] -= self._reserves[nome][1] - snowbs
        if skis > self._reserves[nome][0]:
            avail = self._stock[0] - self._reserved[0]
            if avail < skis - self._reserves[nome][0]:
                skis = self._reserves[nome][0] + avail
        if snowbs > self._reserves[nome][1]:
            avail = self._stock[1] - self._reserved[1]
            if avail < snowbs - self._reserves[nome][1]:
                skis = self._reserves[nome][1] + avail
        self._reserved[0] -= skis
        self._reserved[1] -= snowbs
        self._stock[0] += skis
        self._stock[1] += snowbs
        self._reserves[nome] = skis, snowbs, True
        self._sales += self._price[0] * skis + self._price[1] * snowbs
        return self._sales
    def cancela(self, nome):
        ''' comment '''
        if nome in self._reserves[nome]:
            self._reserved[0] -= self._reserves[nome][0]
            self._reserved[1] -= self._reserves[nome][1]
            del self._reserves[nome]
    def devolve(self, nome, skis, snowbs):
        ''' comment '''
        no_ski = no_snowb = 0
        if nome in self._reserves[nome]:
            no_ski = self._reserves[nome][0] - skis
            no_snowb = self._reserves[nome][1] - snowbs
        self._stock[0] += skis
        self._stock[1] += snowbs
        return no_ski, no_snowb
    def fecho(self):
        ''' comment '''
        skis = self._equip[0] - self._stock[0]
        snowbs = self._equip[1] - self._stock[1]
        sales = self._sales
        self._use = [0, 0]
        self._reserved = [0, 0]
        self._reserves = {}
        self._sales = 0
        return skis, snowbs, sales
    def __repr__(self):
        ''' comment '''
        return f"Ski: {self._price[0]}; Snowboard: {self._price[1]}"
