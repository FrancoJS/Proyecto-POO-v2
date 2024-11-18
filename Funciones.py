from controllers.sucursal_controller import SucursalController
from controllers.empleado_controller import EmpleadoController
from controllers.usuario_controller import UsuarioController
from controllers.asignaciones_controller import AsignacionesController
from utils.obtener_datos_persona import DatosPersona
from utils.obtener_datos_sucursal import DatosSucursal
from utils.obtener_datos_empleado import DatosEmpleado
from utils.mensajes import MENSAJES, redirigir, reintentar
from utils.get_data_json import obtenerBecasAPI
from colorama import Fore,init
init(autoreset=True)
from os import system
import os
from getpass import getpass

from rich.console import Console
from rich.table import Table
from rich import box


class Funciones:
    
    console = Console()
    console80 = Console(width=80)
    
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
            console = self.console80
            console.rule("[cyan]INICIO DE SESIÓN", style="bold yellow")
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
            table.add_row("4", "Recuperar datos JSON")
            table.add_row("5", "Cerrar Sesión")
            console.print(table)
            opcion = int(console.input("[bold white]Digite una opción: "))

            if opcion == 1:
                return self.__gestionEmpleados()
            elif opcion == 2:
                return self.__gestionSucursales()
            elif opcion == 3:
                return self.gestionAsignaciones()
            elif opcion == 4:
                return self.listarBecasAPI()
            elif opcion == 5:
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
            console = self.console80
            console.rule(title="[cyan]CREAR EMPLEADO", style="bold yellow")
            rut, nombres, ape_paterno, ape_materno, telefono, correo = DatosPersona().obtenerDatosPersona()
            experiencia, inicio_contrato, salario = DatosEmpleado().obtenerDatosEmpleado()
            redirigir("Mostrando Sucursales disponibles para Asignar...")
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
                table.add_row("")
                                
            console.print(table)
            volver = console.input("[bold white]Presione una tecla para continuar...")

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
                redirigir("Mostrando Empleados disponibles para Eliminar...")
                self.listarEmpleados(True)
                console = self.console80
                console.rule(title="[cyan]ELIMINAR EMPLEADO", style="bold yellow")
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
        except:
            redirigir("Volviendo a menu Gestion Empleados...")
            return self.__gestionEmpleados()


    def modificarEmpleado(self):
        while True:
            try:
                while True:
                    system("cls")
                    redirigir("Mostrando Empleados disponibles para Modificar...")
                    self.listarEmpleados(True)
                    console = self.console80
                    console.rule("[cyan]MODIFICAR EMPLEADO", style="bold yellow")
                    e_id = int(console.input("[cyan]Ingrese ID de Empleado: "))
                    empleado_controller = EmpleadoController()
                    if not empleado_controller.verificarE_ID(e_id):
                        print(Fore.RED + "El ID ingresado no es valido.")
                        if not reintentar():
                            redirigir("Volviendo a menu Gestion Empleados...")
                            return self.__gestionEmpleados()

                        redirigir("Volviendo a opcion Modificar Empleado...")
                        continue
                    else:
                        print(Fore.GREEN + f"¡Empleado con ID {e_id} seleccionado!")

                    rut, nombres, apellido_p, apellido_m, telefono, correo = DatosPersona().obtenerDatosPersona()
                    experiencia, inicio_contrato, salario = DatosEmpleado().obtenerDatosEmpleado()
                    EmpleadoController().modificarEmpleado(e_id, rut, nombres, apellido_p, apellido_m, telefono, correo, experiencia, inicio_contrato, salario)
                    print(Fore.GREEN + "¡Empleado modificado exitosamente!")
                    while True:
                        confirmacion = console.input("[bold white]¿Desea modificar otro empleado? [bold yellow](S/N): ").strip().upper()
                        if confirmacion == 'S':
                            redirigir("Volviendo a opcion modificar Empleado...")
                            return self.modificarEmpleado()
                        elif confirmacion == "N":
                            redirigir("Volviendo a menu Gestión Empleados...")
                            return self.__gestionEmpleados()
                        else:
                            print(MENSAJES["error"])
                            
            except ValueError:
                print(Fore.RED + "El ID ingresado no es valido.")
                if not reintentar():
                    redirigir("Volviendo a menu Gestión Empleados...")
                    return self.__gestionEmpleados()
                redirigir("Volviendo a opcion Modificar Empleado...")
            except:
                redirigir("Volviendo a menu Gestión Empleados...")
                return self.__gestionEmpleados()
                  
        
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
            
            opcion = int(console.input("[bold white]Digite opción: "))
            if opcion == 1: 
                return self.crearSucursal()
            elif opcion == 2:
                return self.listarSucursales()
            elif opcion == 3:
                return self.modificarSucursal()
            elif opcion == 4:
                return self.eliminarSucursal()
            elif opcion == 5:
                return self.menuMesaAyudaAdmin()
            else:
                print(MENSAJES["error"])
                system("pause")
                return self.__gestionSucursales()
        except ValueError:
            print(MENSAJES["error"])
            system("pause")
            return self.__gestionSucursales()
    
    
    def crearSucursal(self):
        try:
            system("cls")
            console = self.console80
            console.rule(title="[cyan]CREAR SUCURSAL", style="bold yellow")
            nombre, direccion, fecha_constitucion = DatosSucursal().obtenerDatosSucursal()
            sucursal_controller = SucursalController()
            id_sucursal = sucursal_controller.crearSucursal(nombre,direccion,fecha_constitucion)
            print(Fore.GREEN + f"¡Sucursal creada Exitosamente con ID: {id_sucursal}!")
            opcion = console.input("[bold white]¿Desea agregar otra sucursal? [bold yellow](S/N) ").strip().upper()
            if opcion == 'S':
                redirigir("Volviendo a opcion Crear Sucursal...")
                return self.crearSucursal()
            else:
                redirigir("Volviendo a menu Gestion Sucursales...")
                return self.__gestionSucursales()
        except:
            redirigir("Volviendo a menu Gestion Sucursales...")
            return self.__gestionSucursales()

            
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
            console = self.console
            table = Table(title="[cyan]SUCURSALES REGISTRADAS", style="bold yellow")
            columnas = ["ID", "NOMBRE", "DIRECCION", "FECHA CONSTITUCION"]
            
            for columna in columnas:
                table.add_column("[bold cyan]" + columna + "[/bold cyan]", justify="center", style="bold white")
            
            for sucursal in datosSucursal:
                table.add_row(str(sucursal[0]), sucursal[1], sucursal[2], sucursal[3].strftime("%Y-%m-%d"))
                table.add_row("")
                
            console.print(table)
            volver = console.input("[bold white]Presione una tecla para continuar...")
            
            if not e:
                if self.__perfilID == 1:
                    redirigir("Volviendo a menu Gestión Sucursales...")
                    self.__gestionSucursales()
                else:
                    redirigir("Volviendo a Menu Supervisor...")
                    self.menuMesaAyudaSupervisor()
        except Exception as e:
            print(e)
            
            
    def eliminarSucursal(self):
     
        while True:
            system("cls")
            console = self.console80
            redirigir("Mostrando Sucursales disponibles para Eliminar...")
            self.listarSucursales(True)
            console.rule(title="[cyan]ELIMINAR SUCURSAL", style="bold yellow")
            try:
                s_id = int(console.input("[cyan]Ingrese ID de Sucursal: "))
                if s_id:
                    s_idEnDB = SucursalController().buscarSucursalID(s_id)
                    if s_idEnDB:
                        break
                    console.print("[bold red]¡Sucursal no Existe!, [bold white]Ingrese un ID de Sucursal valido.")
                    if not reintentar():
                        redirigir("Volviendo a menu Gestión Sucursales...")
                        self.__gestionSucursales()
                    
                    redirigir("Volviendo a opcion Eliminar Sucursal...")
                    continue
            except:
                print(Fore.RED + "El ID ingresado no es válido.")
                system("pause")
        
        empleadosEnSucursal = EmpleadoController().buscarEmpleadoPorSucursal(s_id)
        if empleadosEnSucursal:
            redirigir(f"Mostrando Empleados asociados a Sucursal con ID {s_id}...")
            self.listarEmpleadosPorSucursal(empleadosEnSucursal, s_id)
            while True:
                try:
                    console.rule(title="[bold red]¡ADVERTENCIA!", style="bold yellow")
                    console.print("[bold red]Se encontraron Empleados en la Sucursal seleccionada")
                    console.print("[bold white]Usted tiene las siguientes opciones:")
                    console.print("[bold yellow]1) [bold white]Eliminar Empleado(os) Asignados a la Sucursal")
                    console.print("[bold yellow]2) [bold white]Reasignar Empleado(os) a otra Sucursal")
                    opcion = int(console.input("[bold white]Digite una opcion: "))  
                    if opcion == 1:
                        while True:
                            confirmacion = console.input(f"[bold white]¿Esta seguro de eliminar la sucursal con ID {s_id} y sus empleados asociados? [bold yellow](S/N): ").strip().upper()
                            if confirmacion == "N":
                                redirigir("Volviendo a menu Gestion Sucursales...")
                                return self.__gestionSucursales()
                            elif confirmacion == "S":
                                EmpleadoController().eliminarEmpleadoPorSucursal(s_id)
                                SucursalController().eliminarSucursal(s_id)
                                print(Fore.GREEN + "¡Eliminación completada con Éxito!")
                                while True:
                                    seguir = console.input("[bold white]¿Desea eliminar otra sucursal? [bold yellow](S/N): ").strip().upper()
                                    if seguir == 'S':
                                        redirigir("Volviendo a opcion Eliminar Sucursal...")
                                        return self.eliminarSucursal()
                                    elif seguir == "N":
                                        redirigir("Volviendo a menu Gestión Sucursales...")
                                        return self.__gestionSucursales()
                                    else:
                                        print(MENSAJES["error"])
                            else:
                                print(MENSAJES["error"])
                    elif opcion == 2:
                        redirigir("Redirigiendo a menu Gestion Asignaciones...")
                        self.gestionAsignaciones()
                    else:
                        raise Exception
                except:
                    print(MENSAJES["error"])
                    system("pause")
        else:
            while True:
                confirmacion = console.input(f"[bold white]¿Esta seguro de eliminar la sucursal con ID {s_id}? [bold yellow](S/N): ").strip().upper()
                if confirmacion == "S":
                    SucursalController().eliminarSucursal(s_id)
                    print(Fore.GREEN + "¡Eliminación completada con Éxito!")
                    while True:
                        opcion = console.input("[bold white]¿Desea eliminar otra sucursal? [bold yellow](S/N): ").strip().upper()
                        if opcion == 'S':
                            redirigir("Volviendo a opcion Eliminar Sucursal...")
                            return self.eliminarSucursal()
                        elif opcion == "N":
                            redirigir("Volviendo a menu Gestión Sucursales...")
                            return self.__gestionSucursales()
                        else:
                            print(MENSAJES["error"])
                elif confirmacion == "N":
                    redirigir("Volviedo a menu Gestion Sucursales...")
                    return self.__gestionSucursales()
                else:
                    print(MENSAJES["error"])
            
        
            
    def listarEmpleadosPorSucursal(self,empleados, s_id):
        try:
            system("cls")
            console = self.console
            table = Table(title=f"[cyan]EMPLEADOS ASOCIADOS A LA SUCURSAL CON ID {s_id}", style="bold yellow")
            columnas = ["ID","RUT", "NOMBRES", "APELLIDOS", "TELEFONO", "CORREO", "ID SUCURSAL"]
    
            for columna in columnas:
                table.add_column("[bold cyan]" + columna + "[bold cyan]", justify="center", style="bold white")
    
            for empleado in empleados:
                table.add_row(str(empleado[0]), empleado[1], empleado[2], empleado[3], "+56 " + str(empleado[4]), empleado[5], str(empleado[6]))
                table.add_row("")
                
            console.print(table)
            volver = console.input("[bold white]Presione una tecla para continuar...")
        except Exception as e:
            print(e)
            print("Que pedo")
                              
    
    def modificarSucursal(self):
        while True:
            system("cls")
            redirigir("Mostrando Sucursales disponibles para Modificar...")
            self.listarSucursales(True) 
            console = self.console80
            console.rule(title="[cyan]MODIFICAR SUCURSAL", style="bold yellow")

            try:
                s_id = int(console.input("[cyan]Ingrese ID de Sucursal: "))
                if s_id:
                    s_idEnDB = SucursalController().buscarSucursalID(s_id)
                    if s_idEnDB:
                        break
                    console.print("[bold red]¡Sucursal no Existe!, [bold white]Ingrese un ID de Sucursal valido.")
                    if not reintentar():
                        redirigir("Volviendo a menu Gestión Sucursales...")
                        self.__gestionSucursales()
                
                    redirigir("Volviendo a opcion Eliminar Sucursal...")
                    continue
            except:
                print(Fore.RED + "El ID ingresado no es válido.")
                if not reintentar():
                    redirigir("Volviendo a menu Gestión Sucursales...")
                    self.__gestionSucursales()
                redirigir("Volviendo a opcion Eliminar Sucursal...")
                
        try:
            print(Fore.GREEN + f"Sucursal con ID {s_id} seleccionada!")
            nombre, direccion, fecha_constitucion = DatosSucursal().obtenerDatosSucursal()
            SucursalController().modificarSucursal(s_id, nombre, direccion, fecha_constitucion)
            print(Fore.GREEN + "¡Sucursal modificada exitosamente!")
            while True:
                confirmacion = console.input("[bold white]¿Desea modificar otra sucursal? [bold yellow](S/N): ").strip().upper()
                if confirmacion == 'S':
                    redirigir("Volviendo a opcion Modificar Sucursal...")
                    return self.modificarSucursal()
                elif confirmacion == "N":
                    redirigir("Volviendo a menu Gestión Sucursales...")
                    return self.__gestionSucursales()
                else:
                    print(MENSAJES["error"])
        except:
            redirigir("Volviendo a opcion menu Gestion Sucursal...")
            self.__gestionSucursales()
    
    
    def gestionAsignaciones(self):
        try:
            system('cls')
            console = self.console
            table = Table(title="[cyan]MENU ASIGNACIONES[cyan]", style="bold yellow", box=box.ROUNDED)
            table.add_column("[cyan]Opción[cyan]", style="bold white", justify="center")
            table.add_column("[cyan]Descripción[cyan]", style="bold white", )
            table.add_row("1", "Listar Asignaciones")
            table.add_row("2", "Reasignar Empleado")
            table.add_row("3", "Volver")
            console.print(table)
            
            opcion = int(input("Digite opción: "))
            if opcion == 1: 
                return self.listarAsignaciones()
                
            elif opcion == 2:
                return self.reasignarEmpleado()
                
            elif opcion == 3:
                if self.__perfilID == 1:
                    self.menuMesaAyudaAdmin()
                else:
                    self.menuMesaAyudaSupervisor()
            else:
                print(MENSAJES["error"])
                system("pause")
                return self.gestionAsignaciones()
        except ValueError:
            print(MENSAJES["error"])
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
            console = self.console
            table = Table(title="[cyan]ASIGNACIONES DE EMPLEADOS A SUCURSALES[cyan]", style="bold yellow")
            columnas = ["ID EMPLEADO", "RUT EMPLEADO", "NOMBRES EMPLEADO", "APELLIDOS EMPLEADO", "ID SUCURSAL", "NOMBRE SUCURSAL", "DIRECCION SUCURSAL" ]
    
            for columna in columnas:
                table.add_column("[bold cyan]" + columna + "[bold cyan]", justify="center", style="bold white")
    
            for asignacion in datosAsignaciones:
                table.add_row(str(asignacion[0]), asignacion[1], asignacion[2], asignacion[3], str(asignacion[4]), asignacion[5], asignacion[6])
                table.add_row("")
            console.print(table)
            
            volver = input("Presione una tecla para continuar...")
            redirigir("Volviendo a menu Asignaciones...")
            self.gestionAsignaciones()
        except Exception as e:
            print(e)
            
            
    def reasignarEmpleado(self):
        try:
            while True:
                system("cls")
                redirigir("Mostrando Empleados disponibles para Reasignación...")
                self.listarEmpleados(True)
                console = self.console80
                console.rule(title="[cyan]REASIGNAR EMPLEADO", style="bold yellow")
                console.print("[bold white]Ingrese RUT de Empleado y Sucursal a la que desea reasignar")
                rut = DatosPersona().obtenerRut()
                empleado = EmpleadoController().buscarEmpleadoPorRut(rut)

                if not empleado:
                    print(Fore.RED + "¡Empleado no existe!, Ingrese un RUT válido.")
                    if not reintentar():
                        redirigir("Volviendo a menu Gestion Asignaciones")
                        return self.gestionAsignaciones()
                    continue

                redirigir("Mostrando Sucursales disponibles para Reasignación...")
                self.listarSucursales(True)
                while True:
                    try:
                        s_id = int(console.input("[cyan]Ingrese ID de Sucursal Nueva: "))
                        if s_id:
                            s_idEnDB = SucursalController().buscarSucursalID(s_id)
                            if s_idEnDB:
                                break
                            console.print("[bold red]¡Sucursal no existe!, [bold white]Ingrese un ID de sucursal valido.")
                            if not reintentar():
                                redirigir("Volviendo a menu Gestión Asignaciones")
                                return self.gestionAsignaciones()
                    except:
                        print(Fore.RED + "¡ID de Sucursal es necesaria!, Ingresela nuevamente.")
                        

                AsignacionesController().reasignarEmpleado(rut, s_id, empleado)
                print(Fore.GREEN + "¡Reasignacion Exitosa!")
                while True:
                    confirmacion = console.input("[bold white]¿Desea reasignar a otro Empleado? [bold yellow](S/N): ").strip().upper()
                    if confirmacion == 'S':
                        redirigir("Volviendo a opcion Reasignar Empleado...")
                        return self.reasignarEmpleado()
                    elif confirmacion == "N":
                        redirigir("Volviendo a menu Gestión Asignaciones...")
                        return self.__gestionEmpleados()
                    else:
                        print(MENSAJES["error"])
        except Exception as e:
            print(e)
            system("pause")
            return self.gestionAsignaciones()
                   
        
    def salirPrograma(self):
        console = self.console
        while True:
            confirmacion = console.input("[bold white]¿Esta seguro de salir de sistema? [bold yellow](S/N): ").strip().upper()
            if confirmacion == 'S':
                redirigir("Saliendo...")
                console.print("[bold yellow]¡Gracias por usar el sistema!")
                os._exit(0)
            elif confirmacion == "N":
                return self.menuPrincipal()
            else:
                print(MENSAJES["error"])
                system("pause")
            

    def listarBecasAPI(self):
        try:
            system("cls")
            console = self.console
            becas = obtenerBecasAPI()
            table = Table(title="[cyan]LISTADO DE BECAS",style="bold yellow")
            columnas = ["ID", "NOMBRE", "PAIS", "UNIVERSIDAD", "DURACIÓN", "DESCRIPCIÓN", "REQUISITOS", "COBERTURA"]
            
            for columna in columnas:
                table.add_column("[cyan]" + columna + "[cyan]", style="bold white", justify="center")
                
            for beca in becas:
                id_beca = str(beca["id"])
                nombre = beca["nombre"]
                pais = beca["detalles"]["pais"]
                universidad = beca["detalles"]["universidad"]
                duracion = beca["detalles"]["duracion"]
                descripcion = beca["detalles"]["descripcion"]
                requisitos = ", ".join(beca["detalles"]["requisitos"])
                cobertura = beca["detalles"]["cobertura"]
            
                table.add_row(id_beca, nombre, pais, universidad, duracion, descripcion,requisitos,cobertura)
                table.add_row("")
            
            console.print(table)
            volver = console.input("[bold white]Presione una tecla para continuar...")
            redirigir("Volviendo a Menu Administrador...")
            self.menuMesaAyudaAdmin()
                
        except Exception as e:
            console.print(f"[bold white]Error en la solicitud: [bold red]{e}")
            