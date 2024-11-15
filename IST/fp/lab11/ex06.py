def eh_primo(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True

def nao_primos(n):
    return [num for num in range(1,n+1) if not eh_primo(num)]

print(nao_primos(10))
        