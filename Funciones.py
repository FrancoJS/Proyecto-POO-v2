from controllers.sucursal_controller import SucursalController
from controllers.empleado_controller import EmpleadoController
from controllers.usuario_controller import UsuarioController
from controllers.asignaciones_controller import AsignacionesController
from utils.obtener_datos_persona import DatosPersona
from utils.obtener_datos_sucursal import DatosSucursal
from utils.obtener_datos_empleado import DatosEmpleado
from colorama import Fore,init
init(autoreset=True)
from os import system
from beautifultable import BeautifulTable
import sys
from getpass import getpass

class Funciones:
    
    def menuPrincipal(self):
        system("cls")
        print(Fore.CYAN + "----MENU PRINCIPAL----")
        print("1. Iniciar Sesion")
        print("2. Salir")
        opcion = int(input("Digite una opcion: "))
        
        if opcion == 1:
            self.iniciarSesion()
        elif opcion == 2:
            self.salirPrograma()
    
    
    def iniciarSesion(self):
        system("cls")
        print(Fore.CYAN + "----INICIAR SESION----")
        rut = DatosPersona().obtenerRut()
        con = getpass("Digite la Contraseña: ")
        response = UsuarioController().buscarUsuario(rut, con)
        if not response:
            print(Fore.RED + "¡Usuario no se encuentra registrado o la contraseña es incorrecta!")
            system("pause")
            return self.menuPrincipal()
        self.__perfilID = response
        
        print(Fore.GREEN + "¡INICIO DE SESION EXITOSO!")
        system("pause")
        if self.__perfilID == 1:
            self.menuMesaAyudaAdmin()
        elif self.__perfilID == 2:
            self.menuMesaAyudaSupervisor()
        
    def cerrarSesion(self):
        select = input("¿Esta seguro de cerrar sesion?\n Y. SI    N. NO: ").upper()
        if select == 'Y':
            return self.menuPrincipal()
        elif self.__perfilID == 1:
            return self.menuMesaAyudaAdmin()
        else:
            return self.menuMesaAyudaSupervisor()
        
                          
    def menuMesaAyudaAdmin(self):
        try:
            system("cls")
            print(Fore.CYAN + "---BIENVENIDO AL MENU DE ADMINISTRADOR---")
            print("1. Gestion de Empleados")
            print("2. Gestion de Sucursales")
            print("3. Gestion de Asignaciones")
            print("4. Cerrar Sesion")
            opcion = int(input("Digite una opcion: "))

            if opcion == 1:
                self.__gestionEmpleados()
            elif opcion == 2:
                self.__gestionSucursales()
            elif opcion == 3:
                self.gestionAsignaciones()
            elif opcion == 4:
                self.cerrarSesion()
            else:
                print("Debe seleccionar una opcion válida.")
                system("pause")
                return self.menuMesaAyudaAdmin()
        except ValueError:
            print("Ingreso de dato invalido, reintentar.")
            system("pause")
            return self.menuMesaAyudaAdmin()
        
    def menuMesaAyudaSupervisor(self):
        try:
            system("cls")
            print(Fore.CYAN + "---BIENVENIDO AL MENU DE SUPERVISOR---")
            print("1. Listar Empleados")
            print("2. Listar Sucursales")
            print("3. Gestion Asignaciones")
            print("4. Cerrar Sesion")
            opcion = int(input("Digite una opcion: "))

            if opcion == 1:
                self.listarEmpleados()
            elif opcion == 2:
                self.listarSucursales()
            elif opcion == 3:
                self.gestionAsignaciones()
            elif opcion == 4:
                self.cerrarSesion()
            else:
                print("Debe seleccionar una opcion válida.")
                system("pause")
                return self.menuMesaAyudaSupervisor()
        except ValueError:
            print("Ingreso de dato invalido, reintentar.")
            system("pause")
            return self.menuMesaAyudaSupervisor()
        
    def __gestionEmpleados(self):
         try:
            system("cls")
            print(Fore.CYAN + "---GESTIONAR EMPLEADO---")
            print("1. Ingresar nuevo empleado")
            print("2. Listar empleados")
            print("3. Eliminar empleados")
            print("4. Volver")
            select = int(input("Seleccionar opcion: "))
            if select == 1:
                self.crearEmpleado()
            elif select == 2:
                self.listarEmpleados()
            elif select == 3:
                self.eliminarEmpleado()
            elif select == 4:
                self.menuMesaAyudaAdmin()
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
                        s_idEnDB = SucursalController().buscarSucursalID(s_id)
                        if s_idEnDB:
                            break
                        print(Fore.RED + "¡Sucursal no existe!, Ingrese un id de sucursal valido")
                except:
                    print("ID de Sucursal es necesaria")
            empleadoController = EmpleadoController()
            empleadoController.crearEmpleado(rut, nombres, ape_paterno, ape_materno, telefono, correo, experiencia, inicio_contrato, salario, s_id)
            print(Fore.GREEN + "¡EMPLEADO CREADO EXITOSAMENTE!")
            select = input("¿Desea agregar otro empleado?\n Y. SI    N. NO: ").upper()
            if select == 'Y':
                return self.crearEmpleado()
            else:
                self.__gestionEmpleados()
        except ValueError:
            print(Fore.RED + "Uno de los valores ingresados no es válido. Reintentar.")
            system("pause")
            self.__gestionEmpleados()
        except Exception as e:
            print(e, Fore.RED + "Intente nuevamente")
            system("pause")
            self.__gestionEmpleados()
            
            
        
    def listarEmpleados(self):
        empleados = EmpleadoController().listarEmpleados()
        if not empleados:
            print(Fore.RED + "¡No se encontraron empleados registrados!")
            system("pause")
            if self.__perfilID == 1:
                self.__gestionEmpleados()
            else:
                self.menuMesaAyudaSupervisor()
        
        system("cls")
        print(Fore.BLUE + "LISTAR EMPLEADOS")
        tabla = BeautifulTable(maxwidth=150)
        tabla.columns.header = ["ID","RUT", "NOMBRES", "APE_PATERNO", "APE_MATERNO", "TELEFONO", "CORREO", "EXPERIENCIA", "INICIO CONTRATO", "SALARIO", "SUCURSAL"]
        for empleado in empleados:
            tabla.rows.append([empleado[0], empleado[1], empleado[2], empleado[3], empleado[4], empleado[5], empleado[6], empleado[7], empleado[8].strftime("%Y-%m-%d"), empleado[9], empleado[10]])
        print(tabla)
        system("pause")
        
        if self.__perfilID == 1:
            self.__gestionEmpleados()
        else:
            self.menuMesaAyudaSupervisor()
             

    def eliminarEmpleado(self):
        try:
            system("cls")
            print(Fore.CYAN + "---ELIMINAR EMPLEADO---")
            rut = DatosPersona().obtenerRut()
            confirmacion = input(Fore.RED + f"¿Esta seguro de elminar al empleado con rut {rut}?\n Y. Si  N. NO : ").upper()
            if confirmacion == "Y":
                EmpleadoController().eliminarEmpleado(rut)
                print(Fore.GREEN + "¡EMPLEADO ELIMINADO EXITOSAMENTE!")
                system("pause")
                self.__gestionEmpleados()
            else:
                self.__gestionEmpleados()
        except Exception as e:
            print(e)
            system("pause")
            self.__gestionEmpleados()

        
    def __gestionSucursales(self):
        try:
            system('cls')
            print(Fore.CYAN + "---MENU SUCURSALES---")
            print("1. Ingresar nueva sucursal")
            print("2. Listar sucursales")
            print("3. Eliminar Sucursal")
            print("4. Volver")
            opcion = int(input("Ingrese opcion: "))
            if opcion == 1: 
                self.crearSucursal()
            elif opcion == 2:
                self.listarSucursales()
            elif opcion == 3:
                self.eliminarSucursal()
            elif opcion == 4:
                self.menuMesaAyudaAdmin()
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
            select = input("¿Desea agregar otra sucursal?\n Y. SI    N. NO: ").upper()
            if select == 'Y':
                return self.crearSucursal()
            else:
                self.__gestionSucursales()
        except ValueError:
            print("Debe ingresar la fecha en el formato (YYYY-MM-DD)")
            system("pause")
            return self.crearSucursal()

            
    def listarSucursales(self, e:bool = False):
        try:
            datosSucursal = SucursalController().listarSucursales()
            if not datosSucursal:
                print(Fore.RED + "¡No se encontraron sucursales registradas!")
                system("pause")
                if self.__perfilID == 1:
                    self.__gestionSucursales()
                else:
                    self.menuMesaAyudaSupervisor()
                       
            table = BeautifulTable()
            table.column_headers = ["ID", "NOMBRE", "DIRECCION", "FECHA CONSTITUCION"]
            system("cls")
            print(Fore.BLUE + "SUCURSALES")
            for sucursal in datosSucursal:
                table.rows.append([sucursal[0], sucursal[1], sucursal[2], sucursal[3].strftime("%Y-%m-%d")])
            print(table)
            system("pause")
            if not e:
                if self.__perfilID == 1:
                    self.__gestionSucursales()
                else:
                    self.menuMesaAyudaSupervisor()
        except Exception as e:
            print(e)

    def eliminarSucursal(self, id):
        print(Fore.CYAN + "---Eliminar Sucursal---")
        pass
            
            
    def eliminarSucursal(self):
        try:
            system("cls")
            print(Fore.CYAN + "---Eliminar sucursal---")
            self.listarSucursales(True)
            while True:
                try:
                    s_id = int(input("Ingrese el número de la Sucursal a ELIMINAR : "))
                    if s_id:
                        s_idEnDB = SucursalController().buscarSucursalID(s_id)
                        if s_idEnDB:
                            break
                        print(Fore.RED + "Sucursal no Existe, ingrese un número de Sucursal Valido!")
                except:
                    print(Fore.RED + "Se necesita la ID de una Sucursal")
            confirmacion = input(f"¿ESTÁ SEGURO DE ELIMINAR LA SUCURSAL {s_id}?  Y. Si  N. No : ")
            if confirmacion == "Y":
                SucursalController().eliminarSucursal(s_id)
                print(Fore.GREEN + "SUCURSAL ELIMINADA CON ÉXITO")
                system("pause")
                self.__gestionSucursales()
            else:
                print("Ok. Vuelves al Menú Sucursales")
                system("pause")
                self.__gestionSucursales()
        except Exception as e:
            system("cls")
            print(e)
            system("pause")
            self.__gestionSucursales
                              
         
    def gestionAsignaciones(self):
        try:
            system('cls')
            print(Fore.CYAN + "---MENU ASIGNACIONES---")
            print("1. Listar asignaciones")
            print("2. Reasignar empleado a nueva sucursal")
            print("3. Volver")
            opcion = int(input("Ingrese opcion: "))
            if opcion == 1: 
                self.listarAsignaciones()
                pass
            elif opcion == 2:
                self.reasignarEmpleado()
                pass
            elif opcion == 3:
                if self.__perfilID == 1:
                    self.menuMesaAyudaAdmin()
                else:
                    self.menuMesaAyudaSupervisor()
            else:
                print("Debe seleccionar una de las opciones disponibles")
                system("pause")
                return self.gestionAsignaciones()
        except ValueError:
            print("Uno de los valores ingresados en gestion sucursales no es válido. Reintentar.")
            system("pause")
            return self.gestionAsignaciones()
        
    def listarAsignaciones(self):
        try:
            datosAsignaciones = AsignacionesController().listarAsignaciones()
            if not datosAsignaciones:
                print(Fore.RED + "¡No existen asignaciones!")
                system("pause")
                self.gestionAsignaciones()

            table = BeautifulTable(maxwidth=150)
            table.column_headers = ["ID EMPLEADO", "RUT EMPLEADO", "NOMBRES EMPLEADO", "APELLIDOS EMPLEADO", "ID SUCURSAL", "NOMBRE SUCURSAL", "DIRECCION SUCURSAL" ]
            system("cls")
            print(Fore.BLUE + "ASIGNACIONES DE EMPLEADOS A SUCURSALES")
            for asignacion in datosAsignaciones:
                table.rows.append([asignacion[0], asignacion[1], asignacion[2], asignacion[3], asignacion[4], asignacion[5], asignacion[6]])
            print(table)
            system("pause")
            self.gestionAsignaciones()
        except Exception as e:
            print(e)
            
    def reasignarEmpleado(self):
        try:
            system("cls")
            print(Fore.CYAN + "---REASIGNAR EMPLEADO---")
            rut = DatosPersona.obtenerRut()
            while True:
                try:
                    s_id = int(input("ID SUCURSAL NUEVA: "))
                    if s_id:
                        s_idEnDB = SucursalController().buscarSucursalID(s_id)
                        if s_idEnDB:
                            break
                        print(Fore.RED + "¡Sucursal no existe!, Ingrese un id de sucursal valido.")
                except:
                    print("ID de Sucursal es necesaria")
                
            AsignacionesController().reasignarEmpleado(rut, s_id)
            print(Fore.GREEN + "¡RESIGNACION EXITOSA!")
            system("pause")
            self.gestionAsignaciones()
        except Exception as e:
            print(e)
            system("pause")
            return self.gestionAsignaciones()
                   
        
    def salirPrograma(self):
        print(Fore.YELLOW + "¡GRACIAS POR USAR EL SISTEMA!")
        sys.exit(0)


