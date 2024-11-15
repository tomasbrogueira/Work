def segment(int):
    if len(int) != 2 or int[0] > int[1] or not isinstance(int,list):
        raise ValueError

    def atualiz(n):
        if n > int[0] and n< int[1] :
            return int
        if n < int [0]:
            int[0] = n
            return int
        int[1] = n
        return int
    return atualiz
