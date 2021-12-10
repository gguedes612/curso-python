"""
Entendo o *args

- O *args é um parametro, como outro qualquer, isso significa que voce poderar chamar de qualquer coisa, desde que comece com asterisco.

EX: *xis mas por converção, utilizamos *args para defini-lo

O parametro *args utilizando em ma funcao, coloca os valores extras informados como entrada em uma tupla.

"""

def soma_todos_parametro(*args):
    return sum(args) 

print(soma_todos_parametro(1,3,6))


lista = [1,2,3,4,5,6,7,8,9]
print(soma_todos_parametro(*lista)) 

"""
O asterisco serve para que informamos ao python que estamos passando como argumento uma coleção de dados. DEsta forma, ele sabera que precisara antes, desempacotar esses dados.
"""