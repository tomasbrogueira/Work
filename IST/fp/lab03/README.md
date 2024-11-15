# Elementos Básicos de Programação

![image](python-programming.png)

Para resolver os exercícios deste laboratório deve utilizar
exclusivamente valores inteiros, ou seja não deve usar
valores em vírgula flutuante ou cadeias de carateres, por exemplo.

Para testar as suas resoluções dos exercícios deve criar um ficheiro
com o nome do exercício, por exemplo `ex01.py`, e executar `python
test_ex01.py` (ou apenas `./test_ex01.py` em *UNIX*) para executar
os testes.
Para testar todos os exercícios pode fazer `python -m unittest`;
os testes aos exercícios ainda não resolvidos, ou com erros,
são ignorados (*skipped*) [**s**].
Opções com `python -m unittest -h`.

## ex01
Escreva um programa em Python que pede ao utilizador que lhe forneça
dois números (x e y) e que escreve o valor de (x + 3 * y) * (x - y).
O seu programa deve gerar uma interação como a seguinte:
```
Vou pedir-lhe dois numeros
Escreva o primeiro numero, x = 5
Escreva o segundo numero, y = 6
O valor de (x + 3 * y) * (x - y) e: -23
```

## ex02
Escreva um programa que lê um número inteiro correspondente a um
certo número de segundos e que escreve o número de dias, horas, minutos
e segundos correspondentes a esse número. Por exemplo,
```
Escreva o número de segundos 345678
dias: 4 horas: 0 mins: 1 segs: 18
```

## ex03
Escreva um programa em Python que lê três números e que diz qual o
maior dos números lidos. Por exemplo,
```
x1 = 1
x2 = 2
x3 = 3
O maior é 3
```

## ex04
Escreva um programa em Python que lê o número de horas, que um empregado trabalhou numa dada semana e o seu salário/hora e calcula o
ordenado semanal tendo em conta as horas extraordinárias. O salário é
calculado do seguinte modo: se o número de horas for menor que 40 então
salário é dado pelo produto do número de horas pelo salário hora; em caso
contrário recebe horas extraordinárias as quais são pagas a dobrar.
```
horas de trabalho: 56
salário/hora: 35
pagar 2520
```

## ex05
Escreva um programa em Python que lê uma sequência de dígitos, sendo
cada um dos dígitos fornecido numa linha separada, e calcula o número
inteiro composto por esses dígitos, pela ordem fornecida. Para terminar a
sequência de dígitos, terá de ser fornecido ao programa o inteiro -1. O seu programa
deve permitir a interação:
```
Escreva um dígito
(-1 para terminar)
? 3
Escreva um dígito
(-1 para terminar)
? 2
Escreva um dígito
(-1 para terminar)
? 5
Escreva um dígito
(-1 para terminar)
? 7
Escreva um dígito
(-1 para terminar)
? -1
O número é: 3257
```

## ex06
Escreva um programa em Python que lê um número inteiro positivo e
imprime o número com a mesma sequência de dígitos do número lido
que apenas contém os seus dígitos impares. Por exemplo,
```
Escreva um inteiro
? 785554
Resultado: 7555
```

## ex07
Escreva um programa em Python que lê um número inteiro positivo e
imprime o número com a ordem dos seus dígitos invertida. Por
exemplo,
```
Escreva um inteiro positivo
? 7633256
O número invertido é 6523367
```

## ex08
Escreva um programa em Python que pede ao utilizador que lhe forneça
um número e que escreve a tabuada da multiplicação para esse número.
O seu programa deve gerar uma interacção como a seguinte:
```
Escreva um numero para eu escrever a tabuada da multiplicação
Num -> 8
8 x 1 = 8
8 x 2 = 16
8 x 3 = 24
8 x 4 = 32
8 x 5 = 40
8 x 6 = 48
8 x 7 = 56
8 x 8 = 64
8 x 9 = 72
8 x 10 = 80
```

## ex09
Escreva um programa que lê um inteiro e calcula a soma dos seus dígitos.
```
Escreva um inteiro positivo
? 123876
A soma dos dígitos é 27
```

## ex10
Escreva um programa que lê um número e cria uma capicua cuja primeira
metade é o número lido. Por exemplo:
```
Escreva um número
-> 347
347743
```

## ex11
Escreva um programa que lê um número inteiro e determina quantas vezes
aparecem dois zeros seguidos. Por exemplo:
```
Escreva um inteiro
? 98007640003
O numero tem 3 zeros seguidos
```

## ex12
Escreva um programa em Python que lê uma quantia em Euros e calcula
o número de notas de 50€ e, 20€ e, 10€ e, 5€ e e moedas de 2€ e, 1€ e, 50
cêntimos, 20 cêntimos, 10 cêntimos, 5 cêntimos, 2 cêntimos e 1 cêntimo,
necessário para perfazer essa quantia, utilizando sempre o máximo
número de notas e moedas para cada quantia, da mais elevada, para a mais
baixa.
```
Escreva uma quantia ? 200
4 * 50 €
```
ou
```
Escreva uma quantia ? 237.89
4 * 50 €
1 * 20 €
1 * 10 €
1 * 5 €
1 * 2 €
1 * 50 cênt
1 * 20 cênt
1 * 10 cênt
1 * 5 cênt
2 * 2 cênt
```

