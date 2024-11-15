''' exercício 02 '''
def binary(val):
    ''' comment '''
    if not isinstance(val, int) or val > 1:
        return 0
    if val < 0:
        return 1
    return 1 - val
