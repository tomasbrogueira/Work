# Recursão: por operações adiadas, pela cauda

![image](RecursionInPython.jpg)

Nos exercícios desta aula não pode utilizar a atribuição nem os ciclos `while`
e `for`.

## ex01
Escreva a função recursiva `apenas_digitos_impares` que recebe um número inteiro
não negativo `n`, e devolve um inteiro composto apenas pelos dígitos ímpares de
`n`.
Se `n` não tiver dígitos ímpares, a função deve devolver zero.
Não pode usar cadeias de caracteres. Por exemplo,
```
>>> apenas_digitos_impares(468)
0
>>> apenas_digitos_impares(12426374856)
1375
```

## ex02
Escreva a função recursiva `junta_ordenadas` que recebe como argumentos
duas listas ordenadas por ordem crescente e devolve uma lista também
ordenada com os elementos das duas listas. Não é necessário validar os
argumentos da sua função. Por exemplo,
```
>>> junta_ordenadas([2, 5, 90], [3, 5, 6, 12])
[2, 3, 5, 5, 6, 12, 90]
```

## ex03
Escreva a função recursiva `sublistas` que recebe uma lista, e tem como
valor o número total de sublistas que esta contém. Por exemplo,
```
>>> sublistas([[1], 2, [3]])
2
>>> sublistas([[[[[1]]]]])
4
>>> sublistas(['a', [2, 3, [[[1]], 6, 7], 'b']])
4
```

## ex04
Escreva a função recursiva `soma_n_vezes` que recebe três números inteiros,
`a`, `b` e `n`, e que devolve o valor de somar `n` vezes `a` a `b`, ou seja, `b + a + a + ... + a`, `n` vezes. A sua função não pode usar a operação de multiplicação.
Por exemplo,
```
>>> soma_n_vezes(3, 2, 5)
17
```

## ex05
Escreva a função recursiva `soma_els_atomicos` que recebe como argumento um tuplo, cujos elementos podem ser outros tuplos, e que devolve
a soma dos elementos correspondentes a tipos elementares de dados que
existem no tuplo original. Não é necessário verificar os dados de entrada.
Por exemplo,
```
>>> soma_els_atomicos((3, ((((((6, (7, ))), ), ), ), ), 2, 1))
19
>>> soma_els_atomicos(((((),),),))
0
```

## ex06
Escreva a função recursiva `inverte` que recebe uma lista e devolve a lista
invertida. Por exemplo,
```
>>> inverte([3, 4, 7, 9])
[9, 7, 4, 3]
```

## ex07
Suponha que a operação `in` não existia em Python. Escreva a função
recursiva `pertence` que recebe uma lista e um elemento e devolve `True` se
o elemento pertence à lista e `False` em caso contrário. Por exemplo,
```
>>> pertence([3, 4, 5], 2)
False
>>> pertence([3, 4, 5], 5)
True
```

## ex08
Escreva a função recursiva `subtrai` que recebe duas listas e devolve a
lista que corresponde a remover da primeira lista todos os elementos que
pertencem à segunda lista. Por exemplo,
```
>>> subtrai([2, 3, 4, 5], [2, 3])
[4, 5]
>>> subtrai([2, 3, 4, 5], [6, 7])
[2, 3, 4, 5]
```

## ex09
Escreva a função recursiva `parte` que recebe uma lista de números e um
número e que devolve uma lista de duas listas, a primeira lista contém
os elementos da lista original menores que o número dado (pela mesma
ordem) e a segunda lista contém os elementos da lista original maiores ou
iguais que o número dado (pela mesma ordem). Não é necessário verificar
a coreção dos dados de entrada. Sugestão: Use uma função auxiliar. Por
exemplo,
```
>>> parte([3, 5, 1, 4, 5, 8, 9], 4)
[[3, 1], [5, 4, 5, 8, 9]]
```

## ex10
10. Escreva a função recursiva `maior` que recebe uma lista de números
e devolve o maior número da lista. Sugestão: use uma função auxiliar.
Por exemplo,
```
>>> maior([5, 3, 8, 1, 9, 2])
9
```

## ex11
Considere a seguinte função:
```python
def misterio(x, n):
    if n == 0:
        return 0
    else:
        return x * n + misterio(x, n - 1)
```
- (a) Explique o que é calculado pela função `misterio`.
- (b) Mostre a evolução do processo gerado pela avaliação de `misterio(2, 3)`.
- (c) De que tipo é o processo gerado pela função apresentada? Justifique.
- (d) Se a função apresentada for recursiva de cauda, defina uma nova função recursiva por transformação da primeira de modo a deixar operações adiadas; se for uma função recursiva com operações adiadas,
defina uma função recursiva de cauda.

