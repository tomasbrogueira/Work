valor = float(input("Escreva uma quantia ? "))
recebido = valor*100
cent = recebido - (recebido//100)*100
euros = valor//1
cinquenta = 0
vinte = 0
dez = 0
cinco = 0
dois = 0
um = 0
if cent > 0 :
    cinquenta = cent//50
    cent = cent-cinquenta*50
    if cent > 0 :
        vinte = cent//20
        cent = cent-vinte*20
        if cent > 0 :
            dez = cent//10
            cent = cent-dez*10
            if cent > 0 :
                cinco = cent//5
                cent = cent-cinco*5
                if cent > 0 :
                    dois = cent//2
                    cent = cent-dois*2
                    if cent > 0 :
                        um = 1
x = 0
y = 0
z = 0
w = 0
u = 0
uno = 0
if euros > 0 :
    x = euros//50
    euros = euros-x*50
    if euros > 0 :
        y = euros//20
        euros = euros-y*20
        if euros > 0 :
            z = euros//10
            euros = euros-z*10
            if euros > 0 :
                w = euros//5
                euros = euros-w*5
                if euros > 0 :
                    u = euros//2
                    euros = euros-u*2
                    if euros > 0 :
                        uno = 1
print(f'{x} * 50 €')
print(f'{y} * 20 €')
print(f'{z} * 10 €')
print(f'{w} * 5 €')
print(f'{u} * 2 €')
print(f'{uno} * 1 €')
print(f'{cinquenta} * 50 cênt')
print(f'{vinte} * 20 cênt')
print(f'{dez} * 10 cênt')
print(f'{cinco} * 5 cênt')
print(f'{dois} * 2 cênt')
print(f'{um} * 1 cênt')