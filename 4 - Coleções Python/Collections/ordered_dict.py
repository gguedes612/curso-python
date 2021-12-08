"""


"""
#Em um dicionario, a ordem de inserção dos elementos nao é garantida.
dicionario = {'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6}

for chave, valor in dicionario.items():
    print(f'Chave = {chave} Valor = {valor}')


#Fazendo import

from collections import OrderedDict

#Ordered Dict -> É um dicionario que nos garante a ordem de inserção dos elementos.
dict = OrderedDict({'a': 1,'b': 2,'c': 3,'d': 4,'e': 5,'f': 6})

for chave, valor in dict.items():
    print(f'Chave = {chave} Valor = {valor}')