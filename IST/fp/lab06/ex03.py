def elemento_matriz(x,y,z):
    if y > len(x)-1 :
        raise ValueError(": elemento_matriz: indice invalido, linha",y)
    if z >= len(x[0]):
        raise ValueError(": elemento_matriz: indice invalido, coluna",z)
    return x[y][z]