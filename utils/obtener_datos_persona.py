from datetime import datetime
import re
from colorama import Fore
from os import system
from rich.console import Console
from utils.mensajes_templates import reintentar

class DatosPersona:
    
    def __init__(self) -> None:
            self.console = Console()
    
    
    def obtenerDatosPersona(self):
        try:
            rut = self.obtenerRut()
            nombres = self.__obtenerNombre()
            apellido_p = self.__obtenerApellido("Paterno")
            apellido_m = self.__obtenerApellido("Materno")
            telefono = self.__obtenerTelefono()
            correo = self.__obtenerCorreo()
            return rut, nombres, apellido_p, apellido_m, telefono, correo
        except:
            raise Exception
        
        
    def obtenerRut(self, error:bool = False) -> str:
        console = self.console
        while True:
            if error:
                if not reintentar():
                    raise Exception
                
            console.print("[bold white]Si el digito verificador de su rut es [bold yellow]'K'[/bold yellow] reemplacelo con 0")
            rut = console.input("[bold cyan]Rut: ").strip()
                        
            #Cambiar al momento de la presentacion el 2 a 8 para ruts validos
            if len(rut) < 8 or len(rut) > 12:
                print(Fore.RED + "La longitud del RUT no es válida.")
                error = True
                continue
                
            rut = rut.replace(".","").replace("-","")
            if len(rut) > 9:
                print(Fore.RED + "La longitud del RUT no es válida.")
                error = True
                continue
                
            numero, dv = rut[:-1], rut[-1]
            if not numero.isdigit() or not dv.isdigit():
                print(Fore.RED + "El RUT y dígito verificador deben ser números.")
                error = True
                continue
                
            rut_validado = f"{numero}-{dv}"
            return rut_validado
                  
                
    def __obtenerNombre(self, error:bool = False) -> str:
        console = self.console
        while True:
            if error:
                if not reintentar():
                    raise Exception
                
            nombres = console.input("[bold cyan]Nombres: ").strip()
            if not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", nombres):
                print(Fore.RED + "Los nombres solo deben contener caracteres válidos.")
                error = True
                continue
            
            elif len(nombres) < 1 or len(nombres) > 50:
                print(Fore.RED + "El nombre debe tener entre 1 y 50 caracteres.")
                error = True
                continue
                
            return nombres
        
        
    def __obtenerApellido(self, tipo:str, error:bool = False) -> str:
        console = self.console
        while True:
            if error:
                if not reintentar():
                    raise Exception
                
            apellido = console.input(f"[bold cyan]Apellido {tipo}: ").strip()
            if not apellido.isalpha():
                print(Fore.RED + "El apellido no debe contener caracteres especiales ni espacios.")
                error = True
                continue
            
            elif len(apellido) < 1 or len(apellido) > 30:
                print(Fore.RED + "El apellido debe tener entre 1 y 30 caracteres.")
                error = True
                continue
            
            return apellido
        
        
    def __obtenerTelefono(self, error:bool = False) -> int:
        console = self.console
        while True:
            if error:
                if not reintentar():
                    raise Exception
                
            telefono = console.input("[bold cyan]Telefono: +56")
            
            if not telefono.isdigit():
                print(Fore.RED + "El teléfono debe contener solo números.")
                error = True
                continue
            
            if len(telefono) != 9:
                print(Fore.RED + "El télefono debe tener 9 números.")
                error = True
                continue
            
            return int(telefono)
        
        
    def __obtenerCorreo(self, error:bool = False) -> str:
        console = self.console
        while True:
            if error:
                if not reintentar():
                    raise Exception
                
            correo = console.input("[bold cyan]Correo: ")
            
            if len(correo) < 1 or len(correo) > 50:
                print(Fore.RED + "El correo debe tener entre 1 y 50 caracteres.")
                error = True
                continue
            
            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$", correo):
                print(Fore.RED + "Debe ingresar un correo válido, ej: ejemplo@dominio.com.")
                error = True
                continue
            
            return correo

    