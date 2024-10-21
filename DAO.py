from Ejemplar import Ejemplar
from Usuario import Usuario
from Editorial import Editorial
from Tipo import Tipo
from os import system
import pymysql

class DAO:

    def __init__(self):
        pass
#---------------------------------------
    def conectar(self):
        self.con = pymysql.connect(
            host = "localhost",
            user = "root",
            password= "",
            db = "BD_gestion"
        )
        self.cursor = self.con.cursor()
#---------------------------------------

    def desconectar(self):
        self.con.close()

#---------------------------------------

    def comprobarNomEditorial(self, nom):
        try:
            sql = "select nom_edi from editoriales where nom_edi=%s"
            self.conectar()
            self.cursor.execute(sql, nom)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar Nombre De Editorial!! (DAO) ---", end="\n\n")
            system("pause")
#--------------------------------------------------------------------------------

    def agregarEditorial(self, edi):
        try:            
            sql = "insert into editoriales (nom_edi, id_est) values (%s, %s)"
            val = (edi.getNombre(), edi.getIdEstado())
            self.conectar()
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Agregar Editorial (DAO)!! ---", end="\n\n")
            system("pause")

#--------------------------------------------------------------------------------

    def obtenerEditoriales(self):
        try:
            sql = "select id_edi, nom_edi, nom_est from editoriales e inner join estados est on e.id_est=est.id_est order by nom_edi asc"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Obtener Editoriales (DAO)!! ---", end="\n\n")
            system("pause")
#--------------------------------------------------------------------------------
    def obtenerEstadisticaEditoriales(self, opcion):
        try:
            sql = ""
            if opcion == 1:
                sql = "select count(*) from editoriales"
            elif opcion == 2:
                sql = "select count(*) from editoriales where id_est=1"
            elif opcion == 3:
                sql = "select count(*) from editoriales where id_est=2"
            
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs[0]
        except:
            print("\n--- Error Al Obtener Estadistica de Editoriales!! (DAO) ---", end="\n\n")
            system("pause")

#------------------------------------------------------------------------------------------------------------

    def comprobarNomTipo(self, nom):
        try:
            sql = "select nom_tip from tipos where nom_tip=%s"
            self.conectar()
            self.cursor.execute(sql, nom)
            rs = self.cursor.fetchone()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Comprobar Nombre De Tipo!! (DAO) ---", end="\n\n")
            system("pause")
#------------------------------------------------------------------------------------------------------------

    def agregarTipo(self, tip):
        try:            
            sql = "insert into tipos (nom_tip, id_est) values (%s, %s)"
            val = (tip.getNombre(), tip.getIdEstado())
            self.conectar()
            self.cursor.execute(sql, val)
            self.con.commit()
            self.desconectar()
        except:
            print("\n--- Error Al Agregar Tipo (DAO)!! ---", end="\n\n")
            system("pause")

#------------------------------------------------------------------------------------------------------------

    def obtenerTipos(self):
        try:
            sql = "select id_tip, nom_tip, nom_est from tipos t inner join estados est on t.id_est=est.id_est order by nom_tip asc"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Obtener Tipos (DAO)!! ---", end="\n\n")
            system("pause")

#------------------------------------------------------------------------------------------------------------

    def obtenerTipos(self):
        try:
            sql = "select id_tip, nom_tip, nom_est from tipos t inner join estados est on t.id_est=est.id_est order by nom_tip asc"
            self.conectar()
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            self.desconectar()
            return rs
        except:
            print("\n--- Error Al Obtener Tipos (DAO)!! ---", end="\n\n")
            system("pause")