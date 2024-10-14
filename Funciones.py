from controllers.sucursal_controller import SucursalController
from controllers.empleado_controller import Empleado_Controller
from utils.obtener_datos_persona import DatosPersona
from utils.obtener_datos_sucursal import DatosSucursal
from colorama import Fore, Style, init
init(autoreset=True)
from models.Sucursal import Sucursal
from database.dao import DAO
from os import system
from datetime import datetime
from beautifultable import BeautifulTable
import sys

class Funciones:
    def __init__(self):
        pass
                     
    def menuMesaAyuda(self):
        try:
            system("cls")
            print(Fore.GREEN + "---BIENVENIDO AL MENU DE MESA DE AYUDA---")
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
            print("Gestionar empleados\n")
            print("1. Ingresar nuevo empleado\n")
            print("2. Listar empleados\n")
            print("3. Volver a menu principal\n")
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
            else:
                print("Debe seleccionar una de las opciones disponibles, Reintentar.")
                system("pause")
                return self.__gestionEmpleados()
         except ValueError:
            print("Debe ingresar un valor válido dentro de las opciones empleados.")
            system("pause")
            return self.__gestionEmpleados()

                
                
#------------------------------------------BUSCAR MEJOR MANERA PARA MEJORAR FLUJO DE INGRESO DE DATOS--------------------

#----------------------------------------- VERIFICAR FORMATO FECHA Y VERIFICAR S_ID
    def crearEmpleado(self):
        try:
            system("cls")
            print("Crear empleado\n")
            rut, nombres, ape_paterno, ape_materno, telefono, correo, experiencia, inicio_contrato, salario = DatosPersona().obtenerDatos()
            self.listarSucursales()
            s_id = int(input("Ingrese el ID de la sucursal para asignar al empleado: "))
            empleadoController = Empleado_Controller()
            empleadoController.crearEmpleado(rut, nombres, ape_paterno, ape_materno, telefono, correo, experiencia, inicio_contrato, salario, s_id)
        except ValueError:
            print("Uno de los valores ingresados no es válido. Reintentar.")
            system("pause")
            
        
    def listarEmpleado(self):
        datos = Empleado_Controller()
        empleados = datos.listarEmpleados()
        if not empleados:
            system("cls")
            print("No se encontraron empleados registrados")
            system("pause")
            self.menuMesaAyuda()
        else:
            system("cls")
            print("Listar Usuarios")
            tabla = BeautifulTable()
            tabla.columns.header = ["ID EMPLEADO","RUT", "NOMBRES", "APE_PATERNO", "APE_MATERNO", "TELEFONO", "CORREO", "EXPERIENCIA", "INICIO CONTRATO", "SALARIO", "SUCURSAL"]
            for empleado in empleados:
                tabla.rows.append([empleado[0], empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6], empleado[7], empleado[8], empleado[9], empleado[10]])
            print(tabla)
            system("pause")
        
        
    
    def __gestionSucursales(self):
        try:

            system('cls')
            print("MENU SUCURSALES")
            print("1. Crear sucursal\n")
            print("2. Listar sucursales\n")
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
            print("---CREAR SUCURSAL---")
            nombre, direccion, fecha_constitucion = DatosSucursal().obtenerDatosSucursal()
            sucursal_controller = SucursalController()
            id_sucursal = sucursal_controller.crearSucursal(nombre,direccion,fecha_constitucion)
            print(f"Sucursal creada exitosamente ID: {id_sucursal}")
            select = input("Desea agregar otra sucursal?\n Y. SI    N. NO: ").upper()
            if select == 'Y':
                return self.crearSucursal()
            else:
                self.menuMesaAyuda()
        except ValueError:
            print("Debe ingresar la fecha en el formato (YYYY-MM-DD)")
            system("pause")
            return self.crearSucursal()

            
    def listarSucursales(self):
        system("cls")
        datos_sucursal = SucursalController().listarSucursales()
        table = BeautifulTable()
        table.column_headers = ["ID", "NOMBRE", "DIRECCION", "FECHA CONSTITUCION"]
        for sucursal in datos_sucursal:
            print(sucursal)
            sucursal[3]
            table.rows.append([sucursal[0], sucursal[1], sucursal[2], sucursal[3].strftime("%Y-%m-%d")])
        print(table)
        system("pause")
        
    
    def salirPrograma(self):
        system("cls")
        print("GRACIAS POR USAR EL SISTEMA")
        sys.exit()

        
        
            
            
    
func = Funciones()

func.menuMesaAyuda()
