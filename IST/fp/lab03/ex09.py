num = int(input("Escreva um inteiro positivo\n? "))
new_num = 0
while num > 0 :
    dig = num - (num//10)*10
    new_num = new_num + dig
    num = num//10
print("A soma dos dígitos é",new_num)