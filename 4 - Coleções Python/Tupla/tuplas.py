"""
Tuplas

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças basicas:

1 - As tuplas são representadas por parenteses []
2 - As tuplas são imutaveis: isso significa que ao se criar uma tupla ela nao se muda. Toda operação em uma tupla gera uma nova tupla.


"""

print(type(()))

#Cuidado 1: As tuplas são representadas por (), mas veja:
tupla1 = (1, 2, 3, 4, 5)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5
print(tupla2)
print(type(tupla2))

#Cuidado 2: Tupla com 1 elemento

tupla3 = (1) # NÃO É UMA TUPLA
print(tupla3)
print(type(tupla3))

tupla4 = 1, # É UMA TUPLA
print(tupla4)
print(type(tupla4))

tupla5 = (1,) # É UMA TUPLA
print(tupla5)
print(type(tupla5))

# Podemos concluir que tuplas são definidas pela virgula e não pelo uso do parenteses()


#Gerando tupla com range
tupla6 = tuple(range(11))
print(tupla6)

#Desempacotamento de tupla
tupla7 = ('Guilherme', 'Guedes')
nome, sobrenome = tupla7
print(nome)
print(sobrenome)

# Métodos para: adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutaveis.

# Soma, Valor Máximo, Valor Mínimo e Tamanho

tupla8 = 1, 2 , 3, 4, 5, 6

print(sum(tupla8))
print(max(tupla8))
print(min(tupla8))
print(len(tupla8))

# Concatenação de tuplas

tupla9 = 1, 2, 3
tupla10 = 4, 5, 6
tupla9 = tupla9 + tupla10 # Tuplas são IMUTAVEIS mas podemos sobrescrever seus valores
print(tupla9)

# Verificar se determinado elemtno esta contido na tupla

print( 3 in tupla9)

#Iterando sobre uma tupla

for i, value in enumerate(tupla9):
    print(i,value)

#Contando elementos dentro d uma tupla

tupla11 = tuple('Guilherme Guedes')
print(tupla11)
print(tupla11.count('e'))

"""
Dicas de utilização de tuplas
Devemos utilizar as tuplas sempre que não precisamos modificar os dados contidos em uma coleção, por exemplo: meses do ano e etc
"""

# Verificar indice de um elemento
print(tupla11.index('e'))

#Slicing tupla[INICIO:FIM:PASSO]
 