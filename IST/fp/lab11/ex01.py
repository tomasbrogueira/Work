def somatorio(l_inf, l_sup, calc_termo, prox):
    soma = 0
    while l_inf <= l_sup:
        soma = soma + calc_termo(l_inf)
        l_inf = prox(l_inf)
    return soma

print(somatorio(9, 21, lambda x : x * x, lambda x : x + 3))
print(somatorio(4, 6, lambda x: x, lambda x: x + 1))
print(somatorio(5, 10, lambda x: x * x, lambda x: x + 5))
print(somatorio(1, 1, lambda x: somatorio(1, x, lambda x: x, lambda x: x+1), lambda x: x+1))