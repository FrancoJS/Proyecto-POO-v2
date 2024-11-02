from database.dao import DAO
from colorama import Fore
from .empleado_controller import EmpleadoController

class AsignacionesController:
    
    def __init__(self):
        self.__dao = DAO()
        
    def listarAsignaciones(self):
        try:
            sql = "SELECT E_ID, RUT, NOMBRES, CONCAT(APE_PATERNO, ' ', APE_MATERNO), S.S_ID, NOMBRE, DIRECCION FROM EMPLEADOS E JOIN SUCURSALES S ON E.S_ID = S.S_ID WHERE E.ES_ID = 1 AND S.ES_ID = 1"
            self.__dao.cursor.execute(sql)
            response = self.__dao.cursor.fetchall()
            print(response)
            return response
        except:
            print(Fore.RED + "Ocurrio un error al buscar los datos")
        finally:
            self.__dao.desconectar()
            
    def reasignarEmpleado(self, rut:str, s_id:int):
        try:
            empleado = EmpleadoController().buscarEmpleadoPorRut(rut)
            if not empleado:
                raise Exception(Fore.RED + "¡El Rut del empleado no existe!, Ingreselo nuevamente")
            
            if empleado[1] == s_id:
                raise Exception(Fore.RED + "¡El empleado ya esta asignado a esta sucursal!, Ingreselo nuevamente")
            
            sql = "UPDATE EMPLEADOS SET S_ID = %s WHERE rut = %s"
            values = (s_id, rut)
            self.__dao.cursor.execute(sql, values)
            self.__dao.connection.commit()
        except Exception as e:
            raise Exception(e)
        finally:
            self.__dao.desconectar()