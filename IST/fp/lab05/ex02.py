def explode(x):
    t = ()
    if x//1 == x : 
        for i in str(x):
            y = int(i)
            t += (y,)
        return t
    raise ValueError(":explode: argumento não inteiro")