''' exercício 08 '''
def printn(num, base) :
    ''' comment '''
    tab = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base < 0 or base > 35:
        raise ValueError('Invalid base (2 to 35)')
    out = ''
    res = int(num // base)
    if res != 0:
        out += printn(res, base)
    out += tab[num % base]
    return out
