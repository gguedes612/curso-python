"""
Any e All

all() retorna True se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel esta vazio.

any() retorna True se qualquer elemento do iteravel for verdadeiro, Se o iteravel estiver vazio, retorna False
"""

#Exemplo all

print(all([0,1,2,3,4])) #Lista com 0 que é False

print(all([1,2,3,4])) # Lista apenas com True

lista = [1,2,3,4]
lista2 = [-1,2,-3,-4]


print(all([numero > 0 for numero in lista]))

print(any([numero > 0 for numero in lista]))
