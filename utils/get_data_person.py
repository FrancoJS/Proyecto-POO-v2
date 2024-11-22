import re
from rich.console import Console
from utils.messages_templates import show_confirmation

class PersonData:
    
    def __init__(self) -> None:
            self.console = Console()
    
    
    def get_data(self):
        try:
            rut = self.get_rut(self.console)
            names = self.get_names(self.console)
            paternal_surname = self.get_surnames(self.console,"Paterno")
            maternal_surname = self.get_surnames(self.console,"Materno")
            phone_number = self.get_phone_number(self.console)
            email = self.get_email(self.console)
            return rut, names, paternal_surname, maternal_surname, phone_number, email
        except:
            raise Exception("Ocurrio un error al obtener los datos de la persona.")
        
    @staticmethod
    def get_rut(console, error:bool = False) -> str:        
        while True:
            if error:
                if not show_confirmation():
                    raise Exception("Cancelado por el usuario.")
                
            console.print("[bold white]Si el digito verificador de su rut es [bold yellow]'K'[/bold yellow] reemplacelo con 0")
            rut = console.input("[bold cyan]Rut: ").strip()
                        
            #Cambiar al momento de la presentacion el 2 a 8 para ruts validos
            if len(rut) < 8 or len(rut) > 12:
                console.print("[bold red]La longitud del RUT no es válida.")
                error = True
                continue
                
            rut = rut.replace(".","").replace("-","")
            if len(rut) > 9:
                console.print("[bold red]La longitud del RUT no es válida.")
                error = True
                continue
                
            number, dv = rut[:-1], rut[-1]
            if not number.isdigit() or not dv.isdigit():
                console.print("[bold red]El RUT y dígito verificador deben ser números.")
                error = True
                continue
                
            validated_rut = f"{number}-{dv}"
            return validated_rut
                  
    @staticmethod    
    def get_names(console, error:bool = False) -> str:
        while True:
            if error:
                if not show_confirmation():
                    raise Exception("Cancelado por el usuario.")	
                
            names = console.input("[bold cyan]Nombres: ").strip()
            if not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", names):
                console.print("[bold red]Los nombres solo deben contener caracteres válidos.")
                error = True
                continue
            
            elif len(names) < 1 or len(names) > 50:
                console.print("[bold red]El nombre debe tener entre 1 y 50 caracteres.")
                error = True
                continue
                
            return names
        
    @staticmethod
    def get_surnames(console, type:str, error:bool = False) -> str:
        while True:
            if error:
                if not show_confirmation():
                    raise Exception("Cancelado por el usuario.")
                
            surname = console.input(f"[bold cyan]Apellido {type}: ").strip()
            if not surname.isalpha():
                console.print("[bold red]El apellido no debe contener caracteres especiales ni espacios.")
                error = True
                continue
            
            elif len(surname) < 1 or len(surname) > 30:
                console.print("[bold red]El apellido debe tener entre 1 y 30 caracteres.")
                error = True
                continue
            
            return surname
        
    @staticmethod
    def get_phone_number(console, error:bool = False) -> int:
        while True:
            if error:
                if not show_confirmation():
                    raise Exception("Cancelado por el usuario.")
                
            phone_number = console.input("[bold cyan]Telefono: +56")
            
            if not phone_number.isdigit():
                console.print("[bold red]El teléfono debe contener solo números.")
                error = True
                continue
            
            if len(phone_number) != 9:
                console.print("[bold red]El télefono debe tener 9 números.")
                error = True
                continue
            
            return int(phone_number)
        
    @staticmethod
    def get_email(console, error:bool = False) -> str:
        while True:
            if error:
                if not show_confirmation():
                    raise Exception("Cancelado por el usuario.")
                
            email = console.input("[bold cyan]Correo: ")
            
            if len(email) < 1 or len(email) > 50:
                console.print("[bold red]El correo debe tener entre 1 y 50 caracteres.")
                error = True
                continue
            
            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$", email):
                console.print("[bold red]Debe ingresar un correo válido, ej: ejemplo@dominio.com.")
                error = True
                continue
            
            return email

    