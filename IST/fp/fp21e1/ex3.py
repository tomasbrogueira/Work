d = { 1:[1,2,3], 2:[2,3,4], 3:[3,4,5], 4:[4,5,6], 5:[5,6,7] }

def remove_dict_maiores(dic,n):
    for chave in list(dic.keys()):
        for valor in list(dic[chave]):
            if valor > n :
                dic[chave].remove(valor)
        if not dic[chave]:
            del dic[chave]

remove_dict_maiores(d, 3)
print(d)
            

