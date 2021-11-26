"""
Mapas -> Conhecidos em Python como Dicionarios

Dicionarios em Python são representados por chaves {}


"""

paises = {'BR': 'Brasil', 'EUA': 'Estados Unidos'} 

#Interar sobre dicionarios
for chave in paises:
    print(chave)

for chave in paises:
    print(paises[chave])

for chave in paises:
    print(f'{chave}: {paises[chave]}')

#Acessando as chaves
print(paises.keys())

#Acessando os valores
print(paises.values())

#Desempacotando de dicionarios
for chave, item in paises.items():
    print(f'{chave}: {item}')


#Soma, Valor maximo, Valor Minimo, tamanho
print(sum(paises.values()))
print(max(paises.values()))
print(min(paises.values()))
print(len(paises.values()))
