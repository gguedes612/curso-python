"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto. Ou seja, pelo atributos nós conseguimos representar computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instancia;
    - Atributos de Classe;
    - Atributos Dinamicos;

# Atributos de Instância: São atributos declarados dentro do metodo construtor.

OBS: Metodo construtor é um metodo especial utilizado para a construção de um objeto.

"""


class Lampada:

    #Metodo Construtor!!
    def __init__(self,voltagem,cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False

class ContaCorrente:

    def __init__(self,numero,limite,saldo) -> None:
        self.numero = numero
        self.limite = limite
        self.saldo = saldo

#Atributos Publicos ou Privados 

class Acesso:
    
    def __init__(self,email,senha):
        self.email = email      #Publico 
        self.__senha = senha    #Privado


user1 = Acesso('user@gmail.com','senha123')

#print(user1.__senha) AtributeError


"""
O que Significa atributos de instancia??

Significa, que ao criarmos instancias/objetos de uma classe, todas as instancias terão esses atributos.

"""


#Atributos de Classe -> são atributos que são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já inicializamos um valor, e este valor é compartilhado entre todas as instancias da classe, ou seja, ao inves de cada instancia de classe ter seus proprios valores como é o caso dos atributos de instancia, com os atributos de classe todas as instancias terão o mesmo valor para esse atributo.

class Produto:
    
    #Atributo de Classe
    imposto = 1.05
    id_produto = 0
    
    def __init__(self,nome,descricao,valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor * Produto.imposto
        self.id_produto = Produto.id_produto
        Produto.id_produto += 1

    

p1 = Produto('Carro','É um carro mzr o que faz?',100)
p2 = Produto('Moto','É um carro mzr o que faz?',100)

print(p1.id_produto)
print(p2.id_produto)


#Atributos Dinamicos -> É um atributo de instancia que pode ser criado em tempo de execução, sendo exclusivo da instancia que o criou

p2.peso =  '5Kg'

print(p2.peso)
