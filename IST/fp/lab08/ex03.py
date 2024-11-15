class Data:
    def __init__(self, dia, mes, ano):
        self._dia = dia
        self._mes = mes
        self._ano = ano

    def dia(self):
        return self._dia

    def mes(self):
        return self._mes

    def ano(self):
        return self._ano

    def mesma(self, data):
        return (self._dia == data._dia) and (self._mes == data._mes) and (self._ano == data._ano)

    def anterior(self, data):
        if self._ano < data._ano:
            return True
        elif self._ano > data._ano:
            return False
        else:
            if self._mes < data._mes:
                return True
            elif self._mes > data._mes:
                return False
            else:
                return self._dia < data._dia

    def idade(self, data_nascimento):
        if self.anterior(data_nascimento):
            raise ValueError("idade: a pessoa ainda não nasceu")

        idade = self._ano - data_nascimento._ano
        if self._mes < data_nascimento._mes:
            idade -= 1
        elif self._mes == data_nascimento._mes:
            if self._dia < data_nascimento._dia:
                idade -= 1
        return idade

    def __repr__(self):
        era = ""
        if self._ano < 0:
            era = " AC"
            ano_str = str(abs(self._ano)).zfill(4)
        else:
            ano_str = str(self._ano).zfill(4)
        return f"{str(self._dia).zfill(2)}/{str(self._mes).zfill(2)}/{ano_str}{era}"
