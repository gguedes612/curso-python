"""
Funções com Retorno
  
Em Python quando uma função não retorna nenhum valor, o retorno é None

"""

def diz_oie(): 
    print('oie')

diz_oie()

#Refatorar a função para que ela retorne o valor 
def diz_oie(): 
    return 'oie'

print(diz_oie())

"""

Sobre o Return
- Ela finaliza a função;
- Podemos ter em uma função mais de um return;
- Podemos em uma função retornar qualquer tipo de dado e até mesmo multiplos valores.

"""