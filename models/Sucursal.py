from datetime import date

class Sucursal:
    
    def __init__(self, nombre:str, direccion:str, fecha_constitucion:date):
        self.nombre = nombre
        self.direccion = direccion
        self.fecha_constitucion = fecha_constitucion