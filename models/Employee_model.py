from models.Person_model import Person
from datetime import date

class Employee (Person):
    
    def __init__(self, rut:str, names:str, paternal_surname:str, maternal_surname:str, phone_number:int, email:str,
                experience:int, hire_date:date, salary:int, sucursal_id:int):
        super().__init__(rut, names, paternal_surname, maternal_surname, phone_number, email)
        
        self.experience = experience
        self.hire_date = hire_date
        self.salary = salary
        self.sucursal_id = sucursal_id