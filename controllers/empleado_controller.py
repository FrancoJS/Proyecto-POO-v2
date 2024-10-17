from models.Empleado import Empleado
from database.dao import DAO
from datetime import date
from colorama import Fore, Style, init
from .sucursal_controller import SucursalController
init(autoreset=True)

class Empleado_Controller:
    def __init__(self):
        self.__dao = DAO()

    def crearEmpleado(self, rut:str, nombres:str, ape_paterno:str, ape_materno:str, telefono:int, correo:str, experiencia:int, inicio_contrato:date, salario:int, s_id:int):
        try:
            empleadoEnDB = self.buscarEmpleado(rut, telefono, correo)
            if empleadoEnDB:
                raise Exception(Fore.RED + "¡Empleado ya esta registrado!")
            
            if not SucursalController().buscarSucursalID(s_id):
                raise Exception(Fore.RED + "¡Sucursal no existe!")
            
            empleado = Empleado(rut, nombres, ape_paterno, ape_materno, telefono, correo, experiencia, inicio_contrato, salario, s_id)
            sql = "INSERT INTO EMPLEADOS (RUT, NOMBRES, APE_PATERNO, APE_MATERNO, TELEFONO, CORREO, EXPERIENCIA, INICIO_CON, SALARIO, S_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (empleado.rut, empleado.nombres, empleado.ape_paterno, empleado.ape_materno, empleado.telefono, empleado.correo, empleado.experiencia, empleado.inicio_contrato, empleado.salario, empleado.s_id)
            self.__dao.cursor.execute(sql, values)
            self.__dao.connection.commit()
        except Exception as e:
            raise Exception(e)
        finally:
            self.__dao.cursor.close()

    def listarEmpleados(self):
        try:
            sql = "SELECT * FROM EMPLEADOS"
            self.__dao.cursor.execute(sql)
            result = self.__dao.cursor.fetchall()
            return result
        except:  
            print(f"Ocurrió un error al buscar los datos")   
        finally:
            self.__dao.desconectar()
            
    def buscarEmpleado(self, rut, telefono, correo):
        try:
            sql = "SELECT * FROM EMPLEADOS WHERE rut = %s or telefono = %s or correo = %s"
            value = (rut, telefono, correo)
            self.__dao.cursor.execute(sql, value)
            empleado = self.__dao.cursor.fetchone()
            return empleado
        except:
            print("Error al buscar al encontrar al empleado")