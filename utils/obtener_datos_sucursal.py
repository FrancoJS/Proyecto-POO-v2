from datetime import datetime
import re
from colorama import Fore
from rich.console import Console
from utils.mensajes_templates import reintentar

class DatosSucursal:
    
    def __init__(self) -> None:
            self.console = Console()
    
    def obtenerDatosSucursal(self):
        nombre = self.__obtenerNombreSucursal()
        direccion = self.__obtenerDireccion()
        fecha_constitucion = self.__obtenerFechaConstitucion()
        return nombre, direccion, fecha_constitucion
    
    
    def __obtenerNombreSucursal(self, error:bool = False) -> str:
        console = self.console
        while True:
            if error:
                if not reintentar():
                    raise Exception
                
            nombre = console.input("[bold cyan]Nombre Sucursal: ").strip()
            if not re.match("^[A-Za-z0-9áéíóúÁÉÍÓÚñÑ\s]+$", nombre):
                print(Fore.RED + "El nombre de la sucursal solo debe contener caracteres alfanuméricos y espacios.")
                error = True
                continue
            elif len(nombre) < 3 or len(nombre) > 50:
                print(Fore.RED + "El nombre de la sucursal debe tener entre 3 y 50 caracteres.")
                error = True
                continue
            return nombre


    def __obtenerDireccion(self, error:bool = False) -> str:
        console = self.console
        while True:
            if error:
                if not reintentar():
                    raise Exception
                
            direccion = console.input("[bold cyan]Dirección Sucursal: ").strip()
            if not re.match("^[A-Za-z0-9áéíóúÁÉÍÓÚñÑ\s#.,-]+$", direccion):
                print(Fore.RED + "La dirección contiene caracteres no permitidos.")
                error = True
                continue
            elif len(direccion) < 5 or len(direccion) > 100:
                print(Fore.RED + "La dirección debe tener entre 5 y 100 caracteres.")
                error = True
                continue
            return direccion
    
    
    def __obtenerFechaConstitucion(self, error:bool = False) -> str:
        console = self.console
        while True:
            if error:
                if not reintentar():
                    raise Exception
                
            fecha_constitucion = console.input("[bold cyan]Fecha Constitución (YYYY-MM-DD): ").strip()
            try:
                fecha = datetime.strptime(fecha_constitucion, "%Y-%m-%d")
                return fecha
            except ValueError:
                print(Fore.RED + "Debe ingresar una fecha válida en el formato (YYYY-MM-DD).")
                error = True


    def get_sucursal_id(self, sucursal_cotroller):
            console = self.console
            while True:
                try:
                    sucursal_id = int(console.input("[bold cyan]Ingrese ID de Sucursal: "))
                    if sucursal_cotroller.buscarSucursalID(sucursal_id):
                        return sucursal_id
                    else:
                        console.print("[bold red]¡Sucursal no existe!, [bold white]Ingrese un ID válido.")
                        if not reintentar():
                            raise Exception
                except ValueError:
                    print(Fore.RED + "¡ID de Sucursal inválido!")
                except:
                    raise Exception