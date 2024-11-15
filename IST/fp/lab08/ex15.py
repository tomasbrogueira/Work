from ex03 import Data
from ex04 import Relogio
class TimeStamp(Data, Relogio):
    def __init__(self, dat, rel):
        self._data = dat
        self._relogio = rel

    def data(self):
        return self._data

    def relogio(self):
        return self._relogio

    @staticmethod
    def eh_time_stamp(arg):
        return isinstance(arg, TimeStamp)

    def mesmo_time_stamp(self, outro_ts):
        return (self._data.mesma(outro_ts._data) and
                self._relogio.igual(outro_ts._relogio))

    def depois(self, outro_ts):
        if self._data.anterior(outro_ts._data):
            return False
        elif self._data.mesma(outro_ts._data):
            return not self._relogio.mais_cedo(outro_ts._relogio)
        return True
