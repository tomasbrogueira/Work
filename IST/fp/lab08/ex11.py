import random

class Conjunto:
    def __init__(self,*e):
        self._elements = list(e)
    
    def element(self):
        if len(self._elements) == 0:
            raise ValueError('conjunto vazio')
        return random.choice(self._elements)
    
    def cardinal(self):
        return len(self._elements)
    
    def insere(self,e):
        if e not in self._elements:
            self._elements.append(e)
    
    def retira(self,e):
        if e in self._elements:
            self._elements.remove(e)

    def vazio(self):
        return not bool(self._elements)
    
    def pertence(self,e):
        return e in self._elements
    
    def elements(self):
        return tuple(self._elements)
    
    def duplica(self):
        return Conjunto(*self._elements)
    
    def subconjunto(self,c2):
        return all(e in c2._elements for e in self._elements)
    
    def uniao(self,c2):
        return Conjunto(*set(self._elements) | set(c2._elements))
    
    def intersecao(self,c2):
        return Conjunto(*set(self._elements) & set(c2._elements))
    
    def diferenca(self, c2):
        return Conjunto(*set(self._elements) - set(c2._elements))

    def __repr__(self):
        return f"{{{', '.join(map(str, self._elements))}}}"
