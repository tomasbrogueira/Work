# Colecções: tuplos e strings

![image](python-tuples.png)

## ex01
Considere as seguintes instruções em Python:
```python
soma = 0
i = 20
while i > 0:
    soma = soma + 1
    i = i - 2
print('Soma =', soma)
```
Escreva instruções equivalentes utilizando um ciclo for.

## ex02
Escreva a função `explode` que recebe um número inteiro positivo e, após verificar a correção do seu argumento, e devolve o tuplo contendo os dígitos
desse número, pela ordem em que aparecem no número. Por exemplo
```
>>> explode(34500)
(3, 4, 5, 0, 0)
>>> explode(3.5)
ValueError: explode: argumento não inteiro
```

## ex03
Escreva a função `implode` que recebe um tuplo contendo algarismos , após verificar a correção do seu argumento, e devolve o número inteiro contendo
os algarismos do tuplo, pela ordem em que aparecem. Por exemplo
```
>>> implode((3, 4, 0, 0, 4))
34004
>>> implode((2, 'a', 5))
ValueError: implode: elemento não inteiro
```
Escreva duas versões da sua função, uma utilizando um ciclo while e outra
utilizando um ciclo for.

## ex04
Escreva a função `filtra_pares` que recebe um tuplo contendo algarismos e, após verificar a correção do seu argumento, e devolve o tuplo contendo
apenas os algarismos pares. Por exemplo
```
>>> filtra_pares((2, 5, 6, 7, 9, 1, 8, 8))
(2, 6, 8, 8)
```

## ex05
Recorrendo às funções `explode`, `implode` e `filtra_pares`, defina a função
`algarismos_pares` que recebe um inteiro e devolve o inteiro que apenas
contém os algarismos pares do número original. Por exemplo,
```
algarismos_pares(6643399766641)
6646664
```

## ex06
Escreva a função `num_para_seq_cod` que recebe um número inteiro positivo maior do que zero e que devolve um tuplo contendo os algarismos
codificados desse número do seguinte modo: (a) cada algarismo par é
substituído pelo número par seguinte, entendendo-se que o número par
seguinte a 8 é o 0; (b) cada algarismo ímpar é substituído pelo número
ímpar anterior, entendendo-se que o número ímpar anterior a 1 é o 9. Por
exemplo,
```
>>> num_para_seq_cod(1234567890)
(9, 4, 1, 6, 3, 8, 5, 0, 7, 2)
```

## ex07
Duas palavras de igual comprimento dizem-se "amigas" se o número de posições em que os respetivos carateres diferem for inferior a 10%. Escreva
a função `amigas` que recebe como argumentos duas cadeias de carateres e devolve verdadeiro se os seus argumentos corresponderem a palavras
amigas e falso em caso contrário. Por exemplo:
```
amigas('amigas', 'amigas')
True
amigas('amigas', 'asigos')
False
```

## ex08
Defina a função, `junta_ordenados`, que recebe dois tuplos contendo inteiros,
ordenados por ordem crescente. e devolve um tuplo
com os elementos dos dois tuplos também ordenados por ordem crescente.
Por exemplo,
```
>>> junta_ordenados((2, 34, 200, 210), (1, 23))
(1, 2, 23, 34, 200, 210)
```

## ex09
Considere a gramática em notação BNF:
```
<idt> ::= <letras> <numeros>
<letras> ::= <letra> | <letra> <letras>
<numeros> ::= <num> | <num> <numeros>
<letra> ::= A | B | C | D
<num> ::= 1 | 2 | 3 | 4
```

Escreva a função `reconhece` que recebe como argumento uma cadeia
de carateres e devolve verdadeiro se o seu argumento corresponde a uma
frase da linguagem definida pela gramática e falso em caso contrário.
Por exemplo,
```
>>> reconhece('A1')
True
>>> reconhece('ABBBBCDDDD23311')
True
>>> reconhece('ABC12C')
False
```

## ex10
Um método básico para codificar um texto corresponde a isolar os carateres das posições pares para um lado e os carateres nas posições ímpares
para o outro, juntando depois as duas partes anteriormente obtidas. Por
exemplo, o texto `abcde` é codificado por `acebd`.

- (a) Defina uma função que `codifica` uma cadeia de carateres de acordo
com o algoritmo apresentado. Não é necessário validar os dados de
entrada. Por exemplo,
```
>>> codifica('abcde')
'acebd'
```
- (b) Defina uma função que `descodifica` uma cadeia de carateres de acordo
com o algoritmo apresentado. Não é necessário validar os dados de
entrada. Por exemplo,
```
>>> descodifica('acebd')
'abcde'
```

## ex11
Escreva a função `lista_codigos` que recebe uma cadeia de carateres
como argumento e que devolve um tuplo contendo os códigos "Unicode"
de cada um dos carateres de um tuplo. Por exemplo:
```
>>> lista_codigos('bom dia')
(98, 111, 109, 32, 100, 105, 97)
```

## ex12
Escreva um predicado, designado por `palidromo`, que recebe uma palavra
como argumento verifica se a palavra é um palíndromo ou não.
Uma palavra é um palíndromo se se escrever da mesma maneira da esquerda
para a direita e vice-versa (por exemplo, "AMA" é um palíndromo).
```
>>> palidromo('ANA')
True
>>> palidromo('palindromo')
False
```

## ex13
Escreva a função `apaga_char` que recebe uma cadeia de carateres e um caráter, devolvendo a cadeia de carateres com todas as ocorrências do caráter removidas.
```
>>> apaga_char('banana', 'a')
'bnn'
>>> apaga_char('ananaz', 'n')
'aaaz'
```

