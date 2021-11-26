"""
Conjuntos:

- Conjuntos em qualquer linguagem deprogramação, estamos fazendo referencia a teoria dos conjuntos da matematica;
- No Python os conjuntos são chamados de Sets;
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja , conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves/valores/itens duplicados.

Os conjuntos (sets) são referenciados em python com chaves {}

Diferença entre Conjuntos(Sets) e Mapas(Dicionarios) em Python:
- Um dicionario tem chave/valor
- Um conjunto te apenas valor

"""

#Definindo um conjunto

#Forma1
conjunto = set({1, 2, 2, 2, 3, 6, 7}) #Repare que temos valores repetidos, ao criar um conjunto com valores repetidos o mesmo sera ignorado sem gerar erro e não fará parte do conjunto
print(conjunto)
print(type(conjunto))

#Forma2

conjunto2 = {1, 11, 9, 7, 14, 6, 7}
print(conjunto2)
print(type(conjunto2))

#Verificando elemento no conjunto
if 3 in conjunto:
    print('Existe o 3')
else:
    print('Existe não vei')

#Podemos adicionar todos os tipos de dados em um conjunto
conjunto3 = {13, 'Vasco', True}
print(conjunto3)
print(type(conjunto3))

#Podemos interar os valores em um conjunto
for i in conjunto3:
    print(i)

#Adicionando Elementos em um conjunto
conjunto3.add(12)
conjunto3.add(13) # Elementos Repetidos não adiciona e não gera erro
print(conjunto3)

#Removendo valores

#Forma 1
conjunto3.remove(12) #Remove o elemento e não o indice, se for usado um elemento que não existe no conjunto, gera erro
print(conjunto3)

#Forma 2
conjunto3.discard(13) # Se o elemento não for encontrado, não gera erro
print(conjunto3)

#Removendo itens de um conjuto
conjunto3.clear()
print(conjunto3)

#Metodos Matematicos em um conjunto

# Elementos unicos em um conjunto


#Forma 1 - Union
conjunto3.clear() 
conjunto3 = conjunto.union(conjunto2)
print(conjunto3)

# Forma 2 Utilizando um pipe
conjunto3.clear()
conjunto3 = conjunto | conjunto2
print(conjunto3)

#Elementos incluso nos dois conjuntos

#Forma 1 - Intersection
conjunto3.clear()
conjunto3 = conjunto.intersection(conjunto2)
print(conjunto3)

# Forma 2 - Utilizando um &
conjunto3.clear()
conjunto3 = conjunto & conjunto2
print(conjunto3)


#Elementos que estão em um conjunto mas não estão no outro
conjunto3.clear()
conjunto3 = conjunto.difference(conjunto2)
print(conjunto3)

#Soma, Valor maximo, Valor Minimo, tamanho
print(sum(conjunto3))
print(max(conjunto3))
print(min(conjunto3))
print(len(conjunto3))
