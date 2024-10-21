class Editorial:
    
    __id = 0
    __nombre = ""
    __idEstado = 0
    __nomEstado = ""

    def __init__(self):
        pass

    def getId(self):
        return self.__id
    
    def setId(self, id):
        self.__id = id

    def getNombre(self):
        return self.__nombre
    
    def setNombre(self, nom):
        self.__nombre = nom
    
    def getIdEstado(self):
        return self.__idEstado
    
    def setIdEstado(self, idest):
        self.__idEstado = idest
    
    def getNomEstado(self):
        return self.__nomEstado
    
    def setNomEstado(self, nomest):
        self.__nomEstado = nomest