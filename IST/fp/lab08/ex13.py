class Relogio:
    def __init__(self, h, m, s):
        self.horas = h
        self.minutos = m
        self.segundos = s
    
    def get_horas(self):
        return self.horas
    
    def get_minutos(self):
        return self.minutos
    
    def get_segundos(self):
        return self.segundos
    
    @classmethod
    def eh_relogio(cls, arg):
        return isinstance(arg, cls)
    
    def eh_meia_noite(self):
        return self.horas == 0 and self.minutos == 0 and self.segundos == 0
    
    def eh_meio_dia(self):
        return self.horas == 12 and self.minutos == 0 and self.segundos == 0
    
    def mesmas_horas(self, outro_relogio):
        return self.horas == outro_relogio.horas and self.minutos == outro_relogio.minutos and self.segundos == outro_relogio.segundos
    
    def __str__(self):
        return f"{self.horas:02}:{self.minutos:02}:{self.segundos:02}"
    
    def __repr__(self):
        return f"{self.horas}:{self.minutos}:{self.segundos}"
    
    def antes(self, outro_relogio):
        if self.horas < outro_relogio.horas:
            return True
        elif self.horas == outro_relogio.horas and self.minutos < outro_relogio.minutos:
            return True
        elif self.horas == outro_relogio.horas and self.minutos == outro_relogio.minutos and self.segundos < outro_relogio.segundos:
            return True
        else:
            return False
    
    def depois(self, outro_relogio):
        if self.horas > outro_relogio.horas:
            return True
        elif self.horas == outro_relogio.horas and self.minutos > outro_relogio.minutos:
            return True
        elif self.horas == outro_relogio.horas and self.minutos == outro_relogio.minutos and self.segundos > outro_relogio.segundos:
            return True
        else:
            return False
    
    def diferenca(self, outro_relogio):
        if self.depois(outro_relogio):
            segundos1 = self.horas * 3600 + self.minutos * 60 + self.segundos
            segundos2 = outro_relogio.horas * 3600 + outro_relogio.minutos * 60 + outro_relogio.segundos
            return segundos1 - segundos2
        else:
            raise ValueError("diferenca: primeiro arg posterior ao segundo")


