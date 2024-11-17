from datetime import datetime
import re
from colorama import Fore

class DatosEmpleado: 
    
    def obtenerDatosEmpleado(self):
        experiencia = self.__obtenerExperiencia()
        inicio_contrato = self.__obtenerFechaContrato()
        salario = self.__obtenerSalario()
        return experiencia, inicio_contrato, salario
    
    
    @staticmethod
    def __obtenerExperiencia(error:bool = False) -> int:
        while True:
            if error:
                opcion = input("¿Desea intentar de nuevo? (S/N): ").strip().upper()
                if opcion == "N":
                    raise Exception
                
            try:
                experiencia = int(input("EXPERIENCIA (en años): "))
                if experiencia < 0 or experiencia > 50:
                    print(Fore.RED + "La experiencia debe ser un valor entre 0 y 50 años.")
                    error = True
                    continue
                return experiencia
            except ValueError:
                print(Fore.RED + "Debe ingresar un número válido para la experiencia.")
                error = True
    
    
    @staticmethod
    def __obtenerFechaContrato(error:bool = False) -> str:
        while True:
            if error:
                opcion = input("¿Desea intentar de nuevo? (S/N): ").strip().upper()
                if opcion == "N":
                    raise Exception
                
            fecha_contrato = input("FECHA INICIO CONTRATO (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(fecha_contrato, "%Y-%m-%d")
                return fecha_contrato
            except ValueError:
                print(Fore.RED + "Debe ingresar una fecha válida en el formato YYYY-MM-DD.")
                error = True
    
    
    @staticmethod
    def __obtenerSalario(error:bool = False) -> int:
        while True:
            if error:
                opcion = input("¿Desea intentar de nuevo? (S/N): ").strip().upper()
                if opcion == "N":
                    raise Exception
                
            try:
                salario = int(input("SALARIO (clp): $"))
                if salario < 0:
                    print(Fore.RED + "Debe ingresar un salario valido")
                    error = True
                    continue
                return salario
            except ValueError:
                print(Fore.RED + "Debe ingresar un número válido para el salario.")
                error = True
