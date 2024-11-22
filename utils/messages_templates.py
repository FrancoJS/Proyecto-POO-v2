from colorama import Fore
import time
from rich.console import Console
from os import system

MESSAGES = {
    "error": Fore.RED + "¡Debe ingresar una opción valida!"
}

console = Console()

def redirect(mensaje):
    with console.status(f"[bold yellow]{mensaje}", spinner="dots"):
        time.sleep(1.2)
    
def reintentar(): 
    while True:
        opcion = console.input("[bold white]¿Desea intentar denuevo? [bold yellow](S/N): ").strip().upper()
        if opcion == "S":
            return True
        elif opcion == "N":
            return False
        else:
            print(MESSAGES["error"])
            system("pause")

def show_confirmation(message: str = "¿Desea intentar denuevo?") -> bool:
    # Muestra un mensaje de confirmación y devuelve True si la respuesta es "S", False si es "N".
    # Acepta como argumento un mensaje personalizado para mostrar al usuario.
    
    while True:
        response = console.input(f"[bold white]{message} [bold yellow][S/N]: ").strip().upper()
        if response == "S":
            return True
        elif response == "N":
            return False
        else:
            print(MESSAGES["error"])
            
def get_perfil_id():
        while True:
            try:
                perfil_id = int(console.input("[bold cyan]Ingrese tipo de usuario (1. Administrador || 2. Supervisor): "))
                if perfil_id in (1, 2):
                    return perfil_id
                
                raise Exception            
            except:
                print(MESSAGES["error"])
                if not show_confirmation():
                    raise Exception("Cancelado por el usuario.")
    
    
def get_employee_id(employee_controller):
    while True:
        try:
            employee_id = int(console.input("[bold cyan]Ingrese ID de Empleado: "))
            if not employee_controller.verificarE_ID(employee_id):
               raise Exception("El ID ingresado no es válido.")
               
            return employee_id
        except ValueError:
            console.print("[bold red]El ID debe ser un número entero.")
        except Exception as error:
            console.print(f"[bold red]{error}")
            if not show_confirmation():
                raise Exception("Cancelado por el usuario.")
            
def pause():
    input("Presione una tecla para continuar...")