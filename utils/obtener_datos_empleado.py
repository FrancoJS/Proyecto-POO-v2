from datetime import datetime
import re
from colorama import Fore
from rich.console import Console
from utils.mensajes import reintentar


class DatosEmpleado: 
    
    def __init__(self) -> None:
        self.console = Console()
    
    def obtenerDatosEmpleado(self):
        experiencia = self.__obtenerExperiencia()
        inicio_contrato = self.__obtenerFechaContrato()
        salario = self.__obtenerSalario()
        return experiencia, inicio_contrato, salario
    
    
    def __obtenerExperiencia(self, error:bool = False) -> int:
        console = self.console
        while True:
            if error:
                if not reintentar():
                    raise Exception
                
            try:
                experiencia = int(console.input("[bold cyan]Experiencia (en años): "))
                if experiencia < 0 or experiencia > 50:
                    print(Fore.RED + "La experiencia debe ser un valor entre 0 y 50 años.")
                    error = True
                    continue
                return experiencia
            except ValueError:
                print(Fore.RED + "Debe ingresar un número válido para la experiencia.")
                error = True
    
    
    def __obtenerFechaContrato(self, error:bool = False) -> str:
        console = self.console
        while True:
            if error:
                if not reintentar():
                    raise Exception
                
            fecha_contrato = console.input("[bold cyan]Fecha inicio contrato (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(fecha_contrato, "%Y-%m-%d")
                return fecha_contrato
            except ValueError:
                print(Fore.RED + "Debe ingresar una fecha válida en el formato YYYY-MM-DD.")
                error = True
    
    
    def __obtenerSalario(self, error:bool = False) -> int:
        console = self.console
        while True:
            if error:
                if not reintentar():
                    raise Exception
                
            try:
                salario = int(console.input("[bold cyan]Salario (clp): $"))
                if salario < 0:
                    print(Fore.RED + "Debe ingresar un salario valido")
                    error = True
                    continue
                return salario
            except ValueError:
                print(Fore.RED + "Debe ingresar un número válido para el salario.")
                error = True
