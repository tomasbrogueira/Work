print("Escreva um número")
num = int(input("-> "))
result = num
e = 0
final = 0
while num > 0 :
    dig = num - (num//10)*10
    final = (final*10 + dig)
    e = e+1
    num = num//10
valor = result*10**e
resultado = valor+final
print(resultado)