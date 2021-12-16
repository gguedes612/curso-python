"""
Reduce

A partir do Python3 a função reduce() não é mais uma função integrada. Agora temos que importar e utilizar essa função a partir do modulo 'funtools'

Para entender o reduce()

Imagine que voce tem uma coleção de dados:

dados = [n1, n2 ,n3 ...]

E voce tem um funçãoq ue recebe dois parametros:

def funcao(x,y):
    return x * y
    
Assim como map() e filter(), a função recebe dois parametros: a função e o iteravel.

reduce(função , dados)

reduce vai usar todos os valores do interavel para iteragir com a função, recebendo dois parametros na função.

n1 n2
res1 n3
res2 n4 ...

"""

import functools
dados = [numero for numero in range(20)]

soma_dados = functools.reduce(lambda x , y: x + y, dados)
print(soma_dados)