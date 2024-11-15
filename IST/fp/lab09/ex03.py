''' exercício 03 '''
def divisores(val):
    ''' comment '''
    if type(val, int):
        return -1
    if val < 0:
        val = -val
    div, i = 0, 2
    while i <= val // 2 :
        if val % i == 0 :
            div += 1
        i += 1
    return div
