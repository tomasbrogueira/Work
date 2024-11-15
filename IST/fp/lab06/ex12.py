def baralho():
    naipe = ['espadas','copas','ouros','paus']
    valores = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    carta = {'np' : '' , 'vlr' : ''}
    todas = []
    for val in valores:
        for tipo in naipe:
            carta['np'] = tipo
            carta['vlr'] = val
            todas.append(carta)
    return todas

def baralha(baralho):
    '''muito chato'''