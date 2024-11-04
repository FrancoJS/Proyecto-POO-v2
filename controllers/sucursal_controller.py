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
            sql = "SELECT * FROM SUCURSALES where es_id = 1"
            self.__dao.cursor.execute(sql)
            response = self.__dao.cursor.fetchall()
            return response
        except:
            print("Ocurrió un error al buscar los datos")
        finally:
            self.__dao.desconectar()
    
    def buscarSucursalID(self, s_id:int):
        try:
            sql = "SELECT S_ID FROM SUCURSALES WHERE s_id = %s and es_id = 1"
            values = (s_id)
            self.__dao.cursor.execute(sql,values)
            sucursal = self.__dao.cursor.fetchone()
            return sucursal
        except:
            print("Error al buscar al encontrar la sucursal")
            
    def eliminarSucursal(self, s_id:int):
        try:
            sucursal = self.buscarSucursalID(s_id)
            if not sucursal:
                print(Fore.RED + "No hay Sucursales!")
            
            sql = "UPDATE SUCURSALES SET ES_ID = 2 WHERE S_ID = %s"
            self.__dao.cursor.execute(sql, (s_id))
            self.__dao.connection.commit()
        except Exception as e:
            raise Exception(e)
        
    
    

        