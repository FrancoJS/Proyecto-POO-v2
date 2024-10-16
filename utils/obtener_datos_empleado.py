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
    def __obtenerExperiencia() -> int:
        while True:
            try:
                experiencia = int(input("EXPERIENCIA (en años): "))
                if experiencia < 0 or experiencia > 50:
                    print(Fore.RED + "La experiencia debe ser un valor entre 0 y 50 años.")
                    continue
                return experiencia
            except ValueError:
                print(Fore.RED + "Debe ingresar un número válido para la experiencia.")
    
    @staticmethod
    def __obtenerFechaContrato() -> str:
        while True:
            fecha_contrato = input("FECHA INICIO CONTRATO (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(fecha_contrato, "%Y-%m-%d")
                return fecha_contrato
            except ValueError:
                print(Fore.RED + "Debe ingresar una fecha válida en el formato YYYY-MM-DD.")
    
    @staticmethod
    def __obtenerSalario() -> int:
        while True:
            try:
                salario = int(input("SALARIO (clp): $"))
                if salario < 0:
                    print(Fore.RED + "Debe ingresar un salario valido")
                    continue
                return salario
            except ValueError:
                print(Fore.RED + "Debe ingresar un número válido para el salario.")
