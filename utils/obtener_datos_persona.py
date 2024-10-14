from datetime import datetime
from os import system
import re
from colorama import Fore

class DatosPersona:
    
    def obtenerDatos(self):
        rut = self.__obtenerRut()
        nombres = self.__obtenerNombre()
        apellido_p = self.__obtenerApellido("PATERNO")
        apellido_m = self.__obtenerApellido("MATERNO")
        telefono = self.__obtenerTelefono()
        correo = self.__obtenerCorreo()
        experiencia = self.__obtenerExperiencia()
        inicio_contrato = self.__obtenerFechaContrato()
        salario = self.__obtenerSalario()
        return rut, nombres, apellido_p, apellido_m, telefono, correo, experiencia, inicio_contrato, salario
        
    @staticmethod
    def __obtenerRut() -> str:
        while True:
            print(Fore.GREEN + "Si el digito verificador de su rut es 'K' reemplacelo con 0")
            rut = input("RUT: ").strip()
                         
            if len(rut) < 2 or len(rut) > 12:
                print("La longitud del RUT no es válida.")
                continue
                
            rut = rut.replace(".","").replace("-","")
            if len(rut) > 9:
                print("La longitud del RUT no es válida.")
                continue
                
            numero, dv = rut[:-1], rut[-1]
            if not numero.isdigit() or not dv.isdigit():
                print("El RUT y dígito verificador deben ser números.")
                continue
                
            rut_validado = f"{numero}-{dv}"
            return rut_validado
                
    @staticmethod
    def __obtenerNombre() -> str:
        while True:   
            nombres = input("NOMBRES: ").strip()
            if not re.match("^[A-Za-záéíóúÁÉÍÓÚñÑ\s]+$", nombres):
                print("Los nombres solo deben contener caracteres válidos.")
                continue
            
            elif len(nombres) < 1 or len(nombres) > 50:
                print("El nombre debe tener entre 1 y 50 caracteres.")
                continue
                
            return nombres
        
    @staticmethod
    def __obtenerApellido(tipo:str) -> str:
        while True:
            apellido = input(f"APELLIDO {tipo}: ").strip()
            if not apellido.isalpha():
                print(f"El apellido no debe contener caracteres especiales ni espacios.")
                continue
            
            elif len(apellido) < 1 or len(apellido) > 30:
                print("El apellido debe tener entre 1 y 30 caracteres.")
                continue
            
            return apellido
        
    @staticmethod
    def __obtenerTelefono() -> int:
        while True:
            telefono = input("TELEFONO: +56")
            
            if not telefono.isdigit():
                print("El teléfono debe contener solo números.")
                continue
            
            if len(telefono) != 9:
                print("El télefono debe tener 9 números.")
                continue
            
            return int(telefono)
        
    @staticmethod
    def __obtenerCorreo() -> str:
        while True:
            correo = input("CORREO: ")
            
            if len(correo) < 1 or len(correo) > 50:
                print("El correo debe tener entre 1 y 50 caracteres.")
                continue
            
            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$", correo):
                print("Debe ingresar un correo válido, ej: ejemplo@dominio.com.")
                continue
            
            return correo
    
    @staticmethod
    def __obtenerExperiencia() -> int:
        while True:
            try:
                experiencia = int(input("Ingrese la experiencia del empleado (en años): "))
                if experiencia < 0 or experiencia > 50:
                    print("La experiencia debe ser un valor entre 0 y 50 años.")
                    continue
                return experiencia
            except ValueError:
                print("Debe ingresar un número válido para la experiencia.")
    
    @staticmethod
    def __obtenerFechaContrato() -> str:
        while True:
            fecha_contrato = input("Ingrese la fecha de inicio de contrato del empleado (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(fecha_contrato, "%Y-%m-%d")
                return fecha_contrato
            except ValueError:
                print("Debe ingresar una fecha válida en el formato YYYY-MM-DD.")
    
    @staticmethod
    def __obtenerSalario() -> int:
        while True:
            try:
                salario = int(input("Ingrese el salario del empleado: "))
                if salario < 0:
                    print("El salario no puede ser negativo.")
                    continue
                return salario
            except ValueError:
                print("Debe ingresar un número válido para el salario.")
