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
    
# def reintentar(): 
#     while True:
#         opcion = console.input("[bold white]¿Desea intentar denuevo? [bold yellow](S/N): ").strip().upper()
#         if opcion == "S":
#             return True
#         elif opcion == "N":
#             return False
#         else:
#             print(MESSAGES["error"])
#             system("pause")

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
            
def get_perfil_id(self):
        while True:
            try:
                perfil_id = int(self.console80.input("[bold cyan]Ingrese tipo de usuario (1. Administrador || 2. Supervisor): "))
                if perfil_id in (1, 2):
                    return perfil_id
                else:
                    raise Exception            
            except:
                MESSAGES["error"]
                if not show_confirmation():
                    redirect("Volviendo a Menu Principal...")
                    return False
    
def pause():
    input("Presione una tecla para continuar...")