num = int(input("Escreva um inteiro\n? "))
final = 0
e = 0
while num > 0:
    if num % 2 == 1 :
        dig = num - (num//10)*10
        final = final + dig*10**e
        e += 1
    num = num//10
print("Resultado:", final)