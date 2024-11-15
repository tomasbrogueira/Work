# Números reais em vírgula flutuante

![image](real-python.png)

Para resolver os exercícios deste laboratório deve utilizar
exclusivamente valores numéricos, inteiros ou em vírgula flutuante,
ou seja não deve usar cadeias de carateres, por exemplo.

Nestes exercícios imprima (`print`) os números reais em vírgula flutuante
com um máximo de `8` dígitos decimais usando a função `round(num,dig)`,
ou seja `round(x,8)`.

## ex01
Escreva um programa em Python que lê valores correspondentes a uma
distância percorrida (em **Km**) e o tempo necessário para a percorrer (em
**minutos**), e calcula a velocidade média em:

- (a) Km / h
- (b) m / s

Por exemplo:
```
distância percorrida (Km): 300
tempo gasto (minutos): 200
90.0 Km/h
25.0 m/s
```

## ex02
Escreva um programa em Python que pede ao utilizador que lhe forneça
um inteiro correspondente a um número de segundos e que calcula o número de dias correspondentes a esse número de segundos. O seu programa
deve permitir a interação:
```
Escreva um número de segundos
? 65432998
O número de dias correspondentes é 757.32636574
```

## ex03
Escreva um programa em Python que lê cinco números reais e calcula a
sua média e o seu desvio padrão. A média, x̄, e o desvio padrão, Ϭ, de
cinco números `x1 , ... x5` são dados respectivamente por
![formula](https://render.githubusercontent.com/render/math?math=\bar{x}=\frac{\sum_{i=1}^{5}x_i}{5})
e por
![formula](https://render.githubusercontent.com/render/math?math=\sigma=\sqrt{\frac{1}{4}\sum_{i=1}^{5}(x_i-\bar{x})}^2)


A primeira linha do seu programa deve ser `from math import sqrt`. Esta
instrução importa a função `sqrt` que calcula a raiz quadrada. Por exemplo,
`sqrt(4)` tem o valor `2.0`.
Considere o exemplo de execução
```
x1 = 1
x2 = 2
x3 = 3
x4 = 4
x5 = 5
média = 3.0 desvio padrão = 1.58113883
```

## ex04
Escreva um programa em Python que pede ao utilizador que lhe forneça
uma sucessão de inteiros correspondentes a valores em segundos e que
calcula o número de dias correspondentes a cada um desses inteiros. O
programa termina quando o utilizador fornece um número negativo. O
seu programa deve possibilitar a seguinte interação:
```
Escreva um número de segundos
(um número negativo para terminar)
? 45
O número de dias correspondente é 0.00052083
Escreva um número de segundos
(um número negativo para terminar)
? 6654441
O número de dias correspondente é 77.01899306
Escreva um número de segundos
(um número negativo para terminar)
? -1
```

## ex05
Escreva um programa em Python que calcula o valor da soma:
![formula](https://render.githubusercontent.com/render/math?math=1%2Bx%2B\frac{x^2}{2!}%2B\frac{x^3}{3!}%2B...%2B\frac{x^n}{n!})

para um dado valor de `x` e de `n`. O seu programa deve ter em atenção
que o i-ésimo termo da soma pode ser obtido do termo na posição `i - 1`,
multiplicando-o por `x/i`. O seu programa deve permitir a interação:
```
Qual o valor de x
? 2
Qual o valor de n
? 3
O valor da soma é 6.33333333
```

## ex06
Dado um conjunto de `n` inteiros representando notas de alunos, escreva
um programa em Python para determinar quantos tiveram nota positiva.
Modifique o seu programa de modo a também calcular qual a percentagem
de notas positivas.
```
Nota ? 12
Nota ? 17
Nota ? 19
Nota ? 15
Nota ? 18
Nota ? 16
Nota ? 16
Nota ? -2
7 positivas 100.0 %
```

## ex07
Defina a função `horas_dias` que recebe um número inteiro 
de horas e que retorna um número real correspondente
ao número de dias. Por exemplo
```
>>> horas_dias(48)
2.0
>>> horas_dias(10)
0.4166666666666667
```

## ex08
Defina a função `area_circulo` que recebe o valor do raio de um círculo e
tem como valor a área do círculo. Note-se que a área do círculo cujo raio
é `r` é dada por 
![formula](https://render.githubusercontent.com/render/math?math=\pi{r}^2).
Use o valor de π definido em `math` (`from math import pi`).
A função deve devolver `0` para raios negativos.
```
>>> area_circulo(2)
12.566370614359172
>>> area_circulo(-2)
0
```

## ex09
Utilizando a função `area_circulo` do exercício anterior, escreva a função
`area_coroa` que recebe dois argumentos, `r1` e `r2`, e que tem como valor
a área da coroa circular de raio interior `r1` e raio exterior `r2`.
A sua função deverá gerar um erro de valor (`ValueError`) se o valor de
`r1` for maior que o valor de `r2`.
```
>>> area_coroa(12,13)
78.53981633974485
>>> area_coroa(12,10)
ValueError: r1 > r2
```

## ex10
Quando se efectua um depósito a prazo de uma quantia `q` com uma taxa
de juros `j (0 < j < 1)`, o valor do depósito ao fim de `n` anos é dado por
![formula](https://render.githubusercontent.com/render/math?math=q\times(1%2Bj)^n)

- (a) Escreva a função `valor` que recebe como argumentos um número inteiro positivo `q` correspondente à quantia depositada, um real `j` no
intervalo `]0, 1[` correspondente à taxa de juros e um inteiro positivo
`n` correspondente ao número de anos que o dinheiro está a render.
Após verificar os argumentos, esta função deverá devolver um real
correspondente ao valor do depósito ao fim do número de anos `n`.
Caso os argumentos não estejam correctos, a função deverá gerar um erro.
Por exemplo,
```
>>> valor(100, 0.03, 4)
112.55088100000002
```

- (b) Usando a função da alínea anterior, escreva uma função que calcula
ao fim de quantos anos consegue `duplicar` o seu dinheiro.
Não é necessário validar os dados de entrada. Por exemplo,
```
>>> duplicar(100, 0.03)
24
```

## ex11
Escreva a função `pi` que calcula uma aproximação ao valor de π
por desenvolvimento em série Gregory-Leibniz
![formula](https://render.githubusercontent.com/render/math?math=\frac{\pi}{4}=1-\frac{1}{3}%2B\frac{1}{5}-\frac{1}{7}%2B\frac{1}{9}%2B...).
A função recebe como argumento um inteiro que representa o número termos da série a calcular. Por exemplo:
```
>>> pi(200)
3.136592684838816
```

## ex12
O método da bisseção permite encontrar a aproximaçao de um zero de uma
função `f` contínua num intervalo `[a,b]` tal que `f(a) f(b) < 0`,
o que significa que a função `f` troca de sinal no intervalo.
O método consiste em dividir o intervalo ao meio `c = (a + b) / 2` e
verificar qual das metades contém o zero.
O novo intervalo é agora sucessivamente dividido até o valor da função
ser suficientemente próximo de zero.

Escreva a função `bissecao(f,a,b,n,feps,neps)`, que recebe uma função (ponteiro) e os
extremos do intervalo `a` e `b`. A função recebe igualmente o número
máximo de iteradas a realizar `n`, o erro absoluto máximo `feps` (quão
próximo do zero se pretende a raiz), e o comprimento mínimo do intervalo
`neps`.
Para estes três últimos argumentos considere valores por omissão de `100`,
`1e-6` e `1e-6`, respetivamente.
A função devolve o valor aproximado de `x` e o número de iteradas realizadas
como um tuplo `(x, n)`.

Por exemplo, para calcular o valor de `x` para
![formula](https://render.githubusercontent.com/render/math?math=x%2Be^{-x}=2)
no intervalo '[0, 2]` deve fazer:
```
>>> from math import exp
>>> def func(x): return x + exp(-x) -2
>>> bissecao(func, 0, 2)
(1.8414058685302734, 20)
```

## ex13
Para calcular o valor da raiz quadrada pelo método babilónico é necessário
considerar que, se *x* é uma sobreestimação da raiz quadrada de S,
então *S/x* é uma subestimativa, e vice-versa,
logo a média dos dois valores é uma aproximação melhor
que o valor anterior de *x*.
Assim, cada nova iterada é calculada por
![formula](https://render.githubusercontent.com/render/math?math=x_{n%2B1}=\frac{1}{2}\left(s_n%2B\frac{S}{x_n}\right))
O valor inicial de *x* deve ser uma boa estimativa da raiz quadrada de *S*,
mas como a convergência é garantida e quadrática
(ver [wikipedia](https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method), qualquer valor positivo serve.

Escreva a função `sqroot(n, eps = 1e-12)` que devolve o valor aproximado
da raiz quadrada do argumento `n` com um erro
(diferença entre a sobreestimação e a subestimação) inferior a `eps`.
Compare com o valor devolvido pela rotina da biblioteca `math` do python.
Por exemplo:
```
>>> sqroot(12)
3.464101615137755
>>> from math import sqrt
>>> sqrt(12)
3.4641016151377544
```

## ex14
Equações diferenciais são usadas muito frequentemente para descrever
processos nos quais a mudança de uma medida ou dimensão é causada pelo
próprio processo.
Por exemplo, no crescimento de populações, quanto maior é a população,
mais a população cresce.
O método de [euler](https://en.wikipedia.org/wiki/Euler_method)
para resolver equações diferenciais consiste em dividir o intervalo
`[a,b]` em `n` subintervalos, a que correspode um passo
![formula](https://render.githubusercontent.com/render/math?math=h=\frac{t_n-t_0}{n})
Em cada passo os novos valores de `x` e `y`
são calculados iterativamente por
![formula](https://render.githubusercontent.com/render/math?math=y_i=y_{i-1}%2Bfunc(x_{i-1},y_{i-1})h) e
![formula](https://render.githubusercontent.com/render/math?math=x_i=x_{i-1}%2Bh).
Quanto maior for o número de iteradas mais preciso será o valor devolvido.

Escreva a função `euler(f, y0, t0, tn, n)`, que recebe uma função (ponteiro) e os
valores iniciais `y0` e `x0 = a`. 
A função recebe igualmente o valor final `b` e o número máximo de iteradas a realizar `n`.
Considere a função `y'=2*exp(-2)` com `y0=2` em `t0=0`; a solução em `tn=1` é:
```
>>> from math import exp
>>> def func(t, y): return 2 * exp(-y)
>>> euler(func, 2, 0, 1, 5)
2.244832660832381
```
*Nota: a solução exata é* `log(2*x+exp(2))=2.2395447662218846`.

## ex15
Funções transcendentes não podem ser expressas por uma combinação finita
de expressões algébricas.
Algumas destas funções podem ser descritas por séries infinitas, logo
os seus valores podem ser aproximados calculando os primeiros `N` termos
da série.

Um método para calcular a função logaritmo nepriano `log(x)`, para `x>1`,
consiste em utilizar o desenvolvimento em série:
![formula](https://render.githubusercontent.com/render/math?math=\log(z)=2\sum_{k=0}^{\infty}{\frac{1}{2k%2B1}}\left({\frac{z-1}{z%2B1}}\right)^{2k%2B1})

Escreva a função `logn`, que recebe um número real `x` e o número de termos
da série a calcular `n`, devolvendo uma aproximação ao logaritmo nepriano de `x`.
```
>>> logn(1.5, 20)
0.40546510810816444
```

## ex16
Um método para calcular a função exponencial ![formula](https://render.githubusercontent.com/render/math?math=e^x) consiste em utilizar
o desenvolvimento em série:
![formula](https://render.githubusercontent.com/render/math?math=e^x=1%2Bx%2B\frac{x^2}{2}%2B\ldots%2B\frac{x^n}{n!})

Escreva a função `expon`, que recebe um número real `x` e o número de termos
da série a calcular `n`, devolvendo uma aproximação à exponencial de `x`.
```
>>> expon(1.5, 20)
4.481689070338066
```


## ex17
Um método para calcular a função trigonométrica seno consiste em utilizar
o desenvolvimento em série:
![formula](https://render.githubusercontent.com/render/math?math=sen(x)=x-\frac{x^3}{3!}%2B\frac{x^5}{5!}%2B\ldots%2B\frac{(-1)^nx^{2n%2B1}}{(2n%2B1)!})

Escreva a função `seno`, que recebe um número real `x` e o número de termos
da série a calcular `n`, devolvendo uma aproximação ao seno de `x`.
```
>>> seno(1.5, 20)
0.9974949866040546
```

## ex18
Um método para calcular a função trigonométrica coseno consiste em utilizar
o desenvolvimento em série:
![formula](https://render.githubusercontent.com/render/math?math=cos(x)=1-\frac{x^2}{2!}%2B\frac{x^4}{4!}%2B\ldots%2B\frac{(-1)^{n}x^{2n}}{(2n)!})

Escreva a função `coseno`, que recebe um número real `x` e o número de termos
da série a calcular `n`, devolvendo uma aproximação ao coseno de `x`.
```
>>> coseno(1.5, 20)
0.0707372016677029
```


## ex19
Um método para calcular a função trigonométrica arco seno consiste em
utilizar o desenvolvimento em série:
![formula](https://render.githubusercontent.com/render/math?math=\arcsin(z)=\sum_{n=0}^{\infty}{\frac{(2n)!}{(2^{n}n!)^{2}}}{\frac{z^{2n%2B1}}{2n%2B1}},\qquad|z|\leq{1},z\neq{i},z\neq{-1})

Escreva a função `arco_seno`, que recebe um número real `x` e o número de termos
da série a calcular `n`, devolvendo uma aproximação ao arco seno de `x`.
```
>>> arco_seno(0.5, 20)
0.5235987755982972
```

## ex20
Um método para calcular a função trigonométrica arco tangente consiste em
utilizar o desenvolvimento em série:
![formula](https://render.githubusercontent.com/render/math?math=\arctan(z)={\frac{z}{1%2Bz^{2}}}\sum_{n=0}^{\infty}\prod_{k=1}^{n}{\frac{2kz^{2}}{(2k%2B1)(1%2Bz^{2})}})

Escreva a função `arctan`, que recebe um número real `x` e o número de termos
da série a calcular `n`, devolvendo uma aproximação ao arco tangente de `x`.
```
>>> arctan(1.5, 20)
0.9826156164193632
```
