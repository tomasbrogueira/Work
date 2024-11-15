def implode(x):
    if isinstance(x,tuple):
        num = 0
        i = 0
        while i != range(len(x)):
            if isinstance(x[i],int):
                num = num*10 + x[i]
            else:
                 raise ValueError(":implode: argumento não inteiro")
            i += 1
        return num
#nao funciona
def implode(x):
    if isinstance(x,tuple):
        num = 0
        for i in range(len(x)):
            if isinstance(x[i],int):
                num = num*10 + x[i]
            else:
                 raise ValueError(":implode: argumento não inteiro")
        return num
