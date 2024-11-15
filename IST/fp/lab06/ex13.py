def resumo_fp(notas_dict):
    negas,total,notas_aug = 0,0,0
    for nota in notas_dict:
        if nota < 10:
            negas += len(notas_dict[nota])
        else:
            notas_aug += nota*len(notas_dict[nota])
        total += len(notas_dict[nota])
    media = notas_aug/total
    return (media,negas)