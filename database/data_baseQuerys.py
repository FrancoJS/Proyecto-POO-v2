from database.dao import DAO
from controllers.empleado_controller import Empleado_Controller
class Data_Querys:
    def __init__(self):
        self.__dao = DAO()
    
    def sql_select(self):
        try:
            query = "SELECT * FROM EMPLEADOS"
            result = self.__dao.cursor.execute(query)
            result = self.__dao.cursor.fetchall()
            return result
        except Exception as e:  
            print(f"Ocurrió un error al buscar los datos: {e}")   
        finally:
            self.__dao.desconectar()