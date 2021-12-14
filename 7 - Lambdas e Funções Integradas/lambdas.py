"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja, funções anonimas.

"""
#Funções em Python
def funcao(x):
    return 3 * x + 1

print(funcao(4))

#Expressão Lambda
lambda x: 3 * x + 1

#Como utilizar a expressão Lambda
calculo = lambda x: 3 * x + 1
print(calculo(4))


# Podemos ter expressões Lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('guilherme','guedes'))

nomes = ['Guilherme Guedes', 'Jefferson Richard', 'Maria Clara', 'João Gabriel', 'Marcio Costa', 'Luiz Henrique']

nomes.sort(key=lambda nome: nome.split(' ')[0].lower())

print(nomes)