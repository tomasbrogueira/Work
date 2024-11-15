num = int(input("Escreva um inteiro positivo\n? "))
final = 0
while num > 0 :
    dig = num - (num//10)*10
    final = final*10 + dig
    num = num//10
print("O número invertido é", final)