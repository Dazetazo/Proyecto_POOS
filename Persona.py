class Persona:
    __rut = ""
    __nombre = ""
    __apellido = ""
    __edad = 0
    
    def __init__(self):
        pass
    
    def getRut(self):
        return self.__rut
    
    def setRut(self, rut):
        self.__rut = rut
    
    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nom):
        self.__nombre = nom
    
    def getApellido(self):
        return self.__apellido
    
    def setApellido(self, ape):
        self.__apellido = ape
        
    def getEdad(self):
        return self.__edad
    
    def setEdad(self, eda):
        self.__edad = eda