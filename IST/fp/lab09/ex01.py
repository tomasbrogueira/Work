''' exercício 01 '''
def nand(in1, in2):
    ''' comment '''
    if not isinstance(in1, bool) or not isinstance(in2, bool):
        return False
    return not (in1 and in2)
