"""

Definindo Funções

- Funções são pequenos trechos de codigo que realizam tarefas especificas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

Já utilizamos varias funções desde que iniciamos este curso.
    - print()
    - len()
    - max()
    - min()

"""

#Utilizando função

cores = ['amarelo','azul','vermelho']

#Utilizando uma função python
print(cores)


"""

Definindo função em Python
def nome_funcao(parametros_de_entrada):
    bloco_da_funcao

nome_da_funcao -> Sempre, com letras minusculas, e se for nome composto separado por underline (Snake Case);
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por virgula, podendo ser opcionais ou não;
bloco_da_funcao -> tambem chamado de corpo da função ou umplementação, é onde o processamento da função acontece. Pode se ter ou não retorno na função.

"""

#Definindo função
def diz_oie(): # Não recebe nenhum parametro de entrada
    print('oie') #Podemos utilizar funcoes dentro de outras funcoes
    #Não existe retorno na função

#Chamada de execução
diz_oie() #Funções só executam uma unica tarefa

#Chamando atravez de variavel
fala = diz_oie
fala()