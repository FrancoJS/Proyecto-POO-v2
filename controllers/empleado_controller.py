from models.Empleado import Empleado
from database.dao import DAO
from datetime import date

class Empleado_Controller:
    
    def __init__(self):
        self.__dao = DAO()
       
    
    def crearEmpleado(self, rut:str, nombres:str, ape_paterno:str, ape_materno:str, telefono:int, correo:str, experiencia:int, inicio_contrato:date ,salario:int ):
        
        pass
        