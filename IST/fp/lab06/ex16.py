def mostra_ordenado(dic):
    l = list(dic.keys())
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
    for key in l:
        print(key,dic[key])
