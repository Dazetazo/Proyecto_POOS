from Ejemplar import Ejemplar
from Usuario import Usuario
from Editorial import Editorial
from Tipo import Tipo
from DAO import DAO
from beautifultable import BeautifulTable
from os import system
import os

class Funciones:
    eje = Ejemplar()
    usu = Usuario()
    edi = Editorial()
    tip = Tipo()
    d = DAO()
    
    def __init__(self):
        pass
    
#------------------------------------------------------------------------------------------------------------
    
    def menuInicial(self):
        try:
            system("cls")
            print("--------------------")
            print("--- MENU INICIAL ---")
            print("--------------------")
            print("1.Iniciar Sesión Como Admin")
            print("2.Iniciar Sesión Como Editor")
            print("3.Salir")
            op = int(input("Digite Una Opcion : "))
            if op == 1:
                self.__menuAdmin()
            elif op == 2:
                self.__menuEditor()
            elif op == 3:
                self.__salir()
            else:
                self.errorOpcion()
        except:
            print("\n--- La Opción Debe Ser Numérica!! ---", end="\n\n")
            system("pause")
            self.menuInicial()
    
#------------------------------------------------------------------------------------------------------------

    def __menuAdmin(self):
        try:
            system("cls")
            print("------------------")
            print("--- MENU ADMIN ---")
            print("------------------")
            print("1.Gestionar Editoriales")
            print("2.Gestionar Tipos")
            print("3.Cerrar Sesión")
            op = int(input("Digite Una Opcion : "))
            if op == 1:
                self.__menuAdminEditoriales()
            elif op == 2:
                self.__menuAdminTipos()
            elif op == 3:
                self.__cerrarSesion()
            else:
                self.errorOpcion()
        except:
            print("\n--- La Opción Debe Ser Numérica!! ---", end="\n\n")
            system("pause")
            self.__menuAdmin()
            
#------------------------------------------------------------------------------------------------------------
       
    def __menuAdminEditoriales(self):
        try:
            system("cls")
            print("--------------------------------")
            print("--- MENU ADMIN (EDITORIALES) ---")
            print("--------------------------------")
            print("1.Crear Editoriales")
            print("2.Listar Editoriales")
            print("3.Buscar Editoriales")
            print("4.Modificar Editoriales")
            print("5.Eliminar Editoriales")
            print("6.Estadistica")
            print("7.Volver")
            op = int(input("Digite Una Opcion : "))
            if op == 1:
                self.__crearEditoriales()
            elif op == 2:
                self.__listarEditoriales()
            elif op == 3:
                self.__buscarEditoriales()
            elif op == 4:
                self.__modificarEditoriales()
            elif op == 5:
                self.__eliminarEditoriales()
            elif op == 6:
                self.__estadisticaEditoriales()
            elif op == 7:
                self.__menuAdmin()
            else:
                print("\n--- Error de Opcion!! ---", end="\n\n")
                system("pause")
                self.__menuAdminEditoriales()
        except:
            print("\n--- La Opción Debe Ser Numérica!! ---", end="\n\n")
            system("pause")
            self.__menuAdminEditoriales()

#------------------------------------------------------------------------------------------------------------

    def __crearEditoriales(self):
        while True:
            try:
                system("cls")
                print("--------------------------------------")
                print("--- MENU ADMIN (CREAR EDITORIALES) ---")
                print("--------------------------------------")
                nom = input("Digite El Nombre De Nueva Editorial a Crear : ")
                if len(nom.strip())<1 or len(nom.strip())>50:
                    print("\n--- Debe Tener Entre 1 y 50 Caracteres!! ---", end="\n\n")
                    system("pause")
                else:
                    nom = nom.strip()
                    r = self.d.comprobarNomEditorial(nom)
                    if r is not None:
                        print(f"\n--- Error. La Editorial ({ nom }) Ya Existe!! ---", end="\n\n")
                        system("pause")
                    else:
                        break
            except:
                print("\n--- Error Al Capturar El Nombre De Editorial A Crear!! ---", end="\n\n")
                system("pause")
        
        self.edi.setNombre(nom.upper())
        self.edi.setIdEstado(1)
        self.d.agregarEditorial(self.edi)
        
        system("cls")
        print(f"--- Nueva Editorial { nom } Creada Correctamente!!---", end="\n\n")
        system("pause")
        self.__menuAdminEditoriales()
        
#------------------------------------------------------------------------------------------------------------


    def __listarEditoriales(self):
        respuesta = self.d.obtenerEditoriales()
        if len(respuesta) == 0:
            system("cls")
            print("--- No Hay Registros De EDITORIALES Para Listar!! ---", end="\n\n")
            system("pause")
            self.__menuAdminEditoriales()
        else:
            system("cls")
            print("---------------------------------------")
            print("--- MENU ADMIN (LISTAR EDITORIALES) ---")
            print("---------------------------------------")
            tabla = BeautifulTable()
            tabla.columns.header = [ "ID", "NOMBRE", "ESTADO"]
            for x in respuesta:
                tabla.rows.append( [ x[0], x[1], x[2] ] )
            
            print(tabla, end="\n\n")
            system("pause")
            self.__menuAdminEditoriales()

#------------------------------------------------------------------------------------------------------------
  
    def __buscarEditoriales(self):
            try:
                system("cls")
                print("-----------------------")
                print("--- EN CONSTRUCCION ---")
                print("-----------------------")
                self.__menuAdminEditoriales()
            except:
                print("\n--- Error Al Buscar Editorial!! ---", end="\n\n")
                system("pause")
                self.__menuAdminEditoriales()

#------------------------------------------------------------------------------------------------------------

    def __modificarEditoriales(self):
        try:
            system("cls")
            print("-----------------------")
            print("--- EN CONSTRUCCION ---")
            print("-----------------------")
            self.__menuAdminEditoriales()
        except:
            print("\n--- Error Al Modificar Editorial!! ---", end="\n\n")
            system("pause")
            self.__menuAdminEditoriales()
#------------------------------------------------------------------------------------------------------------
        def __eliminarEditoriales(self):
            try:
                system("cls")
                print("-----------------------")
                print("--- EN CONSTRUCCION ---")
                print("-----------------------")
                self.__menuAdminEditoriales()
            except:
                print("\n--- Error Al Eliminar Editorial!! ---", end="\n\n")
                system("pause")
                self.__menuAdminEditoriales()

#------------------------------------------------------------------------------------------------------------
    def __estadisticaEditoriales(self):
        try:
            respuesta = self.d.obtenerEditoriales()
            if len(respuesta) == 0:
                system("cls")
                print("--- No hay registros de Editoriales ---")
                system("pause")
                self.__menuAdminEditoriales()
            else:
                system("cls")
                print("--------------------------------------------")
                print("--- MENU ADMIN (ESTADISTICA EDITORIALES) ---")
                print("--------------------------------------------")
                print(f"Cantidad Editoriales : {self.d.obtenerEstadisticaEditoriales(1)}")
                print(f"Cantidad Editoriales Habilitadas : {self.d.obtenerEstadisticaEditoriales(2)}")
                print(f"Cantidad de Editoriales Deshabilitadas : {self.d.obtenerEstadisticaEditoriales(3)}")
        except:
            print("\n--- Error Al Obtener Estadistica de Editoriales!! ---", end="\n\n")
            print("pause")
            self.__menuAdminEditoriales()
        



#------------------------------------------------------------------------------------------------------------

    def __salir(self):
        system("cls")
        os._exit(1)
#------------------------------------------------------------------------------------------------------------
    def __cerrarSesion(self):
        system("cls")
        os._exit(1)
    