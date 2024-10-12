from database.dao import DAO
from models.Sucursal import Sucursal
from datetime import date

class SucursalController:
    def __init__(self):
        self.__dao = DAO()
    
    def crearSucursal(self,nombre:str, direccion:str, fecha_constitucion:date):
        try:
            sucursal = Sucursal(nombre, direccion, fecha_constitucion)
            sql = "INSERT INTO SUCURSALES (nombre, direccion, fecha_constitucion) values (%s, %s, %s)"
            values = (sucursal.nombre, sucursal.direccion, sucursal.fecha_constitucion)
            self.__dao.cursor.execute(sql,values)
            self.__dao.connection.commit()
            id_sucursal = self.__dao.cursor.lastrowid
            return id_sucursal
        except:
            raise Exception("Ocurrio un error al crear la sucursal, intente nuevamente")
        finally:
            self.__dao.desconectar()
            
        