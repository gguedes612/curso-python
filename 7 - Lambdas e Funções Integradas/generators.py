"""
Generatirs
Em aulas anteriores nós estudamos:
 - List Comprehension;
 - Dictionary Comprehension;
 - Set COmprehension;

 Não vimos:
 - Tuple Compregension porque elas se chamam Generators

nomes = [ 'Guilherme', 'Maria', 'Rikinho', 'Jefferson']
print(any(nome[0] == 'G' for nome in nomes  ))
"""
nomes = [ 'Guilherme', 'Maria', 'Rikinho', 'Jefferson']

#Utilizando Comprehension
res = (nome[0] == 'G' for nome in nomes)
print(type(res))

#Utilizando Generator
res = [nome[0] == 'G' for nome in nomes]
print(type(res))

#GENERATOR É SEMPRE MAIS PERFORMATICO DO QUE O COMPREHENSION