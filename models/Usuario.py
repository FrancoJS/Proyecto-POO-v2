from models.Persona import Persona

class Usuario (Persona):
    
    def __init__(self, rut:str, nombres:str, ape_paterno:str, ape_materno:str, telefono:int, correo:str, clave:str, p_id: int):
        super().__init__(rut, nombres, ape_paterno, ape_materno, telefono, correo)
        
        self.clave = clave
        self.p_id = p_id