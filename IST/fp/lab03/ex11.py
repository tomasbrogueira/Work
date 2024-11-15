num = int(input("Escreva um inteiro\n? "))
zero = 0
while num > 0 :
    if num % 10 == 0:
        novo = num//10
        while novo % 10 == 0:
            zero = zero+1
            num = num//10
            novo = novo//10
    num = num//10
print(f'O numero tem {zero} zeros seguidos')