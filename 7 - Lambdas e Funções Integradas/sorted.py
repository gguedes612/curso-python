"""
Sorted

OBS: Não confunda com a função sort() que usamos em listas. O sort() só funciona em listas.

Podemos usar o sorted() com qualquer iteravel

Como o proprio nome diz, sorted() serve pra ordenar. 

OBS: O sorted sempre retorna uma Lista com os elementos do iteravel ordenados
"""

#Exemplo
numeros = [ 6,1,2,3,5,4]
print(sorted(numeros))
print(numeros)
print(type(numeros))


numeros = (6,1,2,3,5,4)
print(sorted(numeros))
print(numeros)
print(type(numeros))



print(sorted(numeros, reverse=True))


paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos', 'ARG': 'Argentina', 'ALM': 'Alemanha'} 

print(paises)
print(sorted(paises))