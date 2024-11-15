def triangulo(x,y,z):
    if x<0 or y<0 or z<0:
        return None
    if x+y <= z or x+z <= y or y+z <= x:
        return 0
    if x == y == z :
        return 1
    if x==y or x==z or y == z:
        return 2
    return 3