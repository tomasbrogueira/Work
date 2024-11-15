print("Escreva um numero para eu escrever a tabuada da multiplicação")
num = int(input("Num -> "))
e = 1
while e <= 10 :
    dig = num*e
    print(f"{num} x {e} = {dig}")
    e += 1



    num = int(input("Escreva um inteiro positivo\n? "))
final = 0
e = 0
while num > 0 :
    dig = num - (num//10)*10
    final = (final*10 + dig)*10**e
    num = num//10
print("O número invertido é", final)