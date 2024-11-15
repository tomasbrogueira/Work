def inverte(l):
    if not l:
        return []
    return inverte(l[1:]) + [l[0]]