x = int(input("Nota ? "))
posit,neg = 0,0
while x >= 0 :
    if x >= 10:
        posit += 1
    else:
        neg +=1
    x = int(input("Nota ? "))
percent = (posit/(posit+neg))*100
print(posit,"positivas",percent,"%")

    

