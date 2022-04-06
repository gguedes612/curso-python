

class Agenda:

    def __init__(self):
        self.__pessoas = []
    
    def armazena_pessoas(self,nome,idade,altura):

        self.__pessoas.append({'nome': nome, 'idade': idade, 'altura':altura})

    def imprime_agenda(self):
        for pessoas in self.__pessoas:
            print(pessoas)

    def busca_pessoa(self,nome):
        contador = 1
        for pessoa in self.__pessoas:
            if pessoa['nome'] == nome:
                print(f'{nome} é o numero {contador}º da lista.')

            contador += 1
    
    def imprime_pessoa(self,index):
        contador = 1
        for pessoa in self.__pessoas:
            if contador == index:
                print(pessoa)

            contador += 1

minha_agenda = Agenda()

minha_agenda.armazena_pessoas('Guilherme',20,1.80)
minha_agenda.armazena_pessoas('Jefferson',22,1.75)
minha_agenda.imprime_agenda()
minha_agenda.busca_pessoa('Jefferson')
minha_agenda.imprime_pessoa(1)