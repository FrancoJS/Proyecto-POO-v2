from datetime import datetime
import re
from colorama import Fore

class DatosPersona:
    
    def obtenerDatosPersona(self):
        rut = self.obtenerRut()
        nombres = self.__obtenerNombre()
        apellido_p = self.__obtenerApellido("PATERNO")
        apellido_m = self.__obtenerApellido("MATERNO")
        telefono = self.__obtenerTelefono()
        correo = self.__obtenerCorreo()
        return rut, nombres, apellido_p, apellido_m, telefono, correo
        
    @staticmethod
    def obtenerRut() -> str:
        while True:
            print(Fore.YELLOW + "Si el digito verificador de su rut es 'K' reemplacelo con 0")
            rut = input("RUT: ").strip()
                         
            if len(rut) < 2 or len(rut) > 12:
                print(Fore.RED + "La longitud del RUT no es válida.")
                continue
                
            rut = rut.replace(".","").replace("-","")
            if len(rut) > 9:
                print(Fore.RED + "La longitud del RUT no es válida.")
                continue
                
            numero, dv = rut[:-1], rut[-1]
            if not numero.isdigit() or not dv.isdigit():
                print(Fore.RED + "El RUT y dígito verificador deben ser números.")
                continue
                
            rut_validado = f"{numero}-{dv}"
            return rut_validado
                
    @staticmethod
    def __obtenerNombre() -> str:
        while True:   
            nombres = input("NOMBRES: ").strip()
            if not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", nombres):
                print(Fore.RED + "Los nombres solo deben contener caracteres válidos.")
                continue
            
            elif len(nombres) < 1 or len(nombres) > 50:
                print(Fore.RED + "El nombre debe tener entre 1 y 50 caracteres.")
                continue
                
            return nombres
        
    @staticmethod
    def __obtenerApellido(tipo:str) -> str:
        while True:
            apellido = input(f"APELLIDO {tipo}: ").strip()
            if not apellido.isalpha():
                print(Fore.RED + "El apellido no debe contener caracteres especiales ni espacios.")
                continue
            
            elif len(apellido) < 1 or len(apellido) > 30:
                print(Fore.RED + "El apellido debe tener entre 1 y 30 caracteres.")
                continue
            
            return apellido
        
    @staticmethod
    def __obtenerTelefono() -> int:
        while True:
            telefono = input("TELEFONO: +56")
            
            if not telefono.isdigit():
                print(Fore.RED + "El teléfono debe contener solo números.")
                continue
            
            if len(telefono) != 9:
                print(Fore.RED + "El télefono debe tener 9 números.")
                continue
            
            return int(telefono)
        
    @staticmethod
    def __obtenerCorreo() -> str:
        while True:
            correo = input("CORREO: ")
            
            if len(correo) < 1 or len(correo) > 50:
                print(Fore.RED + "El correo debe tener entre 1 y 50 caracteres.")
                continue
            
            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$", correo):
                print(Fore.RED + "Debe ingresar un correo válido, ej: ejemplo@dominio.com.")
                continue
            
            return correo
    
    