class Pessoa:

    def __init__(self,nome,idade,altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def imprimir_dados(self):
        print(f'Nome: {self.__nome}')
        print(f'Idade: {self.__idade}')
        print(f'Altura? {self.__altura}')

    def redefinir_altura(self,nova_altura):
        self.__altura = nova_altura
    
    def redefinir_idade(self,nova_idade):
        self.__idade = nova_idade

    def redefinir_nome(self,novo_nome):
        self.__nome = novo_nome

    
guilherme = Pessoa('Guilherme',20,1.80)

guilherme.imprimir_dados()

guilherme.redefinir_nome('Jefferson')
guilherme.redefinir_idade(22)
guilherme.redefinir_altura(1.75)

guilherme.imprimir_dados()