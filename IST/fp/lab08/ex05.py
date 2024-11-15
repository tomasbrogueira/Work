
class ContadorLimitado:
    def __init__(self, lower_limit, upper_limit):
        if lower_limit >= upper_limit:
            raise ValueError("O limite inferior deve ser menor ou igual ao limite superior")
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit
        self.value = lower_limit

    def consulta(self):
        return self.value

    def inc(self):
        if self.value < self.upper_limit:
            self.value += 1
        return self.value

    def dec(self):
        if self.value > self.lower_limit:
            self.value -= 1
        return self.value

    def __repr__(self):
        return f"Contador de {self.lower_limit} a {self.upper_limit} (atual {self.value})"


'''
class Contador_limitado:
    def __init__(self,lim_i,lim_s):
        if lim_i >= lim_s :
            raise ValueError
        self._val = lim_i
        self._lim_i = lim_i
        self._lim_s = lim_s

    def consulta(self):
        return self._val

    def inc(self):
        self._val += 1
        if self._val >= self._lim_s :
            self._val = self._lim_s
        return self._val

    def dec(self):
        self._val -= 1
        if self._val <= self._lim_i :
            self._val = self._lim_i
        return self._val

    def __repr__(self):
        return f'Contador de {self._lim_i} a {self._lim_s} (atual {self._val})'
'''