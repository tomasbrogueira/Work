''' exercício 06 '''
def polzeros(a__, b__, c__):
    ''' comment '''
    if not isinstance(a__, (int, float)) \
            or not isinstance(b__, (int, float)) \
            or not isinstance(c__, (int, float)):
        raise ValueError('Fatores não reais')
    zeros = b__**2 - 4 * a__ * c__
    if zeros > 0:
        return 2
    if zeros == 0:
        return 1
    return 0
