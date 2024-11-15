def soma_els_atomicos(tup):
    if not tup:
        return 0
    if isinstance(tup[0],int or float):
        return tup[0] + soma_els_atomicos(tup[1:])
    return soma_els_atomicos(tup[0]) + soma_els_atomicos(tup[1:])