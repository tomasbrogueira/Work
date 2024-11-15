print('-='*15)
print('Processador de Sequências'.upper())
print('-='*15)
print()
print('INSTRUÇÕES: Não faça a coplementar, coloque a cadeia original, \ncoloque sempre um número de bases maior ou igual ao que colocará numa das perguntas\nnão coloque "enters".\n')
esc = int(input('Primer Forward ou Reverse [1/2]? '))
n = int(input('Quantas bases? '))
if esc == 1:
    seq = input('Cadeia de DNA: ').upper()[:n]
else:
    seq = input('Cadeia de DNA: ').upper()[::-1][:n][::-1]
n_a = 0
n_c = 0
n_g = 0
n_t = 0
comp = ''
for c in range(len(seq)):
    if seq[c] == 'T':
        comp += 'A'
    elif seq[c] == 'G':
        comp += 'C'
    elif seq[c] == 'C':
        comp += 'G'
    elif seq[c] == 'A':
        comp += 'T'
for b in comp:
    if b == 'A':
        n_a += 1
    elif b == 'C':
        n_c += 1
    elif b == 'G':
        n_g += 1
    elif b == 'T':
        n_t += 1
print(f'Seq: {comp}')
print(f'#A: {n_a} \n#C: {n_c} \n#G: {n_g} \n#T: {n_t}')
print(f'%(g/c): {(n_g+n_c)/(n_a+n_c+n_g+n_t)*100:.1f}')
temp = 2*(n_a + n_t) + 4*(n_c + n_g)
print(f'Temp1: {temp}ºC, Temp2: {temp - 10}ºC')
