class Id:
    # Usamos uma lista para armazenar as instâncias da classe
    instances = []

    def __init__(self, nome_):
        self.nome_ = nome_
        self.ident_ = len(Id.instances) + 1
        Id.instances.append(self)

    def nome(self):
        return self.nome_

    def ident(self):
        return self.ident_

    def __str__(self):
        return f"{self.ident_}: {self.nome_}"

    @classmethod
    def ultimo(cls):
        return cls.instances[-1].ident_

    @classmethod
    def procura(cls, nome_):
        for i in cls.instances:
            if i.nome_ == nome_:
                return i.ident_
        return None

    @classmethod
    def id(cls, ident_):
        for i in cls.instances:
            if i.ident_ == ident_:
                return i
        return None

    @classmethod
    def ids(cls, ident_):
        try:
            return cls.instances[ident_ - 1]
        except IndexError:
            raise IndexError("list index out of range")


'''
class Id:
    ultimo_id = 0
    instancias = {}

    def __init__(self, nome):
        self._nome = nome
        self.id = Id.ultimo_id + 1
        Id.ultimo_id = self.id
        Id.instancias[self.id] = self

    def get_nome(self):
        return self._nome

    def ident(self):
        return self.id

    def __str__(self):
        return f'{self.id}: {self._nome}'

    @classmethod
    def ultimo(cls):
        return cls.ultimo_id

    @classmethod
    def procura(cls, nome):
        for id, instancia in cls.instancias.items():
            if instancia._nome == nome:
                return id
        return None

    @classmethod
    def id(cls, id):
        if id in cls.instancias:
            return cls.instancias[id]
        return None

    @classmethod
    def ids(cls, id):
        if id > cls.ultimo_id:
            raise IndexError('list index out of range')
        return cls.instancias[id]
'''

'''
class Id:
    ultimo_id = 0
    combos = {}

    def __init__(self,nome):
        self._nome = nome
        self._ident = Id.ultimo_id + 1
        Id.combos[self._ident] = self._nome

    def nome(self):
        return self._nome
    
    def ident(self):
        return self._ident

    @classmethod
    def ids(cls):
        return Id.combos.keys()

    def __repr__(self,ident):
        return f'{ident}: {Id.combos[ident]}'
'''

'''
class Id:
    def __init__(self,nome):
        self._nome = nome
        self.id = 1
    
    def nome(self):
        return self._nome
    
    def ident(self):
        return self.id
    
    def ids(self,ident):


    def __repr__(self):
        return f'{self.id}: {self._nome}'
'''