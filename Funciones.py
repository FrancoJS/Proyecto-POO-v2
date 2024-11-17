from controllers.sucursal_controller import SucursalController
from controllers.empleado_controller import EmpleadoController
from controllers.usuario_controller import UsuarioController
from controllers.asignaciones_controller import AsignacionesController
from utils.obtener_datos_persona import DatosPersona
from utils.obtener_datos_sucursal import DatosSucursal
from utils.obtener_datos_empleado import DatosEmpleado
from utils.mensajes import MENSAJES, redirigir, reintentar
from colorama import Fore,init
init(autoreset=True)
from os import system
from beautifultable import BeautifulTable
import os
from getpass import getpass


from rich.console import Console
from rich.table import Table
from rich import box
import time
from rich.prompt import Prompt


class Funciones:
    
    console = Console()
    console50 = Console(width=80)
    
    def menuPrincipal(self):
        try:
            system("cls")
            console = self.console
            table = Table(title="[cyan]MENU PRINCIPAL", style="bold yellow", box=box.ROUNDED)
            table.add_column("[cyan]Opción[cyan]", style="bold white", justify="center")
            table.add_column("[cyan]Descripción[cyan]", style="bold white", )
            table.add_row("1", "Iniciar Sesión")
            table.add_row("2", "Salir")
            console.print(table)

            opcion = int(console.input("[bold white]Digite una opción: [/bold white]"))
        
            if opcion == 1:
                return self.iniciarSesion()
            elif opcion == 2:
                return self.salirPrograma()
            else:
                raise Exception 
        except:
            print(MENSAJES["error"])
            system("pause")
            self.menuPrincipal()
    
    
    def iniciarSesion(self):
        try:
            system("cls")
            console = self.console50
            console.rule("[cyan]INICIO DE SESIÓN", style="bold white")
            rut = DatosPersona().obtenerRut()
            con = getpass("Contraseña: ")
            response = UsuarioController().buscarUsuario(rut, con)
            if not response:
                print(Fore.RED + "¡Usuario no se encuentra registrado o la contraseña es incorrecta!")
                system("pause")
                raise Exception
            
            self.__perfilID = response
            console.print("[bold green]¡Inicio de Sesión Exitoso!")
            
            if self.__perfilID == 1:
                redirigir("Redirigiendo a Menu De Administrador...")
                return self.menuMesaAyudaAdmin()
            elif self.__perfilID == 2:
                redirigir("Redirigiendo a Menu De Supervisor...")
                return self.menuMesaAyudaSupervisor()
        except:
            redirigir("Volviendo a Menu Principal...")
            return self.menuPrincipal()
        
        
    def cerrarSesion(self):
        console = self.console
        opcion = console.input("[bold white]¿Esta seguro de cerrar sesión? [bold yellow](S/N): ").strip().upper()
        if opcion == "S":
            redirigir("Cerrando Sesión...")
            return self.menuPrincipal()
        elif opcion == "N" and self.__perfilID == 1:
            return self.menuMesaAyudaAdmin()
        elif opcion == "N" and self.__perfilID == 2:
            return self.menuMesaAyudaSupervisor()
        else:
            print(MENSAJES["error"])
            return self.cerrarSesion()
        
                                
    def menuMesaAyudaAdmin(self):
        try:
            system("cls")
            console = Console()
            table = Table(title="[cyan]BIENVENIDO AL MENU DE ADMINISTRADOR", style="bold yellow", box=box.ROUNDED)
            table.add_column("[cyan]Opción[cyan]", style="bold white", justify="center")
            table.add_column("[cyan]Descripción[cyan]", style="bold white", )
            table.add_row("1", "Gestión de Empleados")
            table.add_row("2", "Gestión de Sucursales")
            table.add_row("3", "Gestión de Asignaciones")
            table.add_row("4", "Cerrar Sesión")
            console.print(table)
            opcion = int(console.input("[bold white]Digite una opción: "))

            if opcion == 1:
                return self.__gestionEmpleados()
            elif opcion == 2:
                return self.__gestionSucursales()
            elif opcion == 3:
                return self.gestionAsignaciones()
            elif opcion == 4:
                return self.cerrarSesion()
            else:
                print(MENSAJES["error"])
                system("pause")
                return self.menuMesaAyudaAdmin()
        except ValueError:
            print(MENSAJES["error"])
            system("pause")
            return self.menuMesaAyudaAdmin()
        
        
    def menuMesaAyudaSupervisor(self):
        try:
            system("cls")
            console = self.console
            table = Table(title="[cyan]BIENVENIDO AL MENU DE SUPERVISOR", style="bold yellow", box=box.ROUNDED)
            table.add_column("[cyan]Opción[cyan]", style="bold white", justify="center")
            table.add_column("[cyan]Descripción[cyan]", style="bold white", )
            table.add_row("1", "Listar Empleados")
            table.add_row("2", "Listar Sucursales")
            table.add_row("3", "Gestión de Asignaciones")
            table.add_row("4", "Cerrar Sesión")
            console.print(table)
            opcion = int(console.input("[bold white]Digite una opción: "))

            if opcion == 1:
                return self.listarEmpleados()
            elif opcion == 2:
                return self.listarSucursales()
            elif opcion == 3:
                return self.gestionAsignaciones()
            elif opcion == 4:
                return self.cerrarSesion()
            else:
                print(MENSAJES["error"])
                system("pause")
                return self.menuMesaAyudaSupervisor()
        except ValueError:
            print(MENSAJES["error"])
            system("pause")
            return self.menuMesaAyudaSupervisor()
        
        
    def __gestionEmpleados(self):
         try:
            system("cls")
            console = self.console
            table = Table(title="[cyan]GESTIONAR EMPLEADOS", style="bold yellow", box=box.ROUNDED)
            table.add_column("[cyan]Opción[cyan]", style="bold white", justify="center")
            table.add_column("[cyan]Descripción[cyan]", style="bold white", )
            table.add_row("1", "Crear Empleado")
            table.add_row("2", "Listar Empleados")
            table.add_row("3", "Modificar Empleados")
            table.add_row("4", "Eliminar Empleado")
            table.add_row("5", "Volver")
            console.print(table)

            opcion = int(console.input("[bold white]Digite una opción: "))
            if opcion == 1:
                return self.crearEmpleado()
            elif opcion == 2:
                return self.listarEmpleados()
            elif opcion == 3:
                return self.modificarEmpleado()
            elif opcion == 4:
                return self.eliminarEmpleado()
            elif opcion == 5:
                return self.menuMesaAyudaAdmin()
            else:
                print(MENSAJES["error"])
                system("pause")
                return self.__gestionEmpleados()
         except ValueError:
            print(MENSAJES["error"])
            system("pause")
            return self.__gestionEmpleados()


    def crearEmpleado(self):
        try:
            system("cls")
            console = self.console50
            console.rule(title="[cyan]CREAR EMPLEADO", style="bold white")
            rut, nombres, ape_paterno, ape_materno, telefono, correo = DatosPersona().obtenerDatosPersona()
            experiencia, inicio_contrato, salario = DatosEmpleado().obtenerDatosEmpleado()
            self.listarSucursales(True)
            while True:
                try:
                    s_id = int(console.input("[bold cyan]Ingrese ID de Sucursal de Empleado: "))
                    if s_id:
                        s_idEnDB = SucursalController().buscarSucursalID(s_id)
                        if s_idEnDB:
                            break
                        
                        console.print("[bold red]¡Sucursal no existe!, [bold white]Ingrese un id de sucursal válido.")
                        if not reintentar():
                           redirigir("Volviendo a menu Gestión Empleados...")
                           return self.__gestionEmpleados() 
                except:
                    print(Fore.RED + "¡ID de Sucursal es necesaria!")
            empleadoController = EmpleadoController()
            empleadoController.crearEmpleado(rut, nombres, ape_paterno, ape_materno, telefono, correo, experiencia, inicio_contrato, salario, s_id)
            console.print("[bold green]¡Empleado creado exitosamente!")
            while True:
                confirmacion = console.input("[bold white]¿Desea agregar otro empleado? [bold yellow](S/N): ").strip().upper()
                if confirmacion == 'S':
                    redirigir("Volviendo a opcion Crear Empleado...")
                    return self.crearEmpleado()
                elif confirmacion == "N":
                    redirigir("Volviendo a menu Gestión Empleados...")
                    return self.__gestionEmpleados()
                else:
                    print(MENSAJES["error"])
        except:
            redirigir("Volviendo a menu Gestión Empleados...")
            return self.__gestionEmpleados()
            
        
    def listarEmpleados(self, e:bool = False):
        try:
            empleados = EmpleadoController().listarEmpleados()
            if not empleados:
                print(Fore.RED + "¡No se encontraron empleados registrados!")
                system("pause")
                if self.__perfilID == 1:
                    self.__gestionEmpleados()
                else:
                    self.menuMesaAyudaSupervisor()
                return
            system("cls")
            console = Console()
            table = Table(title="[cyan]EMPLEADOS REGISTRADOS[/cyan]", style="bold yellow")
            columnas = ["ID","RUT", "NOMBRES", "APE_PATERNO", "APE_MATERNO", "TELEFONO", "CORREO", "EXPERIENCIA", "INICIO CONTRATO", "SALARIO(clp)", "ID SUCURSAL"]
            for columna in columnas:
                table.add_column("[bold cyan]" + columna + "[bold cyan]", style="bold white", justify="center")
                
            for empleado in empleados:
                table.add_row(str(empleado[0]), empleado[1], empleado[2], empleado[3], empleado[4], "+56 " + str(empleado[5]), empleado[6], str(empleado[7]) + " años", empleado[8].strftime("%Y-%m-%d"), "$" + str(empleado[9]), str(empleado[10]))
                                
            console.print(table)
            volver = console.input("[bold white]Presiona una tecla para continuar...")

            if not e:
                if self.__perfilID == 1:
                    redirigir("Volviendo a Menu Gestion Empleados...")
                    return self.__gestionEmpleados()
                else:
                    redirigir("Volviendo a Menu de Supervisor...")
                    return self.menuMesaAyudaSupervisor()
        except Exception as e:
            print(e)


    def eliminarEmpleado(self):
        try:
            while True:
                system("cls")
                self.listarEmpleados(True)
                console = self.console50
                console.rule(title="[cyan]ELIMINAR EMPLEADO", style="bold white")
                rut = DatosPersona().obtenerRut()
                empleado_controller = EmpleadoController()
                empleado = empleado_controller.buscarEmpleadoPorRut(rut)

                if not empleado:
                    console.print("[bold red]¡Empleado no existe!, [bold white]Ingreselo uno válido.")
                    
                    if not reintentar():
                        redirigir("Volviendo a menu Gestión Empleados...")
                        return self.__gestionEmpleados()
                    else:
                        continue

                while True:
                    confirmacion = console.input(f"[bold white]¿Esta seguro de eliminar al empleado con Rut [bold yellow]{rut}? (S/N): ").strip().upper()
                    if confirmacion == "S":
                        empleado_controller.eliminarEmpleado(rut)
                        console.print("[bold green]¡Empleado eliminado Exitosamente!")
                        opcion = console.input("[bold white]¿Desea eliminar otro empleado? [bold yellow](S/N): ").strip().upper()
                        if opcion == "S":
                            redirigir("Volviendo a opcion Eliminar Empleado...")
                            break
                        else:
                            redirigir("Volviendo a menu Gestión Empleados...")
                            return self.__gestionEmpleados()
                    elif confirmacion == "N":
                        redirigir("Volviendo a menu Gestión Empleados...")
                        return self.__gestionEmpleados()
                    else:
                        print(MENSAJES["error"])
        except Exception as e:
            print(e)
            system("pause")
            self.__gestionEmpleados()


    def modificarEmpleado(self):
        try:
            system("cls")
            self.listarEmpleados(e=True)
            print(Fore.CYAN + "---MODIFICAR EMPLEADO---")
            e_id = int(input("Seleccione el ID del empleado a modificar\nIngrese ID Empleado: "))
            empleado_controller = EmpleadoController()
            if not empleado_controller.verificarE_ID(e_id):
                print(Fore.RED + "El ID ingresado no existe o no es valido. Reintente.")
                system("pause")
                self.__gestionEmpleados()
            else:
                print(Fore.GREEN + f"Empleado ID: {e_id} Seleccionada!")
                system("pause")
            rut, nombres, apellido_p, apellido_m, telefono, correo = DatosPersona().obtenerDatosPersona()
            experiencia, inicio_contrato, salario = DatosEmpleado().obtenerDatosEmpleado()
            EmpleadoController().modificarEmpleado(e_id, rut, nombres, apellido_p, apellido_m, telefono, correo, experiencia, inicio_contrato, salario)
            system("pause")
            self.__gestionEmpleados()
        except ValueError:
            print(Fore.RED + "Error: El ID ingresado no es valido.")
            system("pause")
            self.__gestionEmpleados()
        except Exception as e:
            print(e)
            system("pause")
            self.__gestionEmpleados()
        
        
    def __gestionSucursales(self):
        try:
            system('cls')
            console = Console()
            table = Table(title="[cyan]MENU SUCURSALES[cyan]", style="bold yellow")
            table.add_column("[cyan]Opción[cyan]", style="bold white", justify="center")
            table.add_column("[cyan]Descripción[cyan]", style="bold white", )
            table.add_row("1", "Crear Sucursal")
            table.add_row("2", "Listar Sucursales")
            table.add_row("3", "Modificar Sucursales")
            table.add_row("4", "Eliminar Sucursal")
            table.add_row("5", "Volver")
            console.print(table)
            
            opcion = int(input("Ingrese opcion: "))
            if opcion == 1: 
                self.crearSucursal()
            elif opcion == 2:
                self.listarSucursales()
            elif opcion == 3:
                self.modificarSucursal()
            elif opcion == 4:
                self.eliminarSucursal()
            elif opcion == 5:
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
            system("cls")
            console = Console()
            table = Table(title="[cyan]SUCURSALES REGISTRADAS[cyan]", style="bold yellow")
            columnas = ["ID", "NOMBRE", "DIRECCION", "FECHA CONSTITUCION"]
            
            for columna in columnas:
                table.add_column("[bold cyan]" + columna + "[/bold cyan]", justify="center", style="bold white")
            
            for sucursal in datosSucursal:
                table.add_row(str(sucursal[0]), sucursal[1], sucursal[2], sucursal[3].strftime("%Y-%m-%d"))
            console.print(table)
            system("pause")
            if not e:
                if self.__perfilID == 1:
                    self.__gestionSucursales()
                else:
                    self.menuMesaAyudaSupervisor()
        except Exception as e:
            print(e)
            
            
    def eliminarSucursal(self):
        try:
            system("cls")
            print(Fore.CYAN + "--- ELIMINAR SUCURSAL ---")
            self.listarSucursales(True)
            while True:
                try:
                    s_id = int(input("Ingrese el ID de la Sucursal a ELIMINAR: "))
                    if s_id:
                        s_idEnDB = SucursalController().buscarSucursalID(s_id)
                        if s_idEnDB:
                            break
                        print(Fore.RED + "Sucursal no Existe, ingrese un número de Sucursal Valido!")
                        opcion = input("¿Desea intentar denuevo? (S/N): ").strip().upper()
                        if opcion == "N":
                            print(Fore.LIGHTBLUE_EX + "Volviendo a menu Gestion Sucursales...")
                            system("pause")
                            self.__gestionSucursales()
                except:
                    print(Fore.RED + "Se necesita la ID de una Sucursal")
            
            empleadosEnSucursal = EmpleadoController().buscarEmpleadoPorSucursal(s_id)
            if empleadosEnSucursal:
                self.listarEmpleados(True)
                while True:
                    try:
                        print(Fore.YELLOW + "\n---ADVERTENCIA---")
                        print("Se encontraron Empleados en la Sucursal seleccionada!")
                        print("Usted tiene las siguientes opciones:")
                        print("1. Eliminar Empleado(os) Asignados a la Sucursal")
                        print("2. Reasignar Empleado(os) a otra Sucursal")
                        opcion = int(input(Fore.LIGHTCYAN_EX + "Por favor, seleccione una opción: "))  
                        if opcion == 1:
                            confirmacion = input(Fore.LIGHTRED_EX + f"¿Esta seguro de eliminar la sucursal con ID {s_id} y todos sus empleados? (S/N): ").strip().upper()
                            if confirmacion == "N":
                                print("Volviendo a Menu Gestion Sucursales...")
                                system("pause")
                                self.__gestionSucursales()
                            elif confirmacion == "S":
                                EmpleadoController().eliminarEmpleadoPorSucursal(s_id)
                                SucursalController().eliminarSucursal(s_id)
                                print(Fore.GREEN + "ELIMINACION COMPLETADA CON ÉXITO!")
                                print("Volviendo a Menu Gestion Sucursales...")
                                system("pause")
                                self.__gestionSucursales()
                        elif opcion == 2:
                            print("Redirigiendo a Menú Asignaciones...")
                            system("pause")
                            self.gestionAsignaciones()
                    except:
                        print(Fore.RED + "Se debe Digitar 1 o 2")
                        system("pause")
        except:
            system("pause")
            self.__gestionSucursales()
                              
    
    def modificarSucursal(self):
        try:
            system("cls")
            self.listarSucursales(True) #e sirve para llamar a la funcion listar pero no redirige a ese menu
            print(Fore.CYAN + "---MODIFICAR SUCURSAL---")
            s_id = int(input("Seleccione el ID de la sucursal que desea modificar\nIngrese ID: "))
            sucursal_controller = SucursalController()
            if not sucursal_controller.verificarS_ID(s_id):
                print(Fore.RED + "El ID ingresado no existe o no es valido. Reintente.")
                system("pause")
                self.__gestionSucursales()
            else:
                print(Fore.GREEN + f"Sucursal ID: {s_id} Seleccionada!")
            nombre, direccion, fecha_constitucion = DatosSucursal().obtenerDatosSucursal()
            SucursalController().modificarSucursal(s_id, nombre, direccion, fecha_constitucion)
            system("pause")
            self.__gestionSucursales()
        except ValueError:
            print("Debe ingresar un valor valido. Reintente.")
            system("pause")
            self.__gestionSucursales()
        except Exception as e:
            print(e)
            system("pause")
            self.__gestionSucursales()
    
    
    def gestionAsignaciones(self):
        try:
            system('cls')
            console = Console()
            table = Table(title="[cyan]MENU ASIGNACIONES[cyan]", style="bold yellow")
            table.add_column("[cyan]Opción[cyan]", style="bold white", justify="center")
            table.add_column("[cyan]Descripción[cyan]", style="bold white", )
            table.add_row("1", "Listar Asignaciones")
            table.add_row("2", "Reasignar Empleado")
            table.add_row("3", "Volver")
            console.print(table)
            
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
            print("Uno de los valores ingresados en gestion asignaciones no es válido. Reintentar.")
            system("pause")
            return self.gestionAsignaciones()
        
        
    def listarAsignaciones(self):
        try:
            datosAsignaciones = AsignacionesController().listarAsignaciones()
            if not datosAsignaciones:
                print(Fore.RED + "¡No existen asignaciones!")
                system("pause")
                self.gestionAsignaciones()

            system("cls")
            console = Console()
            table = Table(title="[cyan]ASIGNACIONES DE EMPLEADOS A SUCURSALES[cyan]", style="bold yellow")
            columnas = ["ID EMPLEADO", "RUT EMPLEADO", "NOMBRES EMPLEADO", "APELLIDOS EMPLEADO", "ID SUCURSAL", "NOMBRE SUCURSAL", "DIRECCION SUCURSAL" ]
    
            for columna in columnas:
                table.add_column("[bold cyan]" + columna + "[bold cyan]", justify="center", style="bold white")
    
            for asignacion in datosAsignaciones:
                table.add_row(str(asignacion[0]), asignacion[1], asignacion[2], asignacion[3], str(asignacion[4]), asignacion[5], asignacion[6])
            console.print(table)
            system("pause")
            self.gestionAsignaciones()
        except Exception as e:
            print(e)
            
            
    def reasignarEmpleado(self):
        try:
            system("cls")
            self.listarEmpleados(True)
            print(Fore.CYAN + "---REASIGNAR EMPLEADO---")
            print(Fore.LIGHTBLUE_EX + "Ingrese RUT de Empleado y Sucursal a la que desea reasignar")
            rut = DatosPersona.obtenerRut()
            empleado = EmpleadoController().buscarEmpleadoPorRut(rut)
            
            if not empleado:
                print(Fore.RED + "¡Empleado no existe!, Ingrese un RUT valido.")
                opcion = input("¿Desea intentar denuevo? (S/N): ").strip().upper()
                if opcion == 'S':
                    print(Fore.LIGHTBLUE_EX + "Volviendo a opcion Reasignar Empleado...")
                    system("pause")
                    return self.reasignarEmpleado()
                else:
                    print(Fore.LIGHTBLUE_EX + "Volviendo a menu Gestion Asignaciones...")
                    system("pause")
                    self.gestionAsignaciones()
            
            print(Fore.LIGHTBLUE_EX + "Monstrando Sucursales disponibles para Reasignacion")
            system("pause")
            self.listarSucursales(True)
            while True:
                try:
                    s_id = int(input("ID SUCURSAL NUEVA: "))
                    if s_id:
                        s_idEnDB = SucursalController().buscarSucursalID(s_id)
                        if s_idEnDB:
                            break
                        print(Fore.RED + "¡Sucursal no existe!, Ingrese un id de sucursal valido.")
                        opcion = input("¿Desea intentar denuevo? (S/N): ").strip().upper()
                        if opcion == "N":
                            print(Fore.LIGHTBLUE_EX + "Volviendo a menu Gestion Asignaciones...")
                            system("pause")
                            self.gestionAsignaciones()
                except:
                    print(Fore.RED + "¡ID de Sucursal es necesaria!, Ingresela nuevamente.")
                
            AsignacionesController().reasignarEmpleado(rut, s_id, empleado)
            print(Fore.GREEN + "¡RESIGNACION EXITOSA!")
            system("pause")
            self.gestionAsignaciones()
        except Exception as e:
            print(e)
            system("pause")
            return self.gestionAsignaciones()
                   
        
    def salirPrograma(self):
        print(Fore.YELLOW + "¡GRACIAS POR USAR EL SISTEMA!")
        os._exit(0)
