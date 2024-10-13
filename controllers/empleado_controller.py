from models.Empleado import Empleado
from database.dao import DAO
from datetime import date

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
        except Exception as e:  
            print(f"Ocurrió un error al ingresar los datos: {e}")  # 
            raise Exception("Ocurrió un error al ingresar los datos.")
        finally:
            self.__dao.cursor.close()
