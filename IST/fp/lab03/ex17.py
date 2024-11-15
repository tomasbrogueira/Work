def bissexto(x):
    if (x % 4 == 0) and ((x % 100 != 0) or (x % 400 == 0)) :
        return True
    return False
def dia_mes(y,x):
    if y == ("jan" or "mar" or "mai" or "jul" or "ago" or "out" or "dez") :
        return 31
    if y == ("abr" or "jun" or "set" or "nov"):
        return 30
    if (bissexto(x) == True) and y == "fev" :
        return 29
    return ValueError("Mês não existe")

