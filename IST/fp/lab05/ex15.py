def polyval(tuplo,real):
    invertido = tuplo[::-1]
    num = invertido[0]
    for i in range(1,len(invertido)):
        num += int(invertido[i])*real**i
    return num