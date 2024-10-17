from controllers.sucursal_controller import SucursalController
from controllers.empleado_controller import Empleado_Controller
from utils.obtener_datos_persona import DatosPersona
from utils.obtener_datos_sucursal import DatosSucursal
from utils.obtener_datos_empleado import DatosEmpleado
from colorama import Fore,init
init(autoreset=True)
from os import system
from beautifultable import BeautifulTable
import sys

class Funciones:
                     
    def menuMesaAyuda(self):
        try:
            system("cls")
            print(Fore.CYAN + "---BIENVENIDO AL MENU DE MESA DE AYUDA---")
            print("1. Gestion de Empleados")
            print("2. Gestion de Sucursales")
            print("3. Salir")
            opcion = int(input("Digite una opcion: "))

            if opcion == 1:
                self.__gestionEmpleados()
            elif opcion == 2:
                self.__gestionSucursales()
            elif opcion == 3:
                self.salirPrograma()
            else:
                print("Debe seleccionar una opcion válida.")
                system("pause")
                return self.menuMesaAyuda()
        except ValueError:
            print("Ingreso de dato invalido, reintentar.")
            system("pause")
            return self.menuMesaAyuda()
        
    def __gestionEmpleados(self):
         try:
            system("cls")
            print(Fore.CYAN + "---GESTIONAR EMPLEADO---")
            print("1. Ingresar nuevo empleado")
            print("2. Listar empleados")
            print("3. Volver a menu principal")
            select = int(input("Seleccionar opcion: "))
            if select == 1:
                self.crearEmpleado()
            elif select == 2:
                self.listarEmpleado()
            elif select == 3:
                self.menuMesaAyuda()
            else:
                print(Fore.RED + "Debe seleccionar una de las opciones disponibles, Reintentar.")
                system("pause")
                return self.__gestionEmpleados()
         except ValueError:
            print(Fore.RED + "Debe ingresar un valor válido dentro de las opciones empleados.")
            system("pause")
            return self.__gestionEmpleados()

                
#------------------------------------------BUSCAR MEJOR MANERA PARA MEJORAR FLUJO DE INGRESO DE DATOS--------------------

#----------------------------------------- VERIFICAR FORMATO FECHA Y VERIFICAR S_ID
    def crearEmpleado(self):
        try:
            system("cls")
            print(Fore.CYAN + "---CREAR EMPLEADO---")
            rut, nombres, ape_paterno, ape_materno, telefono, correo = DatosPersona().obtenerDatosPersona()
            experiencia, inicio_contrato, salario = DatosEmpleado().obtenerDatosEmpleado()
            self.listarSucursales(True)
            while True:
                try:
                    s_id = int(input(Fore.CYAN + "INGRESE ID SUCURSAL DE EMPLEADO: "))
                    if s_id:
                        break
                except:
                    print("ID de Sucursal es necesaria")
            empleadoController = Empleado_Controller()
            empleadoController.crearEmpleado(rut, nombres, ape_paterno, ape_materno, telefono, correo, experiencia, inicio_contrato, salario, s_id)
            print(Fore.GREEN + "¡EMPLEADO CREADO EXITOSAMENTE!")
            select = input("Desea agregar otro empleado?\n Y. SI    N. NO: ").upper()
            if select == 'Y':
                return self.crearEmpleado()
            else:
                self.menuMesaAyuda()
        except ValueError:
            print(Fore.RED + "Uno de los valores ingresados no es válido. Reintentar.")
            system("pause")
            self.menuMesaAyuda()
        except Exception as e:
            print(e, Fore.RED + "Intente nuevamente")
            system("pause")
            self.menuMesaAyuda()
            
            
        
    def listarEmpleado(self):
        datos = Empleado_Controller()
        empleados = datos.listarEmpleados()
        if not empleados:
            print(Fore.RED + "No se encontraron empleados registrados")
            system("pause")
            self.menuMesaAyuda()
        
        system("cls")
        print(Fore.BLUE + "LISTAR EMPLEADOS")
        tabla = BeautifulTable(maxwidth=150)
        tabla.columns.header = ["ID","RUT", "NOMBRES", "APE_PATERNO", "APE_MATERNO", "TELEFONO", "CORREO", "EXPERIENCIA", "INICIO CONTRATO", "SALARIO", "SUCURSAL"]
        for empleado in empleados:
            tabla.rows.append([empleado[0], empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6], empleado[7], empleado[8].strftime("%Y-%m-%d"), empleado[9], empleado[10]])
        print(tabla)
        system("pause")
        self.menuMesaAyuda()
        
    
    def __gestionSucursales(self):
        try:
            system('cls')
            print(Fore.CYAN + "---MENU SUCURSALES---")
            print("1. Ingresar nueva sucursal")
            print("2. Listar sucursales")
            print("3. Volver")
            opcion = int(input("Ingrese opcion: "))
            if opcion == 1: 
                self.crearSucursal()
            elif opcion == 2:
                self.listarSucursales()
            elif opcion == 3:
                self.menuMesaAyuda()
            else:
                print("Debe seleccionar una de las opciones disponibles")
                system("pause")
                return self.__gestionSucursales()
        except ValueError:
            print("Uno de los valores ingresados en gestion sucursales no es válido. Reintentar.")
            system("pause")
            return self.__gestionSucursales()
    
    
    def crearSucursal(self):
        try:
            system("cls")
            print(Fore.CYAN + "---CREAR SUCURSAL---")
            nombre, direccion, fecha_constitucion = DatosSucursal().obtenerDatosSucursal()
            sucursal_controller = SucursalController()
            id_sucursal = sucursal_controller.crearSucursal(nombre,direccion,fecha_constitucion)
            print(Fore.GREEN + f"SUCURSAL CREADA CON ID: {id_sucursal}")
            select = input("Desea agregar otra sucursal?\n Y. SI    N. NO: ").upper()
            if select == 'Y':
                return self.crearSucursal()
            else:
                self.menuMesaAyuda()
        except ValueError:
            print("Debe ingresar la fecha en el formato (YYYY-MM-DD)")
            system("pause")
            return self.crearSucursal()

            
    def listarSucursales(self, e:bool = False):
        datos_sucursal = SucursalController().listarSucursales()
        table = BeautifulTable()
        table.column_headers = ["ID", "NOMBRE", "DIRECCION", "FECHA CONSTITUCION"]
        system("cls")
        print(Fore.BLUE + "SUCURSALES")
        for sucursal in datos_sucursal:
            table.rows.append([sucursal[0], sucursal[1], sucursal[2], sucursal[3].strftime("%Y-%m-%d")])
        print(table)
        if not e:
            system("pause")
            self.menuMesaAyuda()
        
    
    def salirPrograma(self):
        print(Fore.YELLOW + "¡GRACIAS POR USAR EL SISTEMA!")
        sys.exit(0)