## ex12
Suponha que as operações de multiplicação (\*) e potência (\*\*) não existiam em Python e que pretende calcular o quadrado de um número natural.
O quadrado de um número natural pode ser calculado como a soma de
todos os números ímpares inferiores ao dobro do número

![formula](https://render.githubusercontent.com/render/math?math=n^2=\sum_{i=1}^{n}(2i-1))

Note que o dobro de um número também não pode ser calculado recorrendo à operação de multiplicação. Escreva uma função que calcula o
quadrado de um número natural utilizando o método descrito.

- (a) Usando recursão com operações adiadas: `quadrado(n)`.
- (b) Usando recursão de cauda: `quadrado2(n)`.
- (c) Usando um processo iterativo: `quadrado3(n)`.

## ex13
Escreva a função `numero_digitos` que recebe um número inteiro positivo `n`, e devolve o número de dígitos de `n`. As suas funções não podem
user cadeias de caracteres. As suas funções devem validar a correção do
argumento. Por exemplo,
```
>>> numero_digitos(9)
1
>>> numero_digitos(1012)
4
```
- (a) Usando recursão com operações adiadas: `numero_digitos(n)`.
- (b) Usando recursão de cauda: `numero_digitos2(n)`.
- (c) Usando um processo iterativo: `numero_digitos3(n)`.

## ex14
Um número é uma capicua se se lê igualmente da esquerda para a direita
e vice-versa. Escreva a função recursiva de cauda `eh_capicua`, que recebe um número inteiro positivo `n`, e devolve verdadeiro se o número for
uma capicua e falso caso contrário. A sua função deve utilizar a função
`numero_digitos` do exercício anterior. Por exemplo,
```
>>> eh_capicua(12321)
True
>>> eh_capicua(1221)
True
>>> eh_capicua(123210)
False
```

## ex15
O espelho de um número inteiro positivo é o resultado de inverter a ordem
de todos os seus algarismos. Escreva a função recursiva de cauda `espelho`,
que recebe um número inteiro positivo `n`, não divisível por `10`, e devolve o
seu espelho. Por exemplo,
```
>>> espelho(391)
193
>>> espelho(45679)
97654
```

## ex16
Considere a função `g__`, definida para inteiros não negativos do seguinte
modo:
```
0              se n = 0
n - g__(g__(n-1))  se n > 0
```
- (a) Escreva uma função recursiva em Python para calcular o valor de
`g__(n)`.
- (b) Siga o processo gerado por `g__(3)`, indicando todos os cálculos efectuados.
- (c) Que tipo de processo é gerado por esta função?

## ex17
Escreva a função recursiva, `calc_soma`, para calcular o valor da soma.

![formula](https://render.githubusercontent.com/render/math?math=1%2Bx%2B\frac{x^2}{2!}%2B\frac{x^3}{3!}%2B\frac{x^4}{4!}%2B...%2B\frac{x^n}{n!}).

para um dado valor de `x` e de `n`. A sua função deve ter em atenção
que o i-ésimo termo da soma pode ser obtido do termo na posição `i-1`,
multiplicando-o por `x/i`.

## ex18
Escreva a função recursiva, `maior_inteiro`, que recebe um inteiro positivo, limite, e que devolve o maior inteiro (n) tal que 1 + 2 + ... + n <=
limite. Por exemplo,
```
>>> maior_inteiro(6)
3
>>> maior_inteiro(20)
5
```

## ex19
Um número `d` é divisor de `n` se o resto da divisão de `n` por `d` for `0`. Usando
recursão de cauda, escreva a função `soma_divisores` que recebe um número inteiro positivo `n`, e que devolve a soma de todos os divisores de
`n`.

## ex20
10. Um número diz-se perfeito se for igual à soma dos seus divisores (não
contando o próprio número). Por exemplo, `6` é perfeito porque `1+2+3 = 6`.
- (a) Usando recursão de cauda, escreva a função `perfeito` que recebe
como argumento um número inteiro e tem o valor `True` se o seu
argumento for um número perfeito e `False` em caso contrário. Não
é necessário validar os dados de entrada.
- (b) Usando recursão com operações adiadas e a função `perfeito` da alínea anterior, escreva a função `perfeitos_entre` que recebe dois inteiros positivos e devolve a lista dos números perfeitos entre os seus
argumentos, incluindo os seus argumentos. Por exemplo:
```
>>> perfeitos_entre(6, 30)
[6, 28]
```
