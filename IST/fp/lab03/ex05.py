dig = int(input("Escreva um dígito\n(-1 para terminar)\n? "))
num = dig
if num == -1 :
    print()
else:
    while dig >= 0 :
        dig = int(input("Escreva um dígito\n(-1 para terminar)\n? "))
        if dig != -1 :
            num = num*10 + dig
    print(f'O número é: {num}')


dig = int(input("Escreva um dígito\n(-1 para terminar)\n? "))
num = 0
while dig != -1:
    num = num*10 + dig 
    dig = int(input("Escreva um dígito\n(-1 para terminar)\n? "))
print(f"O número é: {num}")


inicio = int(input("Escreva um dígito\n(-1 para terminar)\n? "))
if inicio >= 0:
    second = int(input("Escreva um dígito\n(-1 para terminar)\n? "))
    if second >= 0 : 
        third = int(input("Escreva um dígito\n(-1 para terminar)\n? "))
        if third >= 0 :
            fourth = int(input("Escreva um dígito\n(-1 para terminar)\n? "))
            if fourth >= 0 :
                fifth = int(input("Escreva um dígito\n(-1 para terminar)\n? "))
                if fifth >= 0 :
                    print("O número é:",inicio*10**4+second*10**3+third*10**2+fourth*10**1+fifth)
                else:
                    print("O número é:", inicio*10**3+second*10**2+third*10**1+fourth)
            else:
                print("O número é:",inicio*10**2+second*10**1+third)
        else:
            print("O número é:",inicio*10**1+second)
    else:
        print("O número é:",inicio)