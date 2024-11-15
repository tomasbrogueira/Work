def sublistas(l):
    '''pq n
    if not isintance(l,list):
        return
    '''
    if not l:
        return 0
    count = 0
    if isinstance(l[0],list):
        count += 1 + sublistas(l[0])
    count += sublistas(l[1:])
    return count