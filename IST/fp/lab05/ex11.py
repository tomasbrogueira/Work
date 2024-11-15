def lista_codigos(x):
    t = ()
    for i in str(x):
        t = t + (ord(i),)
    return t
