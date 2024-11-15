'''
def n_esimo_primo(n_natural)
recebe o indicie da lista dos primos
devolve o primo
'''

'''
n godel
n_esimo_primo()**ord(letra)
'''

def n_esimo_primo(n):
    # initial prime number list
    prime_list = [2]
    # first number to test if prime
    num = 3
    # keep generating primes until we get to the nth one
    while len(prime_list) < n:

        # check if num is divisible by any prime before it
        for p in prime_list:
            # if there is no remainder dividing the number
            # then the number is not a prime
            if num % p == 0:
                # break to stop testing more numbers, we know it's not a prime
                break

        # if it is a prime, then add it to the list
        # after a for loop, else runs if the "break" command has not been given
        else:
            # append to prime list
            prime_list.append(num)

        # same optimization you had, don't check even numbers
        num += 2

    # return the last prime numb
    return prime_list[-1]

def codifica_palavra(palavra):
    num = 1
    iteracao = 0
    
    for letra in palavra:
        iteracao += 1
        num *= n_esimo_primo(iteracao)**ord(letra)
    
    return num

def descodifica_palavra(n):
    comp = 1
    while n % n_esimo_primo(comp) == 0:
        comp += 1
    
    comp -= 1
    
    palavra = ''

    for indice in range(comp):
        contador = 0
        
        while n % n_esimo_primo(indice+1) == 0:
            n = n // n_esimo_primo(indice+1)
            contador += 1
        
        palavra += chr(contador)
    
    return palavra




'''
def descodifica_palavra(n,palavra = '',vez = 1):
    if n == 1 :
        return palavra
    
    iteracao = 0

    while n % n_esimo_primo(vez) == 0:
        n = n//n_esimo_primo(vez)
        iteracao += 1
    
    letra = chr(iteracao)

    return descodifica_palavra(n,palavra + letra , vez + 1)
'''
print (codifica_palavra('brogueira'))

print(descodifica_palavra(codifica_palavra('brogueira')))