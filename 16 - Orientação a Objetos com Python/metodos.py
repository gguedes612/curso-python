"""
POO - Metodos

- Metodos (Funções) - Representam so compotamentos dos objetos, ou seja, as acções que esse objeto pode realizar no seu sistema.

Em python, dividimos os metodos, em 2 grupos: Metodos de Instancia e Metodo de Classe.


__init__ -> O metodo __init__ é um metodo especial chamado de construtor e sua função é construir o objeto a partir da classe.
"""

class Lampada:

    def __init__(self,cor,voltagem,luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade

class ContaCorrente:
    
    contador = 1000

    def __init__(self,limite,saldo,senha):
        self.__id_conta = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__senha = senha

        ContaCorrente.contador += 1
    
    def __validar_senha(self):
        "Valida a senha para utilização de outros metodos"
        
        senha = int(input('Digite a senha para proseguir: '))
        if senha == self.__senha:
            print('Senha valida')
            return True
        else:
            print('Senha invalida')
            return False

    def aumentar_limite(self,porcetagem_aumento):
        """Aumenta o limite da conta baseado em porcetagem (recebe apenas valores inteiros)"""
        
        self.__limite += self.__limite * ( porcetagem_aumento / 100 )

    def consulta(self):
        """Consulta Saldo e Limite da Conta"""
        
        if self.__validar_senha():
            print(f'Conta {self.__id_conta} com saldo de {self.__saldo} e limite de {self.__limite}')
        


conta1 = ContaCorrente(1000,2000,123)
conta1.aumentar_limite(20)
conta1.consulta()
