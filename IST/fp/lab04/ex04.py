x = int(input("Escreva um número de segundos\n(um número negativo para terminar)\n? "))
while x >= 0:
    y = round(x/(3600*24),8)
    print("O número de dias correspondente é",y)
    x = int(input("Escreva um número de segundos\n(um número negativo para terminar)\n? "))