from datetime import datetime
import re
from colorama import Fore
from os import system

class DatosPersona:
    
    def obtenerDatosPersona(self):
        try:
            rut = self.obtenerRut()
            nombres = self.__obtenerNombre()
            apellido_p = self.__obtenerApellido("PATERNO")
            apellido_m = self.__obtenerApellido("MATERNO")
            telefono = self.__obtenerTelefono()
            correo = self.__obtenerCorreo()
            return rut, nombres, apellido_p, apellido_m, telefono, correo
        except:
            raise Exception
        
        
    @staticmethod
    def obtenerRut(error:bool = False) -> str:
        while True:
            if error:
                opcion = input("¿Desea intentar denuevo? (S/N): ").strip().upper()
                if opcion == "N":
                    raise Exception
                
            print(Fore.YELLOW + "Si el digito verificador de su rut es 'K' reemplacelo con 0")
            rut = input("Rut: ").strip()
                         
            if len(rut) < 2 or len(rut) > 12:
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
                
                
    @staticmethod
    def __obtenerNombre(error:bool = False) -> str:
        while True:
            if error:
                opcion = input("¿Desea intentar denuevo? (S/N): ").strip().upper()
                if opcion == "N":
                    raise Exception
                
            nombres = input("NOMBRES: ").strip()
            if not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", nombres):
                print(Fore.RED + "Los nombres solo deben contener caracteres válidos.")
                error = True
                continue
            
            elif len(nombres) < 1 or len(nombres) > 50:
                print(Fore.RED + "El nombre debe tener entre 1 y 50 caracteres.")
                error = True
                continue
                
            return nombres
        
        
    @staticmethod
    def __obtenerApellido(tipo:str, error:bool = False) -> str:
        while True:
            if error:
                opcion = input("¿Desea intentar denuevo? (S/N): ").strip().upper()
                if opcion == "N":
                    raise Exception
                
            apellido = input(f"APELLIDO {tipo}: ").strip()
            if not apellido.isalpha():
                print(Fore.RED + "El apellido no debe contener caracteres especiales ni espacios.")
                error = True
                continue
            
            elif len(apellido) < 1 or len(apellido) > 30:
                print(Fore.RED + "El apellido debe tener entre 1 y 30 caracteres.")
                error = True
                continue
            
            return apellido
        
        
    @staticmethod
    def __obtenerTelefono(error:bool = False) -> int:
        while True:
            if error:
                opcion = input("¿Desea intentar denuevo? (S/N): ").strip().upper()
                if opcion == "N":
                    raise Exception
                
            telefono = input("TELEFONO: +56")
            
            if not telefono.isdigit():
                print(Fore.RED + "El teléfono debe contener solo números.")
                error = True
                continue
            
            if len(telefono) != 9:
                print(Fore.RED + "El télefono debe tener 9 números.")
                error = True
                continue
            
            return int(telefono)
        
        
    @staticmethod
    def __obtenerCorreo(error:bool = False) -> str:
        while True:
            if error:
                opcion = input("¿Desea intentar denuevo? (S/N): ").strip().upper()
                if opcion == "N":
                    raise Exception
                
            correo = input("CORREO: ")
            
            if len(correo) < 1 or len(correo) > 50:
                print(Fore.RED + "El correo debe tener entre 1 y 50 caracteres.")
                error = True
                continue
            
            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$", correo):
                print(Fore.RED + "Debe ingresar un correo válido, ej: ejemplo@dominio.com.")
                error = True
                continue
            
            return correo
    
    