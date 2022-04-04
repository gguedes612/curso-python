"""
POO - Classes

Em POO, Classes nada mais são que modelos dos objetos do mundo real sendo representados computacionalmentes.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
    - Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos conseguimos representar computacionalmente os estados de um objeto. No caso da lampada, possivelmente iriamos querer saber se a lampada é 110 ou 220 volts, se ela é branca, amarela, vermelha ou outra cor, qual éa  luminosidade dela e etc.

    - Metodos(funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode realizar no seu sistema. No caso da lampada, por exemplo, um compotamento comum que muito provavelmente iriamos querer representar no nosso sistema é o de ligar e desligar a mesma. 
"""

class Lampada:
    pass

lamp = Lampada()

print(type(lamp))
