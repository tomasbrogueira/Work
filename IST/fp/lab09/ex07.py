''' exercício 07 '''
from ex06 import polzeros
print('Cálculo do número de zeros reais de um polinómio de grau 2.')
a__ = float(input('termo ao quadrado (a) ? '))
b__ = float(input('termo linear (b) ? '))
c__ = float(input('termo independente (c) ? '))
sol = ('nenhum zero.', 'um zero duplo.', 'dois zeros.')
print('O polinómio tem', sol[polzeros(a__, b__, c__)])
