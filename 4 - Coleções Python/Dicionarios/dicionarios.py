"""
Dicionarios:

OBS: Em algumas linguagens de programação, os dicionarios Python são conhecidos por mapas.

Dicionarios são coleções do tipo chave/valor.
OBS: 
    - Chave e valor são separados por dois pontos ':';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Dicionarios são representados por chaves{}
    - Podemos misturar tipos de dados
"""

print(type({}))

#Criando dicionarios

#Forma 1
paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos'} 
print(paises)
print(type(paises))

#Forma 2
paises2 = dict(BR='Brasil', EUA='Estados Unidos')
print(paises2)
print(type(paises2))

#Acessando Elementos

#Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['BR'])

#Forma 2 - Acessando via get

print(paises.get('BR'))

#Podemos Verificar se determinada chave se encontra em um dicionario

if 'EUA' in paises:
    print(paises.get('EUA'))

#Adicionando dados em um dicionario

# Forma 1
nova_dado = {'AR': 'Argentina'}

paises.update(nova_dado) # paises.update({'AR': 'Argentina'})

# Forma 2

paises['KR'] = 'Coreia do Sul'

#Atulizando dados de um dicionario

#Forma 1

paises['KR'] = 'Republica da Coreia'

#Forma 2

paises.update({'AR': 'Argentina'}) 

""""
OBS: 
    - O mesmo metodo que adiciona é o mesmo que atualiza
    - Não se pode repetir o valor da chave
"""

#Remover dados de um Dicionario

paises.pop('KR') # Obrigatorio passar chave e valor do objeto é retornado
print(paises)

#Exemplo carrinho de compras
carrinho = []

produto1 = {'Nome': 'EspertoFone', 'Quantidade': 1, 'Preço': 2300.00}
produto2 = {'Nome': 'FoneDeUvido', 'Quantidade': 1, 'Preço': 230.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#Criação diferente de dicionario

usuario = {}.fromkeys(['Nome', 'CPF', 'RG'], None)
print(usuario)

teste = {}.fromkeys((range(10)), None)
print(teste)