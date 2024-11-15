def apenas_digitos_impares(n):
    if n == 0 :
        return 0
    if n % 2 == 1 :
        return (n % 10) + 10*(apenas_digitos_impares(n // 10))
    return apenas_digitos_impares(n // 10)

print(apenas_digitos_impares(1725))