## ex13
Escreva um programa em Python que escreve o seguinte:
```
1 x 8 + 1 = 9
12 x 8 + 2 = 98
123 x 8 + 3 = 987
1234 x 8 + 4 = 9876
12345 x 8 + 5 = 98765
123456 x 8 + 6 = 987654
1234567 x 8 + 7 = 9876543
12345678 x 8 + 8 = 98765432
123456789 x 8 + 9 = 987654321
```
Os valores do primeiro termo da multiplicação e o resultado devem ser
calculados pelo seu programa.

## ex14
Desenvolva um classificador de triângulos: desenvolva a função `triangulo` que recebe
*3* argumentos do tipo inteiro que representam as dimensões de cada
lado do triângulo e devolve:

- **None** se alguma dimensão não for positiva
- **0** se as 3 dimensões não formam um triângulo
- **1** se o triânglo é equilátero
- **2** se o triânglo é isósceles
- **3** se o triânglo é escaleno

## ex15
Escreva a função `cinco` que devolve o valor `True` se o seu argumento
for `5` e `False` caso contrário. Não pode utilizar uma instrução `if`.

## ex16
Escreva a função bissexto que recebe um número inteiro correspondente a
um ano e que devolve `True` se o ano for bissexto e `False` em caso contrário.
Um ano é bissexto se for divisível por `4` e não for divisível por `100`, a não
ser que seja também divisível por `400`. Por exemplo, `1984` é bissexto, `1100`
não é, e `2000` é bissexto. por exemplo:
```
>>> bissexto(1984)
True
>>> bissexto(1985)
False
>>> bissexto(2000)
True
```

## ex17
Defina a função `dias_mes` que recebe uma cadeia de caracteres
correspondentes às 3 primeiras letras (minúsculas) do nome de um mês e um
ano, e retorna o número inteiro correspondendo ao número de
dias desse mês. No caso de uma cadeia de caracteres inválida, a sua função
deverá gerar um erro de valor (`ValueError`). Use a função `bissexto` do
exercício anterior. A sua função deve permitir gerar a interação:
```
>>> dias_mes('jan', 2017)
31
>>> dias_mes('fev', 2016)
29
>>> dias_mes('MAR', 2017)
ValueError: Mês não existe
```

## ex18
Escreva a função `serie_geom` que recebe um inteiro `r` e um inteiro não
negativo `n`, e devolve a soma dos primeiros `n+1` termos da série geométrica
![formula](https://render.githubusercontent.com/render/math?math=1%2Br%2Br^2%2Br^3%2B\ldots%2Br^n). Por exemplo,
```
>>> serie_geom(2, 4)
31
>>> serie_geom(100, 0)
1
>>> serie_geom(100, -1)
ValueError: serie_geom: argumento incorrecto
```

## ex19
A *congruência de Zeller* é um algoritmo inventado pelo matemático alemão Julius Christian Zeller (1822–1899) para calcular o dia da semana
para qualquer dia do calendário. Para o nosso calendário, o *calendário
Gregoriano*, a congruência de Zeller é dada por:
[wikipedia](https://pt.wikipedia.org/wiki/Congru%C3%AAncia_de_Zeller).
Escreva uma função em Python, chamada `dia_da_semana` que recebe três
inteiros correspondentes ao dia, mês e ano e que devolve o dia da
semana em que calha essa data. A sua função pode utilizar outras funções
auxiliares a definir por si. Por exemplo,
```
>>> dia_da_semana(18, 1, 2014)
’sábado’
```

## ex20
Defina uma função `mistério` que, dado qualquer inteiro `n` de `3`
algarismos, cuja diferença entre o primeiro e último dígito é superior
a `1`, inverte os algarismos de `n`, obtendo `ni`; em seguida subtrai
o maior do menor, obtendo `ns`, ou seja `ns =| n - ni |`; e finalmente
inverte os algarismos de `ns`, obtendo `nsi`. 
Pode verificar que `ns + nsi = 1089`. Por exemplo, suponhamos que `n = 246`,
então `ni = 642`, `ns = 396`, `nsi = 693` e `ns + nsi = 396 + 693 = 1089`.
A sua função deve garantir que o argumento é correto. Por exemplo,
```
>>> misterio(246)
1089
>>> misterio(131)
ValueError: Condições não verificadas
```

Explique este mistério.

## ex21
Escreva a função `divisores` que recebe um número inteiro `n` e devolve
o número de divisores de um número, excluindo o próprio `n` e a unidade,
ou `0` se for primo.
Por exemplo,
```
>>> divisores(27983)
0
>>> divisores(30)
6
>>> divisores(144)
13
>>> divisores(120)
14
```
