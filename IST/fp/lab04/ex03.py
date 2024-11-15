from math import sqrt
x1 = float(input("x1 = "))
x2 = float(input("x2 = "))
x3 = float(input("x3 = "))
x4 = float(input("x4 = "))
x5 = float(input("x5 = "))
media = (x1+x2+x3+x4+x5)/5
erro = round(sqrt(((x1-media)**2+(x2-media)**2+(x3-media)**2+(x4-media)**2+(x5-media)**2)/4),8)
media_arredondada = round(media,4)
print("média =",media_arredondada,"desvio padrão =",erro)