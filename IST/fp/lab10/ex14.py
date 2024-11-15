from ex13 import numero_digitos
def eh_capicua(n):
    if n < 0:
        raise ValueError("n deve ser um número inteiro positivo")
    if n < 10:
        return True
    if (n % 10 != n // 10 ** (numero_digitos(n) - 1)) :
        return False
    return eh_capicua(n % 10 ** (numero_digitos(n) - 1) // 10)
