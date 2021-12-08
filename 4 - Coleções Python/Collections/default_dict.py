
dicionario = {'curso': 'Python'}

print(dicionario)

print(dicionario['curso'])

#print(dicionario['outro']) KeyError

"""Default Dict -> Ao criar um dicionaro utilizando-o, nos informamos um valor default, podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver um valor definido. Caso tentemos acessar uma chave que nao existe, essa chave será criada e o valor default sera atribuido.

OBS: Lambdas são funções sem nome, que pode ou nao receber parametros de entrada e retornar valores."""

#Fazendo import
from collections import defaultdict

dict = defaultdict(lambda: 0)
print(dict)

dict['curso'] = 'Teste'
print(dict)

print(dict['outro']) # Em um dicionario normal daria erro pos a chave nao existe
print(dict)