# Funções de ordem superior

![image](lambda-python.jpeg)

## ex01
A função somatorio:
```python
def somatorio(l_inf, l_sup, calc_termo, prox):
    soma = 0
    while l_inf <= l_sup:
        soma = soma + calc_termo(l_inf)
        l_inf = prox(l_inf)
    return soma
```
é apenas a mais simples de um vasto número de abstracções semelhantes
que podem ser capturadas por funções de ordem superior. Por exemplo,
podemos usar a função somatorio para somar os quadrados dos múltiplos
de `3` entre `9` e `21`:
```
>>> somatorio(9, 21, lambda x : x * x, lambda x : x + 3)
1215
```
Diga o que fazem as seguintes utilizações da função somatório:

- (a) `somatorio(4, 500, lambda x: x, lambda x: x + 1)`
- (b) `somatorio(5, 500, lambda x: x * x, lambda x: x + 5)`
- (c) `somatorio(1, 5, lambda x: somatorio(1, x, lambda x: x, lambda x: x+1), lambda x: x+1)`

## ex02

- (a) Defina a função `piatorio` que calcula o produto dos termos de uma
função entre dois limites especificados:
`piatorio(l_inf, l_sup, func, fprox)`, onde `fprox` é uma função que devolve
o valor seguinte a ser usado na invocação da função `func`.
- (b) Mostre como definir o `fatorial` em termos da utilização da função
`piatorio`.

## ex03
Considere a função `soma_fn` que recebe um número inteiro positivo, `n`, e
uma função de um argumento inteiro, `fn`, e devolve a soma de todos os
valores da função entre `1` e `n`. A função `soma_fn` não verifica a correção
do seu argumento nem usa funcionais sobre listas. Por exemplo,
```
>>> soma_fn(4, lambda x: x * x)
30
>>> soma_fn(4, lambda x: x + 1)
10
```
- (a) Escreva a função `soma_fn_for` usando um ciclo for.
- (b) Escreva a função `soma_fn` usando recursão.

## ex04
Usando recursão, defina os seguintes funcionais sobre listas:

- (a) `filtra(tst, lst)` que devolve a lista obtida a partir da lista `lst`
que apenas contém os elementos que satisfazem o predicado de um
argumento `tst`. Por exemplo,
```
>>> filtra(lambda x : x % 2 == 0, [1, 2, 3, 4, 5])
[2, 4]
```
- (b) `transforma(fn, lst)` que devolve a lista obtida a partir da lista
`lst` cujos elementos correspondem à aplicação da função de um argumento `fn` aos elementos de `lst`. Por exemplo,
```
>>> transforma(lambda x : x ** 3, [1, 2, 3, 4])
[1, 8, 27, 64]
```
- (c) `acumula(fn, lst)` que devolve o valor obtido da aplicação da função de dois argumentos `fn` a todos os elementos da lista `lst`. Por
exemplo,
```
>>> acumula(lambda x, y : x + y, [1, 2, 3, 4])
10
```

## ex05
Usando os funcionais sobre listas da pergunta anterior, escreva a função
`soma_quadrados_impares`, que recebe uma lista de inteiros e devolve a
soma dos quadrados dos seus elementos ímpares. A sua função deve conter
apenas uma instrução, a instrução `return`. Não é necessário validar os
dados de entrada. Por exemplo:
```
>>> soma_quadrados_impares([1, 2, 3, 4, 5, 6])
35
```

## ex06
Considere a seguinte definição do predicado `eh_primo` que tem o valor
verdadeiro apenas se o seu argumento é um número primo:
```python
def eh_primo(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True
```
Escreva a função de ordem superior, `nao_primos` que recebe um número
inteiro positivo, `n`, e devolve todos os números inferiores ou iguais a `n`
que não são primos. A sua função deve conter apenas uma instrução, a
instrução return. Por exemplo,
```
>>> nao_primos(10)
[1, 4, 6, 8, 9, 10]
```

## ex07
Considere a seguinte função que recebe como argumentos um número natural, `n`, e um predicado de um argumento, `p`:
```python
def misterio(num, p):
    if num == 0:
        return 0
    elif p(num % 10):
        return num % 10 + 10 * misterio(num // 10, p)
    else:
        return misterio(num // 10, p)
```
- (a) Explique o que faz esta função.
- (b) Utilize a função `misterio` para escrever a função `filtra_pares` que
recebe um número inteiro e devolve o número obtido a partir dele
que apenas contém dígitos pares. A sua função deve conter apenas
uma instrução, a instrução `return`. Por exemplo,
```
>>> filtra_pares(5467829)
4682
```

## ex08
Usando funcionais sobre listas, escreva a função `lista_digitos`, que recebe um inteiro positivo `n` e devolve a lista cujos elementos são os dígitos
de `n`. A sua função deve conter apenas uma instrução, a instrução `return`.
Sugestão: transforme o número numa cadeia de caracteres. Por exemplo:
```
>>> lista_digitos(123)
[1, 2, 3]
```

