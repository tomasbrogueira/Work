def soma_fn(n,fn):
    soma = 0
    cont = 1
    while cont <= n:
        soma += fn(cont)
        cont += 1
    return soma

print(soma_fn(4, lambda x: x * x))
print(soma_fn(4, lambda x: x + 1))