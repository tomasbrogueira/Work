from math import pi
def area_circulo(r):
    if r > 0:
        return (pi*r**2)
    return 0
def area_coroa(r1,r2):
    if r2 > r1 :
        return area_circulo(r2)-area_circulo(r1)
    raise ValueError("r1 > r2")