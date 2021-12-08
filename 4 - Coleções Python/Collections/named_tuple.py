"""


"""

tupla = (1,2,3)
print(tupla[0])

#Named Tuple -> São tuplas onde, especificamos um nome para a mesma e tambem parametros.

#Importando
from collections import namedtuple

#Precisamos definir nome e parametros

#Forma 1 - Declaração named tuple
cachorro = namedtuple('cachorro','idade raca nome')

#Forma 2 - Declaração named tuple
cachorro = namedtuple('cachorro','idade, raca, nome')

#Forma 3 - Declaração named tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

frezza = cachorro(idade=2, raca='Pitbull', nome='Frezza')
print(frezza)


#Acessando os dados 

#Forma - 1

print(frezza[0]) #idade

#Forma - 2

print(frezza.idade)