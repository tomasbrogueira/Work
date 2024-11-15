def horner(tuplo,real):
    num = 0
    for i in range(len(tuplo)+1):
        num = real*(tuplo[i] + num)
    return num
