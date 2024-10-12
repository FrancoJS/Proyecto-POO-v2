from models.Persona import Persona
from datetime import date

class Empleado (Persona):
    
    def __init__(self, rut:str, nombres:str, ape_paterno:str, ape_materno:str, telefono:int, correo:str,
                experiencia:int, inicio_contrato:date, salario:int, s_id:int):
        super().__init__(rut, nombres, ape_paterno, ape_materno, telefono, correo)
        
        self.experiencia = experiencia
        self.inicio_contrato = inicio_contrato
        self.salario = salario
        self.s_id = s_id