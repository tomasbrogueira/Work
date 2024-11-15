def filtra(tst,lst):
    return [x for x in [lst[0]] + filtra(tst, lst[1:]) if tst(x)] if lst else []
    
    if not lst:
        return []
    return [lst[0]] if tst(lst[0]) else [] + filtra(tst,lst[1:])
    
    return [e for e in lst if tst(e)]

def transforma(fn,lst):
    if not lst:
        return []
    return [fn(lst[0])] + transforma(fn,lst[1:])

def acumula(fn,lst):
    if not lst:
        return None
    if len(lst) == 1:
        return lst[0]
    return fn(lst[0], acumula(fn, lst[1:]))
