class piscina():
    def __init__(self,lot):
        self.__lot = lot
        self.__banhistas = {}
        self.__tarifa = 0.5
        self.__custo = 2

    def entra(self,bi,h,m):
        if bi in self.__banhistas.keys() or self.ocupacao() >= self.__lot\
                or h < 0 or h > 23 or m < 0 or m > 59:
            raise ValueError

        self.__banhistas[bi] = [h,m]
        return self.ocupacao()
    
    def sai(self,bi,h,m):
        if bi not in self.__banhistas:
            raise ValueError

        horas_totais = h-self.__banhistas[bi][0] + (m - self.__banhistas[bi][0])/60
        
        if h < 0 or h > 23 or m < 0 or m > 59 or horas_totais < 0:
            raise ValueError
        
        del self.__banhistas[bi]
        preco = self.__custo + horas_totais*self.__tarifa
        
        return f'valor a pagar : Euro {min(preco,5)}'

    def ocupacao(self):
        return len(self.__banhistas)
    
    def __repr__(self) -> str:
        return f'piscina com {self.ocupacao()} pessoas de {self.__lot}'
    
'''
uml
'''