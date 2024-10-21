from Usuario import Usuario
from Editorial import Editorial
from Tipo import Tipo

class Ejemplar:
    __id = 0
    __isbn = ""
    __titulo = ""
    tipo = Tipo()
    editorial = Editorial()
    usuario = Usuario()
    __idEstado = 0
    __nomEstado = ""
    
    def __init__(self):
        pass
    
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
    
    def getIsbn(self):
        return self.__isbn
    
    def setIsbn(self, isbn):
        self.__isbn = isbn
    
    def getTitulo(self):
        return self.__titulo
    
    def setTitulo(self, tit):
        self.__titulo = tit
    
    def getIdEstado(self):
        return self.__idEstado
    
    def setIdEstado(self, idest):
        self.__idEstado = idest
    
    def getNomEstado(self):
        return self.__nomEstado
    
    def setNomEstado(self, nomest):
        self.__nomEstado = nomest