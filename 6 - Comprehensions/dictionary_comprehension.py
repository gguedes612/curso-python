"""
Dictionary Comprehension

Criando lista:

lista = [1,2,3,4,5,6]

Sequisermos Criar uma tupla:

tupla = (1,2,3,4,5,6)

Se quiser criar um conjunto

conjunto = {1,2,3,4,5,6}

Criando um dicionario

dicionario = {'a': 1, 'b': 2, 'c':3}

Sintaxe

{chave:valor for valor in interavel} #Dicionario
"""

#Exemplos

dicionario = {'a': 1, 'b': 2, 'c':3}

quadrado = {chave:valor ** 2 for chave, valor in dicionario.items()}

print(dicionario)
print(quadrado)

#Criando Dicionario

chave = 'abcdef'
lista = [1,2,3,4,5,6]

dicionario = {chave[i]:lista[i] for i in range(len(chave))}

print(dicionario)