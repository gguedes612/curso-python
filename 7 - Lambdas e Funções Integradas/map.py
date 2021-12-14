"""
Map

Com map, fazemos mapeamento de valores para função.
"""

import math

def area(r):
    """Calcula a area de um circulo recebendo raio 'r'."""
    return math.pi * (r ** 2)

print(area(2))


raios = [numeros for numeros in range(5,11)]
areas = []

#Forma 1 - For
for raio in raios:
    areas.append(area(raio))
print(areas)

areas = []

#Forma 2 - Map
areas = list(map(area,raios)) 
print(areas)


#Forma 3 - Map com lambda
areas = list(map(lambda raio: math.pi * (raio ** 2),raios))
print(areas)