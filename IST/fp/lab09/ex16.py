''' exercício 16 '''
class Tempo:
    ''' comment '''
    def __init__(self, hora, min_):
        ''' comment '''
        if hora < 0 or min_ < 0 or min_ > 59:
            raise ValueError('tempo inválido.')
        self._value = hora, min_
    def horas(self):
        ''' comment '''
        return self._value[0]
    def minutos(self):
        ''' comment '''
        return self._value[1]
    @staticmethod
    def eh_tempo(arg):
        ''' comment '''
        return isinstance(arg, Tempo)
    def tempos_iguais(self,t_2):
        ''' comment '''
        return isinstance(t_2, Tempo) and self._value == (t_2.horas(), t_2.minutos())
    def num_minutos(self):
        ''' comment '''
        return self.horas() * 60 + self.minutos()
