#Printando lista
lista = [2, 1, 5, 3, 8, 3, 8, 4, 3]

#Percorrendo lista
for i in range(len(lista)) :
    print(lista[i])

#Condicional com lista
if 2 in lista:
    print("Existe o elemento 2 na lista")
else:
    print("Não existe o elemento 2 na lista")

#Ordenar lista
lista.sort()

#Contar elemento na lista
print(lista.count(3))

#Adicionar um unico elemento na lista
lista.append(1)

#Adicionando lista dentro de outra lista, como elemento unico
lista.extend([1,2,3,4])

#Inserir valor no index
lista.insert(2,"Novo valor")

#Ordenar a lista reversa
lista.reverse()
print(lista[::-1])

#Copiar uma lista
listanova = lista.copy()

#Contar elementos de uma lista
print(len(lista))

#Remover ultimo elemento e retorna o ultimo elemento, pode passar um index como parametro
lista.pop()

#Remover todos os elementos de uma lista
lista.clear()

#Separando em lista string
frase = "meu nome"
frase = frase.split()
print(frase)

#Convertendo uma lista em uma string

listastring = ["Programação", "em", "Python"]
listastring = ' '.join(listastring)

#Ver index de um elemento OBS: Primeiro elemento encontrado
print(lista.index(3))

#Slicing
# Lista/range[inicio:fim:passo]

print(sum(lista))   #Soma
print(max(lista))   #Valor maximo
print(min(lista))   #Valor minimo
print(len(lista))   #Tamanho da lista

print(lista)
print(listastring)