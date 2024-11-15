def reconhece(str):
    value = False
    for x in str:
        if x.isdigit():value = True
        if value and not x.isdigit():return False
    return True


def reconhece(x):
    letras = (A,B,C,D)
    num = (1,2,3,4)
    for i in str(x):