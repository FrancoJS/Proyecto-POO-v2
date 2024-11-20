from colorama import Fore
from utils.mensajes_templates import reintentar
import re
import bcrypt


def hashPassword(password):
    salt = bcrypt.gensalt()
    hashedPassword = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashedPassword.decode("utf-8")   


def comparePassword(password, hashedPassword):
    return bcrypt.checkpw(password.encode("utf-8"), hashedPassword.encode("utf-8"))


def obtenerClave(console, error: bool = False) -> str:
        console = console
        while True:
            if error:
                if not reintentar():
                    raise Exception

            clave = console.input("[bold cyan]Clave: ").strip()

            if len(clave) < 8 or len(clave) > 20:
                print(Fore.RED + "La clave debe tener entre 8 y 20 caracteres.")
                error = True
                continue
            
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
            
            
            return clave