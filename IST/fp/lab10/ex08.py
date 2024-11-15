def subtrai(l1,l2):
    if not l2:
        return l1
    if l2[0] in l1:
        l1.remove(l2[0])
    return subtrai(l1,l2[1:])