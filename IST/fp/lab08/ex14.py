class Unica:
    instance = None 
    def __init__(self):
        if Unica.instance is not None:
            raise ValueError("só pode existir uma instância.")
        self.__value = None

    def get_instance():
        if Unica.instance is None:
            Unica.instance = Unica()
        return Unica.instance

    def store(self, val):
        self.__value = val

    def value(self):
        return self.__value
