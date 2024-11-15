''' exercício 10 '''
def horner(pol, val, res=0) :
    ''' comment '''
    if not pol:
        return res
    return horner(pol[1:], val, res * val + pol[0])
