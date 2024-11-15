''' exercício 11 '''
from ex10 import horner
print('Polinómio: 4x^2 + 3x + 2')
x = float(input('x = '))
print(horner([4, 3, 2], x))
