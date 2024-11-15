''' exercício 19 '''
class Metropolitano:
    ''' comment '''
    def __init__(self):
        ''' comment '''
        self._station = [0] * 10
    def obtem_numero_viagens(self, est = None):
        ''' comment '''
        if est is None:
            return sum(self._station)
        if 0 <= est < 10:
            return self._station[est]
        return None
    def contabiliza_viagem(self, est):
        ''' comment '''
        if 0 <= est < 10:
            self._station[est] += 1

class Utente:
    ''' comment '''
    def __init__(self, nome, metro):
        ''' comment '''
        if not isinstance(nome, str):
            raise ValueError('nome not a string')
        if not isinstance(metro, Metropolitano):
            raise ValueError('metro not a Metropolitano')
        self._name = nome
        self._metro = metro
    def pede_informacoes(self):
        ''' comment '''
        print("Como vou para o IST?")
    def _valida_titulo(self):
        ''' comment '''
        print("Título Válido")
    def viaja(self, est):
        ''' comment '''
        self._valida_titulo()
        self._metro.contabiliza_viagem(est)
    def obtem_nome(self):
        ''' comment '''
        return self._name

class UtentePasse(Utente):
    ''' comment '''
    def __init__(self, nome, metro):
        ''' comment '''
        super().__init__(nome, metro)
        self._count = 0
    def _valida_titulo(self):
        ''' comment '''
        super()._valida_titulo()
        print("Válido até ao final do mês corrente")
        self._count += 1
    def obtem_numero_viagens(self):
        ''' comment '''
        return self._count
