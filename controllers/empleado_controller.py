from models.Empleado import Empleado
from database.dao import DAO
from datetime import date
from colorama import Fore, Style, init
init(autoreset=True)

class Empleado_Controller:
    def __init__(self):
        self.__dao = DAO()

    def crearEmpleado(self, rut:str, nombres:str, ape_paterno:str, ape_materno:str, telefono:int, correo:str, experiencia:int, inicio_contrato:date, salario:int, s_id:int):
        try:
            empleado = Empleado(rut, nombres, ape_paterno, ape_materno, telefono, correo, experiencia, inicio_contrato, salario, s_id)
            sql = "INSERT INTO EMPLEADOS (RUT, NOMBRES, APE_PATERNO, APE_MATERNO, TELEFONO, CORREO, EXPERIENCIA, INICIO_CON, SALARIO, S_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (empleado.rut, empleado.nombres, empleado.ape_paterno, empleado.ape_materno, empleado.telefono, empleado.correo, empleado.experiencia, empleado.inicio_contrato, empleado.salario, empleado.s_id)
            self.__dao.cursor.execute(sql, values)
            self.__dao.connection.commit()
        except:  
            raise Exception(Fore.RED + "¡Ocurrió un error al ingresar al empleado en la base de datos!")
        finally:
            self.__dao.cursor.close()

    def listarEmpleados(self):
        try:
            sql = "SELECT * FROM EMPLEADOS"
            self.__dao.cursor.execute(sql)
            result = self.__dao.cursor.fetchall()
            return result
        except Exception as e:  
            print(f"Ocurrió un error al buscar los datos: {e}")   
        finally:
            self.__dao.desconectar()