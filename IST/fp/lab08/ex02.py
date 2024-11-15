class Autocarro:
    def __init__(self,cap):
        self._cap = cap
        self._pass = 0
    
    def capacidade(self):
        return self._cap 
    
    def sai(self,pass_l):
        if pass_l > self._pass:
            self._pass = 0
        else:
            self._pass = self._pass - pass_l
    
    def entra(self,pass_e):
        if self._pass + pass_e >= self._cap :
            self._pass = self._cap
        else:
            self._pass = self._pass + pass_e

    def passageiros(self):
        return self._pass

    def __repr__(self):
        return f'Autocarro de {self._cap} lugares com {self._pass} passageiros.'