"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso codigo dentro de um grupo logico e hierarquico utilizando classes.


Encapsular -> capsula


Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e metodos privados de usuario.  q
"""


class Conta:

    contador = 100

    def __init__(self,nome_titular,saldo,limite):
        self.__numero = Conta.contador
        self.__nome_titular = nome_titular
        self.__saldo = saldo
        self.__limite = limite

        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de R${self.__saldo} do titular {self.__nome_titular} com limite de R${self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f'Valor depositado de R${valor}.')
        else:
            print('Digite um valor positivo para depositar')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo > valor:
                self.__saldo -= valor
                print(f'Valor sacado de R${valor}.')
            else:
                print('Valor de saque indisponivel, verifique o seu saldo.')
        else:
            print('Digite um valor positivo para sacar')

    def pix(self,valor,conta_destino):
        self.__saldo -= valor
        conta_destino.__saldo += valor
        print('Transferencia concluida.'')


conta1 = Conta('Guilherme',1500,1000)
conta2 = Conta('Jefferson',300,2000)

conta1.pix(500,conta2)
conta1.extrato()