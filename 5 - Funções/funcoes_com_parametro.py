"""
Funções com Parametros de entrada

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saida

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas nao possuem saida;
- Não possuem entrada mas possuem saida;
- Possuem entrada e saida;

"""

#Refatorando uma função
def quadrado(numero):
    return numero * numero

print(quadrado(5))

#Funções podem ter n parametros de entrada. Ou seja, podemos receber como enbtrada em uma função quantos parametros forem necessarios. Eles são separados por virgula.

def soma( a , b ):
    return a + b

print(soma( 1 , 1 ))

def soma( a , b , c ):
    return a + b + c

print(soma( 1 , 1 , 1 ))

"""

Diferenciando parametros e Argumento
- Parametros são variaveis declaradas na definição de uma função
- Argumentos são dados passados durante a execução de uma função


Argumentos nomeados (Keyword Arguments)

Caso utilizemos nomes dos parametro nos argumentos para informalos, podemos utilizar qualquer ordem

"""
#Alterando a ordem de recebimento de parametros.
print(soma(a=10,c=20,b=1))

