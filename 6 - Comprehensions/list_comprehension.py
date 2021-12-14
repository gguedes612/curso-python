"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iteravel.

Sintaxe de List Comprehension

[ dado  for dado in interavel ]

"""

numeros = [1,2,3,4,5,6]

res = [numero * 10 for numero in numeros]

print(res)

"""
Para entender melhor o que esta acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10
"""


#List Comprehensions VS Loop

res2 = []
for i in numeros:
    res2.append( i * 10)
print(res2)

#Outros exemplo
nome = "Guilherme de Lima Guedes"

print([letra.upper() for letra in nome])

################################################

amigos = ['guilherme', 'finho', 'joão', 'maria']

def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

print([caixa_alta(amigo) for amigo in amigos])

"""
Podemos Adicionar estruturas condicionais logicas as nossas List Comprehension
"""

#Exemplos

pares = [ numero for numero in numeros if not numero % 2] # 0 no Python é False
impares = [ numero for numero in numeros if numero % 2] # 1 em Python é True

print(pares)
print(impares)

################################################

res = [ numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)