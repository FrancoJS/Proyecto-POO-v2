from datetime import datetime
import re
from colorama import Fore
from rich.console import Console
from utils.messages_templates import show_confirmation

class SucursalData:
    
    def __init__(self) -> None:
            self.console = Console()
    
    def get_data(self):
        name = self.get_name(self.console)
        adress = self.__obtenerDireccion(self.console)
        constitution_date = self.__obtenerFechaConstitucion(self.console)
        return name, adress, constitution_date
    
    @staticmethod
    def get_name(console, error:bool = False) -> str:
        while True:
            if error:
                if not show_confirmation():
                    raise Exception("Cancelado por el usuario.")
                
            name = console.input("[bold cyan]Nombre Sucursal: ").strip()
            if not re.match("^[A-Za-z0-9áéíóúÁÉÍÓÚñÑ\s]+$", name):
                console.print("[bold red]El nombre de la sucursal solo debe contener caracteres alfanuméricos y espacios.")
                error = True
                continue
            elif len(name) < 3 or len(name) > 50:
                console.print("[bold red]El nombre de la sucursal debe tener entre 3 y 50 caracteres.")
                error = True
                continue
            return name

    @staticmethod
    def get_address(console, error:bool = False) -> str:
        while True:
            if error:
                if not show_confirmation():
                    raise Exception("Cancelado por el usuario.")
                
            address = console.input("[bold cyan]Dirección Sucursal: ").strip()
            if not re.match("^[A-Za-z0-9áéíóúÁÉÍÓÚñÑ\s#.,-]+$", address):
                console.print("[bold red]La dirección contiene caracteres no permitidos.")
                error = True
                continue
            elif len(address) < 5 or len(address) > 100:
                console.print("[bold red]La dirección debe tener entre 5 y 100 caracteres.")
                error = True
                continue
            return address
    
    @staticmethod
    def get_constitution_date(console, error:bool = False) -> str:
        while True:
            if error:
                if not show_confirmation():
                    raise Exception("Cancelado por el usuario.")
                
            consitution_date = console.input("[bold cyan]Fecha Constitución (YYYY-MM-DD): ").strip()
            try:
                date = datetime.strptime(consitution_date, "%Y-%m-%d")
                return date
            except ValueError:
                print(Fore.RED + "Debe ingresar una fecha válida en el formato (YYYY-MM-DD).")
                error = True

    
    def get_sucursal_id(self, sucursal_controller):
            console = self.console
            while True:
                try:
                    sucursal_id = int(console.input("[bold cyan]Ingrese ID de Sucursal: "))
                    if not sucursal_controller.get_sucursal_id(sucursal_id):
                        raise Exception
                    
                    return sucursal_id
                except ValueError:
                    console.print("[bold red]¡El ID debe ser un número entero!.")
                except:
                    console.print("[bold red]¡Sucursal no existe!, Ingrese un ID válido.")
                    if not show_confirmation():
                            raise Exception("Cancelado por el usuario.")
                    