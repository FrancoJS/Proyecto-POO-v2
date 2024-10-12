
from controllers.sucursal_controller import SucursalController
from utils.obtener_datos_persona import DatosPersona
from colorama import Fore, Style, init
init(autoreset=True)
from models.Sucursal import Sucursal
from database.dao import DAO
from os import system
from datetime import datetime

class Funciones:
    def __init__(self):
        pass
                     
    def menuMesaAyuda(self):
        system("cls")
        print("---BIENVENIDO AL MENU DE MESA DE AYUDA---")
        print("1. Gestion de Empleados")
        print("2. Gestion de Sucursales")
        opcion = int(input("Digite una opcion: "))
        
        if opcion == 1:
            self.__gestionEmpleados()
        elif opcion == 2:
            self.__gestionSucursales()
            
    def __gestionEmpleados(self):
        print("MENU EMPLEADOS")
        
    def __gestionSucursales(self):
        system('cls')
        print("MENU SUCURSALES")
        print("1. Crear sucursal")
        opcion = int(input("Ingrese opcion"))
        if opcion == 1: 
            self.crearSucursal()
        
    def crearSucursal(self):
        try:
            system("cls")
            print("---CREAR SUCURSAL---")
            nombre = str(input("Ingrese el nombre: "))
            direccion = str(input("Ingrese direccion: "))
            fecha_constitucion = input("Ingrese la fecha (YYYY-MM-DD): ")
            fecha = datetime.strptime(fecha_constitucion,'%Y-%m-%d')
            sucursal_controller = SucursalController()
            id_sucursal = sucursal_controller.crearSucursal(nombre,direccion,fecha)
            print(f"Sucursal creada exitosamente ID: {id_sucursal}")
        except Exception as e:
            print(e)
        except ValueError:
            print("Debe ingresar la fecha en el formato (YYYY-MM-DD)")
            
    def crearEmpleado(self):
        
        pass
            
            
    
func = Funciones()
# func.registrarUsuario()
# func.iniciarSesion()
# func.crearSucursal()
func.menuMesaAyuda()