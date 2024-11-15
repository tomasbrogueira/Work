class PrioqError(ValueError):
    pass

class Prioq():
    def __init__(self,n):
        self.__fila = []
        while n >= 0:
            self.__fila.append([])
            n -= 1

    def seguinte(self):
        '''
        list necessario?
        '''
        for lista in list(self.__fila):
            if not lista:
                continue
            else:
                '''
                break?
                '''
                return lista[0]
        
        return self.PrioqError()

    def comprimento(self,n):
        if n > len(self.__fila) or n < 1 :
            return -1

        return len(self.__fila[n-1])

    def coloca(self,el,n):
        if n <= self.comprimento():
            self.__fila[n-1].append(el)
    
    def elimina(self):
        indice = -1
        for lista in list(self.__fila):
            indice += 1
            
            if not lista:
                continue

            self.__fila[indice].remove(lista[0])
            break

    
    def aumenta(self):
        indice = -1
        for lista in list(self.__fila):
            indice += 1
            if not lista:
                continue
            
            if indice == 0 :
                break

            elemento = lista[0]
            self.__fila[indice].remove(elemento)
            self.__fila[indice-1].append(elemento)
            
    def vazia(self,n):
        return not self.__fila[n-1]

    def prioridades(self):
        return len(self.__fila)


def espalma(f_1,f_2):
    if not isinstance(f_1,Prioq) or not isinstance(f_2,Prioq):
        raise ValueError('argumentos invalidos')
    
    n_f = f_1

    for lista in f_2:
        n_f.append(lista)
    
    return Prioq(n_f)
