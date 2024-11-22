from utils.messages_templates import reintentar
import re
import bcrypt
from rich.prompt import Prompt


def hash_password(password) -> str:
    salt = bcrypt.gensalt()
    hashedPassword = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashedPassword.decode("utf-8")   


def compare_password(password, hashed_password) -> bool:
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


def get_password(console, error: bool = False, login: bool = False) -> str:
        console = console
        while True:
            if error:
                if not reintentar():
                    raise Exception("Cancelado por el usuario.")

            clave = Prompt.ask("[bold cyan]Clave", password=True).strip()
            
            if len(clave) < 8 or len(clave) > 20:
                console.print("[bold red]La clave debe tener entre 8 y 20 caracteres.")
                error = True
                continue
            
            if not login:
                confirmacion = Prompt.ask("[bold cyan]Confirmar clave", password=True).strip()

                if clave != confirmacion:
                    console.print("[bold red]Las claves no coinciden. Por favor, inténtelo de nuevo.")
                    error = True
                    continue

            return clave
            
            # if not re.search(r"[A-Z]", clave):
            #     print(Fore.RED + "La clave debe incluir al menos una letra mayúscula.")
            #     error = True
            #     continue
            
            # if not re.search(r"[a-z]", clave):
            #     print(Fore.RED + "La clave debe incluir al menos una letra minúscula.")
            #     error = True
            #     continue
            
            # if not re.search(r"\d", clave):
            #     print(Fore.RED + "La clave debe incluir al menos un número.")
            #     error = True
            #     continue
            
            # if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", clave):
            #     print(Fore.RED + "La clave debe incluir al menos un carácter especial (ej.: !@#$%^&*).")
            #     error = True
            #     continue
            
            

