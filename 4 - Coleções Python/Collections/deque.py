"""
Deque -> Lista de alta performace

"""
#Importando
from collections import deque

#Criando deque
deq = deque('deque')
print(deq)

#Adicionando elementos no deque
deq.append('Y') #Adiciona no final

deq.appendleft('Z') #Adiciona no começo da lista

#Remover Elementos

deq.pop() #Remove e retorna o ultimo elemento

deq.popleft() #Remove o elmento inicial