## ex09
Usando a função `lista_digitos` do exercício anterior e funcionais sobre listas,
escreva a função `produto_digitos`, que recebe um inteiro positivo, `n`, e
um predicado de um argumento, `pred`, e devolve o produto dos dígitos de
n que satisfazem o predicado `pred`. A sua função deve conter apenas uma
instrução, a instrução `return`. Por exemplo:
```
>>> produto_digitos(12345, lambda x : x > 3)
20
```

## ex10
Usando a função `lista_digitos` do exercício 8 e funcionais sobre listas,
escreva a função `apenas_digitos_impares`, que recebe um inteiro positivo, `n`, e devolve o inteiro constituído pelos dígitos ímpares de `n`. A
sua função deve conter apenas uma instrução, a instrução `return`. Por
exemplo:
```
>>> apenas_digitos_impares(1234567890)
13579
```

## ex11
Usando *closures* escreva uma função chamada `incrementa` que recebe um
inteiro e devolve uma função de um só parâmetro que incrementa o seu
argumento do valor passado à função `incrementa`. Por exemplo,
```
>>> f = incrementa(12)
>>> f(8)
20
>>> f(20)
32
```

## ex12
Usando *closures* escreva uma função chamada `intervalo` que recebe dois
inteiros e devolve uma função de um só parâmetro que verifica se o seu
argumento se encontra entre os dois valores passados à função `intervalo`,
inclusivé. Por exemplo,
```
>>> f = intervalo(12, 20)
>>> f(8)
False
>>> f(20)
True
```

## ex13
Usando *closures* escreva uma função chamada `tabuada` que recebe um
inteiro e devolve uma função de um só parâmetro que calcula o produto
do seu argumento pelo valor passado à função `tabuada`. Por exemplo,
```
>>> f = tabuada(7)
>>> f(8)
56
>>> f(6)
42
```

## ex14
Usando *closures* escreva uma função chamada `polinomio` que recebe três
valores reais correspondentes aos fatores de um polinómio de grau 2,
por ordem crescente do grau, e devolve uma função de um só parâmetro que
calcula o valor do polinómio no ponto dado pelo seu argumento.
Por exemplo,
```
>>> f = polinomio(12, 3, 4)
>>> f(2)
34
>>> f(3.4)
68.44
```

## ex15
Usando *closures* escreva uma função chamada `index` que recebe uma
lista de valores e devolve uma função de um só parâmetro que retorna
o índice da primeira ocorrência do seu argumento na lista fornecida à
função `index`. A função deve devolver
`-1` se o valor não existir na lista. Por exemplo,
```
>>> f = index([3, 5, 7, 9, 11, 17])
>>> f(11)
4
>>> f(4)
-1
```

## ex16
Usando *closures* escreva uma função chamada `segment` que recebe
um intervalo sob a forma de uma lista, com dois valores numéricos
por ordem crescente, e devolve uma função de um só parâmetro que
atualiza os extremos do intervalo fornecido à função `segment` por
forma a este conter o valor recebido como argumento.
A função `segment` deve garantir a consistência dos seus argumentos
e devolver uma exceção `ValueError` com a mensagem `argumentos inválidos`
caso o argumento não obedeça às especificações acima. Por exemplo,
```
>>> f = segment(3, 4)
>>> f(3)
[3, 4]
>>> f(2)
[2, 4]
>>> f(6)
[2, 6]
```

## ex17
Usando *closures* escreva uma função chamada `acumula` que recebe
uma lista de valores e devolve uma função que soma o seu argumento
a todos os elementos da lista. Por exemplo,
```
>>> f = acumula([1, 2, 3])
>>> f(2)
[3, 4, 5]
>>> f(4)
[7, 8, 9]
>>> f(-12)
[-5, -4, -3]
```

## ex18
Usando *closures* escreva uma função chamada `atualiza` que recebe um
dicionário e devolve uma função de dois parâmetros que atualiza o valor
associado à chave no dicionário, retornando o antigo valor associado à
chave.  Por exemplo,
```
>>> d = {}
>>> x = atualiza(d)
>>> x('a',2)
>>> d
{'a': 2}
>>> x('b',3)
>>> d
{'a': 2, 'b': 3}
>>> x('b',5)
3
>>> d
{'a': 2, 'b': 5}
```

## ex19
Usando *closures* escreva uma função chamada `acrescenta` que recebe um
dicionário de listas e devolve uma função de dois parâmetros que
acrescenta o valor à lista associada à chave no dicionário,
retornando o comprimento da lista resultante. Por exemplo,
```
>>> d={}
>>> x=acrescenta(d)
>>> x('a',2)
1
>>> x('a',21)
2
>>> x('a',12)
3
>>> d
{'a': [2, 21, 12]}
```

## ex20
Usando *closures* escreva uma função chamada `substitui` que recebe um
dicionário e devolve uma função de dois parâmetros que subsitui uma chave
no dicionário por uma nova chave. Se a nova chave já existir,
a função deve retornar o antigo valor associado à chave. Por exemplo,
```
>>> d={'a':1, 'b':2, 'c':3}
>>> x=substitui(d)
>>> x('b', 'x')
2
>>> d
{'a': 1, 'c': 3, 'x': 2}
```
