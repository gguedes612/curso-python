"""
Min e Max

max() -> Retorna o maior valor em um iteravel ou o maior de dois ou mais elementos.
max() -> Retorna o menor valor em um iteravel ou o menor de dois ou mais elementos.


"""

lista = [1,2,3,4,5,6,10]
print(max(lista)) #IDEPENDENTE DA COLEÇÃO

#Min e max com string
nomes = ['Arya','Guilherme', 'Jefferson', 'Maria']

print(max(nomes))
print(min(nomes))

print(max(nomes,key=lambda nome: len(nome)))
print(min(nomes,key=lambda nome: len(nome)))
