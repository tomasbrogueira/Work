class Vetor3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def valor_x(self):
        return self.x

    def valor_y(self):
        return self.y
    
    def valor_z(self):
        return self.z

    def nulo(self):
        return self.x == 0 and self.y == 0 and self.z == 0

    def iguais(self, outro_vetor):
        return self.x == outro_vetor.valor_x() \
            and self.y == outro_vetor.valor_y() \
                and self.z == outro_vetor.valor_z()

    def __repr__(self) -> tuple:
        return (self.x,self.y,self.z)

    def __add__(self,v2):
        return (self.x+v2.x,self.y+v2.y,self.z+v2.z)

    def produto_escalar(self,v2):
        return self.x * v2.x + self.y * v2.y + self.z + v2.z
    
    def norma(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    