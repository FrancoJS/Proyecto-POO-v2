from datetime import date

class Sucursal:
    
    def __init__(self, name:str, adress:str, constitution_date:date):
        self.name = name
        self.adress = adress
        self.constitution_date = constitution_date
