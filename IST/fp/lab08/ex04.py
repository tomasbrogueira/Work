class Relogio:
    def __init__(self, horas, minutos, segundos):
        self.horas = horas
        self.minutos = minutos
        self.segundos = segundos

    def obter_horas(self):
        return self.horas

    def obter_minutos(self):
        return self.minutos

    def obter_segundos(self):
        return self.segundos

    def igual(self, outro_relogio):
        return (self.horas == outro_relogio.horas and
                self.minutos == outro_relogio.minutos and
                self.segundos == outro_relogio.segundos)

    def mais_cedo(self, outro_relogio):
        if self.horas < outro_relogio.horas:
            return True
        elif self.horas == outro_relogio.horas:
            if self.minutos < outro_relogio.minutos:
                return True
            elif self.minutos == outro_relogio.minutos:
                return self.segundos < outro_relogio.segundos
        return False

    def __repr__(self):
        return f"{self.horas}:{self.minutos}:{self.segundos}"





'''
class Relogio:
    def __init__(self,horas,min,seg):
        self._horas = horas
        self._min = min
        self._seg = seg

    def obter_horas(self):
        return self._horas

    def obter_min(self):
        return self._min

    def obter_seg(self):
        return self._seg

    def igual(self,horas,min,seg):
        if self._horas == horas and self._min == min \
            and self._seg == seg:
            return True
        return False

    def mais_cedo(self,horas,min,seg):
        r1 = [self._horas,self._min,self._seg]
        r2 = [horas,min,seg]
        for tempo in r2:
            if r1[tempo] < r2[tempo]:
                return True
        return False
    
    def __repr__(self):
        return f"{self._horas:02}:{self._min:02}:{self._seg:02}"
'''