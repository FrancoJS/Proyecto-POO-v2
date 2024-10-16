from datetime import datetime
import re
from colorama import Fore

class DatosSucursal:
    
    def obtenerDatosSucursal(self):
        nombre = self.__obtenerNombreSucursal()
        direccion = self.__obtenerDireccion()
        fecha_constitucion = self.__obtenerFechaConstitucion()
        return nombre, direccion, fecha_constitucion
    
    @staticmethod
    def __obtenerNombreSucursal() -> str:
        while True:
            nombre = input("NOMBRE SUCURSAL: ").strip()
            if not re.match("^[A-Za-z0-9áéíóúÁÉÍÓÚñÑ\s]+$", nombre):
                print(Fore.RED + "El nombre de la sucursal solo debe contener caracteres alfanuméricos y espacios.")
                continue
            elif len(nombre) < 3 or len(nombre) > 50:
                print(Fore.RED + "El nombre de la sucursal debe tener entre 3 y 50 caracteres.")
                continue
            return nombre

    @staticmethod
    def __obtenerDireccion() -> str:
        while True:
            direccion = input("DIRECCION SUCURSAL: ").strip()
            if not re.match("^[A-Za-z0-9áéíóúÁÉÍÓÚñÑ\s#.,-]+$", direccion):
                print(Fore.RED + "La dirección contiene caracteres no permitidos.")
                continue
            elif len(direccion) < 5 or len(direccion) > 100:
                print(Fore.RED + "La dirección debe tener entre 5 y 100 caracteres.")
                continue
            return direccion
    
    @staticmethod
    def __obtenerFechaConstitucion() -> str:
        while True:
            fecha_constitucion = input("FECHA CONSTITUCION (YYYY-MM-DD): ").strip()
            try:
                fecha = datetime.strptime(fecha_constitucion, "%Y-%m-%d")
                return fecha
            except ValueError:
                print(Fore.RED + "Debe ingresar una fecha válida en el formato YYYY-MM-DD.")
