fator = 0
inicio = 0
while fator < 9 :
    soma = fator+1
    inicio = inicio*10+soma
    fim = inicio*8 + soma
    print(f'{inicio} x 8 + {soma} = {fim}')
    fator = fator + 1