from database.dao import DAO
from models.Sucursal import Sucursal
from colorama import Fore
from os import system

class SucursalController:
    def __init__(self):
        self.__dao = DAO()
    
    def crearSucursal(self,nombre:str, direccion:str, fecha_constitucion):
        try:
            sucursal = Sucursal(nombre, direccion, fecha_constitucion)
            sql = "INSERT INTO SUCURSALES (nombre, direccion, fecha_const) values (%s, %s, %s)"
            values = (sucursal.nombre, sucursal.direccion, sucursal.fecha_constitucion)
            self.__dao.cursor.execute(sql,values)
            self.__dao.connection.commit()
            id_sucursal = self.__dao.cursor.lastrowid
            return id_sucursal
        except:
            raise Exception("Ocurrio un error al crear la sucursal, intente nuevamente")
        finally:
            self.__dao.desconectar()
            
    def listarSucursales(self):
        try:
            sql = "SELECT * FROM SUCURSALES"
            self.__dao.cursor.execute(sql)
            response = self.__dao.cursor.fetchall()
            return response
        except:
            print("Ocurrió un error al buscar los datos")
        finally:
            self.__dao.desconectar()
    
    def buscarSucursalID(self, s_id:int):
        try:
            sql = "SELECT * FROM SUCURSALES WHERE s_id = %s"
            values = (s_id)
            self.__dao.cursor.execute(sql,values)
            sucursal = self.__dao.cursor.fetchone()
            return sucursal
        except:
            print("Error al buscar al encontrar la sucursal")
        
    

        