"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas;

A função reverse só funiona em listas, já a função reversed() funciona com qualquer iteravel. 

Sua função é inverter um iteravel.

A função reversed() retorna um iteravel chamado List Reverse Iterator
"""

lista = [1,2,3,4,5,6]

res = reversed(lista)

print(res)
print(type(res))

#Podemos converter o elemento retornando para uma lista, tupla e etc.+
print(list(reversed(lista)))

#Iteravel
for letra in reversed('Guilherme Guedes'):
    print(letra, end='')
print()
