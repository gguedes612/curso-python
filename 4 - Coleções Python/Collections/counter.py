"""
Counter -> (Contador)
Collections -> High-performace Container Datetypes

Counter -> Recebe um interavel como parametro e cria um objeto do tipo Collections Counter que é parecido com um dicionario, contendo como chave o elemento da lista passa como parametro e como valor a quantidade de ocorrencias desse elemento.


"""

#Realizando import
from collections import Counter

#Podemos utilizar qualquer iterabel, aqui usamos uma Lista
lista = [1,1,1,3,3,1,4,4,1,6,1,6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

#Utilizando o Counter
resultado = Counter(lista)
print(type(resultado))
print(resultado)

#Para cada elemento da lista o Counter criou uma chave e colocou como valor a quantidade de ocorrencias.

#Utilizando string
print(Counter('Guilherme de Lima Guedes'))

#Contando palavras
texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas sapien elit, maximus a est a, tristique ornare est. Mauris placerat auctor tempor. In consectetur magna sit amet sollicitudin auctor. Proin sit amet purus vitae sapien sagittis luctus. Maecenas lectus est, vulputate nec accumsan non, mollis nec sem. Morbi in tempus dolor, vitae posuere ante. Suspendisse tempor dolor felis, at volutpat justo sollicitudin id. Quisque et augue fermentum, sollicitudin mauris vel, dignissim tortor. Praesent sagittis purus nec mauris auctor, eu aliquam nisi egestas. Vivamus efficitur mi ipsum, sit amet rhoncus magna molestie non. Ut interdum tortor risus, nec lobortis tortor vestibulum eu."

palavras = texto.split(" ")

resultado = Counter(palavras)

print(resultado)