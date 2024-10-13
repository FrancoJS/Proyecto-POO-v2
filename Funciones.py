from controllers.sucursal_controller import SucursalController
from controllers.empleado_controller import Empleado_Controller
from utils.obtener_datos_persona import DatosPersona
from database.data_baseQuerys import Data_Querys
from colorama import Fore, Style, init
init(autoreset=True)
from models.Sucursal import Sucursal
from database.dao import DAO
from os import system
from datetime import datetime
from beautifultable import BeautifulTable

class Funciones:
    def __init__(self):
        pass
                     
    def menuMesaAyuda(self):
        system("cls")
        print(Fore.GREEN + "---BIENVENIDO AL MENU DE MESA DE AYUDA---")
        print("1. Gestion de Empleados")
        print("2. Gestion de Sucursales")
        opcion = int(input("Digite una opcion: "))
        
        if opcion == 1:
            self.__gestionEmpleados()
        elif opcion == 2:
            self.__gestionSucursales()
            
#permitir la creación, listado, búsquedas, modificaciones, eliminación (anulaciones) y 
#presentación de estadística indicando cantidades, sumatorias, promedios, entre otros valores que estime conveniente.            
    def __gestionEmpleados(self):
        while True:
            try:
                system("cls")
                print("Gestionar empleados\n")
                print("1. Ingresar nuevo empleado\n")
                print("2. Listar empleados\n")
                print("3. Volver a menu principal")
                #print("3. Buscar empleado\n")
                #print("4. Modificar empleadon\n")
                #print("5. Eliminar empleado\n")
                #print("6. Mostrar Estadisticas\n")
                select = int(input("Seleccionar opcion: "))
                if select == 1:
                    self.crearEmpleado()
                elif select == 2:
                    self.listarEmpleado()
                elif select == 3:
                    self.menuMesaAyuda()
                    break
                else:
                    print("Opcion no valida, Reintentar.")
                    system("pause")
            except ValueError:
                print("Debe ingresar un valor válido dentro de las opciones empleados.")
                system("pause")

                
                
#------------------------------------------BUSCAR MEJOR MANERA PARA MEJORAR FLUJO DE INGRESO DE DATOS--------------------

#----------------------------------------- VERIFICAR FORMATO FECHA Y VERIFICAR S_ID
    def crearEmpleado(self):
        while True:
            try:
                system("cls")
                print("Crear empleado\n")
                rut = input("Ingrese el RUT del empleado: ").strip() 
                nombres = input("Ingrese el nombre del empleado: ").strip()
                ape_paterno = input("Ingrese el apellido del empleado: ").strip()
                ape_materno = input("Ingrese el apellido materno del empleado: ").strip()
                telefono = int(input("Ingrese número teléfono del empleado: "))
                correo = input("Ingrese correo del empleado: ").strip()
                experiencia = int(input("Ingrese la experiencia del empleado: "))
                inicio_contrato = input("Ingrese la fecha de inicio de contrato del empleado (YYYY-MM-DD): ")
                salario = int(input("Ingrese salario del empleado: "))
                s_id = 1
                empleadoController = Empleado_Controller()
                empleadoController.crearEmpleado(rut, nombres, ape_paterno, ape_materno, telefono, correo, experiencia, inicio_contrato, salario, s_id)
                break
            except ValueError:
                print("Uno de los valores ingresados no es válido. Reintentar.")
                system("pause")
            
        
    def listarEmpleado(self):
        datos = Data_Querys()
        empleados = datos.sql_select()
        if not empleados:
            system("cls")
            print("No se encontraron empleados registrados")
            system("pause")
            self.menuMesaAyuda()
        else:
            system("cls")
            print("Listar Usuarios")
            
            pass
                
        
        
        
    
    def __gestionSucursales(self):
        system('cls')
        print("MENU SUCURSALES")
        print("1. Crear sucursal\n")
        print("2. Listar sucursales")
        opcion = int(input("Ingrese opcion: "))
        if opcion == 1: 
            self.crearSucursal()
        elif opcion == 2:
            self.listarSucursales()
    
    
    def crearSucursal(self):
        try:
            system("cls")
            print("---CREAR SUCURSAL---")
            nombre = input("Ingrese el nombre: ")
            direccion = input("Ingrese direccion: ")
            fecha_constitucion = input("Ingrese la fecha (YYYY-MM-DD): ")
            fecha = datetime.strptime(fecha_constitucion,'%Y-%m-%d')
            sucursal_controller = SucursalController()
            id_sucursal = sucursal_controller.crearSucursal(nombre,direccion,fecha)
            print(f"Sucursal creada exitosamente ID: {id_sucursal}")
        except Exception as e:
            print(e)
        except ValueError:
            print("Debe ingresar la fecha en el formato (YYYY-MM-DD)")
            
    def listarSucursales(self):
        
        pass
        
        
            
            
    
func = Funciones()

func.menuMesaAyuda()
