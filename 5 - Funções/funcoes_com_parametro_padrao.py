"""
Funções com parametro padrao (Default Paramters)

-   Funções onde a passagem de parametros seja opcional;
    Como por exemplo o print()
"""


def exponencial( numero, potencia ):
    return numero ** potencia

print(exponencial(3,2))


#Refatorando a função

def exponencial( numero, potencia = 2 ): # Definiciu o valor 2 como valor padrão para o parametro
    return numero ** potencia

print(exponencial(3))


#En funções Python, os parametros com valores default (padrão) DEVEM sempre estar ao final da declaração 

#Exemplo

def mat(num1, num2, funcao=exponencial):
    return funcao(num1, num2)

print(mat(2,2))

"""

Escopo

    - Variaveis globais
    - Variaveis locais
        - Variaveis locais tem preferencia do que variaveis globais
        - Variaveis locais são usadas apenas no seu escopo de função
"""