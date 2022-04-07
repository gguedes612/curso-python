class Televisao:
    def __init__(self,canal_atual,volume_atual):
        self.__canal_atual = canal_atual
        self.__volume_atual = volume_atual

    def diminuir_volume(self):
        if self.__volume_atual == 0:
            print('TV já esta no mudo')
        else:
            self.__volume_atual -= 1

    def aumentar_volume(self):
        if self.__volume_atual == 10:
            print('TV já esta no mudo')
        else:
            self.__volume_atual += 1

    def passar_canal(self):
        if self.__canal_atual == 100:
            self.__canal_atual = 1
        else:
            self.__canal_atual += 1
    
    def voltar_canal(self):
        if self.__canal_atual == 0:
            self.__canal_atual = 100
        else:
            self.__canal_atual -= 1
    
    def mudar_canal(self,canal):
        if canal <= 0 or canal > 100:
            print('Canal inserido invalido')
        else:
            self.__canal_atual = canal

    def volume(self):
        print(self.__volume_atual)

    def canal(self):
        print(self.__canal_atual)

class ControleRemoto:

    def __init__(self,televisao):
        self.__televisao = televisao

    def aumentar_volume(self):
        self.__televisao.aumentar_volume()
    
    def diminuir_volume(self):
        self.__televisao.diminuir_volume()

    def passar_canal(self):
        self.__televisao.passar_canal()

    def voltar_canal(self):
        self.__televisao.voltar_canal()
    
    def mudar_canal(self,canal):
        self.__televisao.mudar_canal(canal)