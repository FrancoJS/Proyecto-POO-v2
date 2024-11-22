from models.Person_model import Person

class User (Person):
    
    def __init__(self, rut:str, names:str, paternal_surname:str, maternal_surname:str, phone_number:int, email:str, password:str, perfil_id: int):
        super().__init__(rut, names, paternal_surname, maternal_surname, phone_number, email)
        
        self.password = password
        self.perfil_id = perfil_id
