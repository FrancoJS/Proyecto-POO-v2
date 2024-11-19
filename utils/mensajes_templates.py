from colorama import Fore
import time
from rich.console import Console
from os import system

MENSAJES = {
    "error": Fore.RED + "¡Debe ingresar una opción valida!"
}

console = Console()

def redirigir(mensaje):
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
            print(MENSAJES["error"])
            system("pause")
            