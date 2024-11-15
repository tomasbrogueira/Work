def pertence(l,e):
    if not l :
        return False
    if l[0] == e:
        return True
    if l[0] != e:
        return pertence(l[1:],e)