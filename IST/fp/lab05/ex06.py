def num_para_seq_cod(x):
    if not isinstance(x,int) or (x<= 0):
        raise ValueError
    t = ()
    for i in str(x):
        if int(i) % 2 == 0 :
            if int(i) != 8 :
                 num = int(i) + 2
            else :
                num = 0
            t += (num,)
        else :
            if int(i) != 1:
                num = int(i) - 2
            else:
                num = 9
            t += (num,)
    return t

    