## ex14
Escreva a função `minusculas` que recebe uma cadeia de carateres e devolve a mesma cadeia com todas as letras maiusculas convertidas em minúsculas.
```
>>> minusculas('LaTeX')
'latex'
>>> minusculas('El Rei Dom João')
'el rei dom joão'
```

## ex15
Escreva a função `polyval` que recebe um tuplo com os fatores de um polinómio e um valor real, devolve o valor do polinómio para esse valor.
Por exemplo, o polinómio
![formula](https://render.githubusercontent.com/render/math?math=p(x)=4x^2%2B3x%2B2)
é representado pelo *tuplo* `(4,3,2)`
```
>>> polyval((4,3,2), 1.2)
11.36
>>> polyval((8,0,0,0,0,0,0,0,8), 1.1)
25.148710480000013
```

## ex16
Escreva a função `horner`, funcionalmente idêntica à função `polyval`,
mas o cálculo do valor do polinómio é realizado segundo o algoritmo de
[horner](https://en.wikipedia.org/wiki/Horner%27s_method):
![formula](https://render.githubusercontent.com/render/math?math=p(x)=a_0%2Bx(a_1%2Bx(a_2%2Bx(a_3%2B\ldots%2Bx(a_{n-1}%2Bxa_n)\ldots))))

## ex17
Escreva a função `trapz` que recebe dois tuplos da mesma dimensão contendo,
respetivamente, os valores de `x` e de `y` de um conjunto de pontos.
A função deve calcular o integral (a área definida pelos pontos e o eixo dos X) segundo a regra dos [trapézios](https://en.wikipedia.org/wiki/Trapezoidal_rule):
![formula](https://render.githubusercontent.com/render/math?math=\bar{x}=\sum_{i=1}^{n}\frac{(y_{i-1}%2By_i)(x_i-x_{i-1})}{2})
```
>>> x = ( 0., .25, .5, .75, 1. )
>>> y = ( 1., 1.0645, 1.2840, 1.7551, 2.7183 )
>>> trapz(x, y)
1.4906875
>>> x = ( 0, .1, .25, .5, .8, 1. )
>>> y = ( 1., 1.0101, 1.0645, 1.284, 1.8965, 2.7183 )
>>> trapz(x, y)
1.4882175
```

## ex18
Dados dois vetores de valores em vírgula flutuante em precisão dupla,
representando os valores de uma função definida por troços (*piecewise*),
os pontos de quebra dos segmentos `x` **ordenados** e os
respetivos valores `y`, pretende-se determinar o valor da função por
intepolação linear no ponto ![formula](https://render.githubusercontent.com/render/math?math=x_k).
Para tal deve procurar qual o segmento ![formula](https://render.githubusercontent.com/render/math?math=[x_i,x_{i+1}]) que inclui o ponto
![formula](https://render.githubusercontent.com/render/math?math=x_k),
ou seja ![formula](https://render.githubusercontent.com/render/math?math=x_k\in[x_i,x_{i+1}]) e determinar:
![formula](https://render.githubusercontent.com/render/math?math=y_k=y_i%2B(x_k-x_i)\frac{y_{i+1}-y_i}{x_{i%2B1}-x_i})

Para tal construa uma rotina, designada por `interpol` que
recebe dois vetores `x` e `y`, a sua dimensão `n` e o valor
![formula](https://render.githubusercontent.com/render/math?math=x_k) a
calcular, e devolve o valor
![formula](https://render.githubusercontent.com/render/math?math=y_k).
Se ![formula](https://render.githubusercontent.com/render/math?math=x_k)
estiver fora da função,
![formula](https://render.githubusercontent.com/render/math?math=x_k\notin]x_0,x_{n-1}[) devolve `nan` (*Not a number*): constante definida em `math`.
```
>>> x = ( 0., .25, .5, .75, 1. )
>>> y = ( 1., 1.0645, 1.2840, 1.7551, 2.7183 )
>>> interpol(x, y, .6)
1.47244
>>> x = ( 0, .1, .25, .5, .8, 1. )
>>> y = ( 1., 1.0101, 1.0645, 1.284, 1.8965, 2.7183 )
>>> interpol(x, y, .6)
1.4881666666666666
```

## ex19
Dado um vetor de valores em vírgula flutuante em precisão dupla,
pretende-se estimar a variância dos seus valores:
![formula](https://render.githubusercontent.com/render/math?math=\widehat{Var}(x)=\frac{1}{n-1}\sum^{i=0}_{n}(x_i-\bar{x})^2)
onde ![formula](https://render.githubusercontent.com/render/math?math=\bar{x}) representa a média de todos os valores.

Para tal construa uma rotina, designada por `variance` que
recebe o vetor e a sua dimensão e devolve a variância dos elementos
do vetor.
```
>>> x = ( 0., .25, .5, .75, 1. )
>>> variance(x)
0.15625
```

## ex20
Dado um vetor não ordenado de valores em vírgula flutuante em precisão
dupla, pretende-se saber qual o elemento do vetor mais próximo de um
valor dado.

Para tal construa uma rotina, designada por `closest` que
recebe um vetor, a sua dimensão e um valor `x_i`, e devolve o valor do
elemento do vetor mais próximo de `x_i`.
Se o vetor estiver vazio a função devolve `nan`:
constante `nan` definida em `math`.
```
>>> x = ( 0., .25, .5, .75, 1. )
>>> closest(x, .28)
0.25
>>> closest(x, 12)
1.0
```
