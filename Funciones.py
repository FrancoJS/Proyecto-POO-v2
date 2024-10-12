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
                
    #rut:str, nombres:str, ape_paterno:str, ape_materno:str, telefono:int, correo:str,
                #experiencia:#int, inicio_contrato:date, salario:int, s_id:int):
    def crearEmpleado(self):
        while True:
            try:
                system("cls")
                print("Crear empleado\n")
                nombres = input("Ingrese el nombre del empleado: ").strip()
                if not nombres:
                    print("El nombre del empleado no puede estar vacio ni contener numeros")
                    system("pause")
                    continue
                ape_paterno = input("Ingrese el apellido del empleado: ").strip()
                if not ape_paterno:
                    print("El apellido del empleado no puede estar vacio")
                    system("pause")
                    continue
                ape_materno = input("Ingrese el apellido materno del empleado: ").strip()
                if not ape_materno:
                    print("El apellido materno del empleado no puede estar vacío")
                    system("pause")
                    continue
                telefono = int(input("Ingrese número teléfono del empleado: "))
                if not telefono:
                    print("El número de teléfono del empleado no puede estar vacío")
                    system("pause")
                    continue
                correo = input("Ingrse correo del empleado: ")
                if not correo:
                    print("El correo del empleado no puede estar vacío")
                    system("pause")
                    continue
                experiencia = int(input("Ingrese la experiencia del empleado: "))
                if experiencia < 0:
                    print("La experiencia del empleado no puede ser negativa")
                    system("pause")
                if not experiencia:
                    print("La experiencia del empleado no puede estar vacía")
                    system("pause")
                    continue
                inicio_contrato = input("Ingrese la fecha de inicio de contrato del empleado (YYYY-MM-DD)")
                if not inicio_contrato:
                    print("La fecha de inicio de contrato del empleado no puede estar vacía")
                    system("pause")
                    continue
                salario = int(input("Ingrese salario del empleado: "))
                if salario <0:
                    print("El salario del empleado no puede ser negativo")
                    system("pause")
                elif not salario:
                    print("El salario del empleado no puede estar vacío")
                    system("pause")
                    continue
            except ValueError:
                print("Uno de los valores ingresados en crear empleado no es valido. Reintentar")
                system("pause")
            
        
    def listarEmpleado(self):
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
