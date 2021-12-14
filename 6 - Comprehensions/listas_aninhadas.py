"""
Listas Aninhadas

- Algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays / Vetores);
    - Multidimensionais (Matrizes).

Em Python nós temos as Listas

numeros = [1,2,3,4,5] LISTAS


"""

matriz = [[1,2,3], [4,5,6], [7,8,9]]

#Vendo Conteudo da matriz

print(matriz[0][2]) # matriz[linha][coluna]


#Indice
for i in range(3):
    for j in range(3):
        print(matriz[i][j],end=' ') 
    print()

print()

#Metodo Python
for lista in matriz:
    for numero in lista:
        print(numero,end=' ')
    
    print()

print()

#List Comprehension
[[print(valor) for valor in lista] for lista in matriz]

#Gerando matrizes com comprehension

matriz =  [[numero for numero in range(1,4)] for valor in range(1,4)]
print(matriz)