class Elevador():

    def __init__(self,capacidade,andares_predio) -> None:
        self.__andar_atual = 0
        self.__qtde_pessoas = 0
        self.__andares_predio = andares_predio
        self.__capacidade = capacidade

    
    def entra(self,numero_pessoas):
        if (self.__qtde_pessoas + numero_pessoas) > self.__capacidade:
            print(f'Quantidade maxima de pessoas não permitida, quantidade maxima de: {self.__capacidade} Pessoas')
        else:
            self.__qtde_pessoas += numero_pessoas
            print(f'Capacidade atual {self.__qtde_pessoas}')
        
    def sai(self):
        if self.__qtde_pessoas > 0:
            self.__qtde_pessoas -= 1
            print(f'Capacidade atual {self.__qtde_pessoas}')
            
        else:
            print('Elevador Vazio')

    def sobe(self):
        if self.__andar_atual == self.__andares_predio:
            print(f'Estamos no ultimo andar')
        else:
            self.__andar_atual += 1 
            print(f'Andar Atual {self.__andar_atual}')
    

    def desce(self):
        if self.__andar_atual == 0:
            print(f'Estamos no terreo')
        else:
            self.__andar_atual -= 1
            print(f'Andar Atual {self.__andar_atual}')

