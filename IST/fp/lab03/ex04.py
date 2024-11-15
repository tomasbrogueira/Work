horas_n = int(input("horas de trabalho: "))
sal_hora = int(input("salário/hora: "))
if horas_n <= 40 :
    sal = horas_n*sal_hora
    print("pagar",sal )
if horas_n > 40 :
    horas_ext = horas_n-40
    sal = 40*sal_hora+2*sal_hora*horas_ext
    print("pagar",sal )
