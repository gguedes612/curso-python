"""
Filter 

filter() -> Serve para filtrar dados de uma determinada coleção.
"""
#Biblioteca para trabalhar com dados estatisticos
import statistics

#Dados coletados
dados = 1,2,3,4,5,6

#Calculando a media dos dados utilizando mean
media = statistics.mean(dados)

#OBS: Assim como a função map(), a filter() recebe dois parametros, sendo uma função e um iteravel.

resultado = list(filter(lambda valor: valor > media, dados))

print(resultado)

paises = ['','Argentina', '', 'Brasil','','','EUA']
paises = list(filter(None,paises))
print(paises)