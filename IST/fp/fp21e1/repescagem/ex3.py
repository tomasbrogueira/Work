def remove_vazios(lst):
    indice = 0
    for dic in list(lst):
        
        for chave in dict(dic):
            if not dic[chave]:
                del dic[chave]
        
        if not dic:
            del lst[indice]
        
        indice += 1


lst = [ { 1:[1,2], 'a':[]}, { 1.2:[] }, { 5:[8], 3:[0,0]} ]

remove_vazios(lst)

print(lst)