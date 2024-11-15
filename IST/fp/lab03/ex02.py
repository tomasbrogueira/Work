second = int(input("Escreva o número de segundos "))
days = second//(24*3600)
second = second%(24*3600)
hours = second//3600
second = second%3600
minut = second//60
second = second%60
print("dias:",days,"horas:",hours,"mins:",minut,"segs:",second)
