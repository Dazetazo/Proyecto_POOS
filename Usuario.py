from Persona import Persona

class Usuario(Persona):
    __id = 0
    __contraseña = ""
    __idPerfil = 0
    __nomPerfil = ""
    __idEstado = 0
    
    def __init__(self):
        pass
    
    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id
    
    def getContraseña(self):
        return self.__contraseña
    
    def setContraseña(self, contr):
        self.__contraseña = contr

    def getIdPerfil(self):
        return self.__idPerfil
    
    def setIdPerfil(self, id):
        self.__idPerfil = id
    
    def getNomPerfil(self):
        return self.__nomPerfil
    
    def setNomPerfil(self, nomper):
        self.__nomPerfil = nomper
    
    def getIdEstado(self):
        return self.__idEstado
    
    def setIdEstado(self, idest):
        self.__idEstado = idest