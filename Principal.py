from Funciones import Funciones

class Principal:
    __f = Funciones()

    def __init__(self):
        pass

    def ejecutarPrograma(self):
        self.__f.menuInicial()
#-------------------------------
p = Principal()
p.ejecutarPrograma()