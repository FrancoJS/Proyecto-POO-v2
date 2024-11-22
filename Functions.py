from controllers.sucursal_controller import SucursalController
from controllers.employee_controller import EmployeeController
from controllers.user_controller import UserController
from controllers.assignments_controller import AsignacionesController
from utils.get_data_person import PersonData
from utils.get_data_sucursal import SucursalData
from utils.get_data_employee import EmpleoyeeData
from utils.messages_templates import MESSAGES, redirect, reintentar, show_confirmation, get_perfil_id, pause, get_employee_id
from utils.get_data_api import obtenerBecasAPI
from utils.password_service import get_password
from colorama import Fore,init
init(autoreset=True)
from os import system
import os


from rich.console import Console
from rich.table import Table
from rich import box

# Crear exepciones para mejor flujo de trabajo

class Functions:
    
    console = Console()
    console80 = Console(width=80)
    
    def __init__(self):
        self.__employee_controller = EmployeeController()
        self.__user_controller = UserController()
        self.__sucursal_controller = SucursalController()
        self.__asignaciones_controller = AsignacionesController()
        self.__person_data = PersonData()
        self.__employee_data = EmpleoyeeData()
        self.__sucursal_data = SucursalData()
    
    
    def main_menu(self):
        console = self.console
        while True:
            try:
                system("cls")
                table = Table(title="[cyan]MENU PRINCIPAL", style="bold yellow", box=box.ROUNDED)
                table.add_column("[cyan]Opción[cyan]", style="bold white", justify="center")
                table.add_column("[cyan]Descripción[cyan]", style="bold white")
                table.add_row("1", "Registro de Usuarios")
                table.add_row("2", "Iniciar Sesión")
                table.add_row("3", "Salir")
                console.print(table)

                option:int = int(console.input("[bold white]Digite una opción: [/bold white]"))

                if option == 1:
                    return self.register()
                elif option == 2:
                    return self.login()
                elif option == 3:
                    return self.salirPrograma()
                else:
                    raise Exception 
            except:
                console.print(MESSAGES["error"])
                pause()
                
    
    def register(self):
        console = self.console80
        while True:
            try:
                system("cls")
                console.rule("[cyan]REGISTRO DE USUARIO", style="bold yellow")
                rut, names, paternal_surname, maternal_surname, phone_number, email = self.__person_data.get_data()
                password = get_password(console)
                perfil_id = get_perfil_id()
                
                #TO DO Lanzar una excepcion personalizada desde el controlador, para mejorar flujo de trabajo
                self.__user_controller.register_user(rut, names, paternal_surname, maternal_surname, phone_number, email, password, perfil_id)
                console.print("[bold green]¡Usuario registrado Exitosamente!")
                self._perfil_id = perfil_id
                
                if self._perfil_id == 1:
                    redirect("Redirigiendo a Menu De Administrador...")
                    return self.admin_menu()
                elif self._perfil_id == 2:
                    redirect("Redirigiendo a Menu De Supervisor...")
                    return self.supervisor_menu()
                         
            except Exception as error:
                console.print(f"[bold red]{error}")
                pause()
                redirect("Volviendo Menu Principal...")
                return self.main_menu()
            
    
    def login(self):
        console = self.console80
        while True:
            try:
                system("cls")
                console.rule("[cyan]INICIO DE SESION", style="bold yellow")
                rut = self.__person_data.get_rut()
                password = get_password(console, login=True)

                perfil_id = self.__user_controller.validate_credentials(rut, password)
                
                self._perfil_id = perfil_id
                console.print("[bold green]¡Inicio de Sesión Exitoso!")

                if perfil_id == 1:
                    redirect("Redirigiendo a Menu De Administrador...")
                    return self.admin_menu()
                elif perfil_id == 2:
                    redirect("Redirigiendo a Menu De Supervisor...")
                    return self.supervisor_menu()

            except Exception as error:
                console.print(f"[bold red]{error}")
                pause()
                redirect("Volviendo a Menu Principal...")
                return self.main_menu()
        
        
    def logout(self):
        if not show_confirmation("¿Esta seguro de cerrar sesión?"):
            if self._perfil_id == 1:
                return self.admin_menu()
            elif self._perfil_id == 2:
                return self.supervisor_menu()
        
        redirect("Cerrando Sesión...")
        return self.main_menu()
        
                                
    def admin_menu(self):
        console = self.console
        while True:
            try:
                system("cls")
                table = Table(title="[cyan]BIENVENIDO AL MENU DE ADMINISTRADOR", style="bold yellow", box=box.ROUNDED)
                table.add_column("[cyan]Opción[cyan]", style="bold white", justify="center")
                table.add_column("[cyan]Descripción[cyan]", style="bold white", )
                table.add_row("1", "Gestión de Empleados")
                table.add_row("2", "Gestión de Sucursales")
                table.add_row("3", "Gestión de Asignaciones")
                table.add_row("4", "Recuperar datos JSON")
                table.add_row("5", "Cerrar Sesión")
                console.print(table)

                option:int = int(console.input("[bold white]Digite una opción: "))
                if option == 1:
                    return self.employee_menu()
                elif option == 2:
                    return self.sucursal_menu()
                elif option == 3:
                    return self.gestionAsignaciones()
                elif option == 4:
                    return self.listarBecasAPI()
                elif option == 5:
                    return self.logout()
                else:
                    raise Exception
            except:
                print(MESSAGES["error"])
                pause()
                
        
    def supervisor_menu(self):
        while True:
            try:
                console = self.console
                system("cls")
                table = Table(title="[cyan]BIENVENIDO AL MENU DE SUPERVISOR", style="bold yellow", box=box.ROUNDED)
                table.add_column("[cyan]Opción[cyan]", style="bold white", justify="center")
                table.add_column("[cyan]Descripción[cyan]", style="bold white", )
                table.add_row("1", "Listar Empleados")
                table.add_row("2", "Listar Sucursales")
                table.add_row("3", "Gestión de Asignaciones")
                table.add_row("4", "Cerrar Sesión")
                console.print(table)

                option = int(console.input("[bold white]Digite una opción: "))
                if option == 1:
                    return self.list_employees()
                elif option == 2:
                    return self.list_sucursals()
                elif option == 3:
                    return self.gestionAsignaciones()
                elif option == 4:
                    return self.logout()
                else:
                    raise Exception
            except:
                print(MESSAGES["error"])
                pause()
            
        
    def employee_menu(self):
        while True:
            try:
               console = self.console
               system("cls")
               table = Table(title="[cyan]GESTIONAR EMPLEADOS", style="bold yellow", box=box.ROUNDED)
               table.add_column("[cyan]Opción[cyan]", style="bold white", justify="center")
               table.add_column("[cyan]Descripción[cyan]", style="bold white", )
               table.add_row("1", "Agregar Empleado")
               table.add_row("2", "Listar Empleados")
               table.add_row("3", "Modificar Empleado")
               table.add_row("4", "Eliminar Empleado")
               table.add_row("5", "Volver")
               console.print(table)

               option:int = int(console.input("[bold white]Digite una opción: "))
               if option == 1:
                   return self.add_employee()
               elif option == 2:
                   return self.list_employees()
               elif option == 3:
                   return self.modify_employee()
               elif option == 4:
                   return self.delete_employee()
               elif option == 5:
                   return self.admin_menu()
               else:
                   raise Exception
            except:
               print(MESSAGES["error"])
               pause()
            

    def add_employee(self):
        console = self.console80
        while True:
            try:
                sucursal_data = self.__sucursal_controller.list_sucursals()
                if not sucursal_data:
                    console.print("[bold red]¡No existen sucursales creadas, porfavor agregue una sucursal primero para poder agregar un Empleado!")
                    pause()   
                    return self.employee_menu()

                system("cls")
                console.rule(title="[cyan]CREAR EMPLEADO", style="bold yellow")
                rut, names, paternal_surname, maternal_surname, phone_number, email = self.__person_data.get_data()
                experience, hire_date, salary = self.__employee_data.get_data()

                redirect("Mostrando Sucursales disponibles para Asignar...")
                self.list_sucursals(True)
                sucursal_id = self.__sucursal_data.get_sucursal_id(self.__sucursal_controller)

                self.__employee_controller.add_employee(rut, names, paternal_surname, maternal_surname, phone_number, email, experience, hire_date, salary, sucursal_id)
                
                console.print("[bold green]¡Empleado creado exitosamente!")

                if not show_confirmation("¿Desea agregar otro Empleado?"):
                    redirect("Volviendo a menu Gestión Empleados...")
                    return self.employee_menu()

                redirect("Volviendo a opcion Crear Empleado...")
        
            except Exception as error:
                console.print(f"[bold red]{error}")
                pause()
                redirect("Volviendo a menu Gestión Empleados...")
                return self.employee_menu()
            
        
    def list_employees(self, no_redirect:bool = False, from_assignments:bool = False):   
        try:
            console = self.console
            employees_data = EmployeeController().list_employees()
            if not employees_data:
                console.print("[bold red]¡No se encontraron empleados registrados!")
                pause()
                if from_assignments:
                    redirect("Volviendo a menu Gestion Asignaciones...")
                    return self.gestionAsignaciones()
                
                if self._perfil_id == 1:
                    return self.employee_menu()
                elif self._perfil_id == 2:
                    return self.supervisor_menu()
                
            system("cls")
            table = Table(title="[cyan]EMPLEADOS REGISTRADOS[/cyan]", style="bold yellow")
            columns = ["ID","RUT", "NOMBRES", "APE_PATERNO", "APE_MATERNO", "TELEFONO", "CORREO", "EXPERIENCIA", "INICIO CONTRATO", "SALARIO(clp)", "ID SUCURSAL"]
            for column in columns:
                table.add_column("[bold cyan]" + column + "[bold cyan]", style="bold white", justify="center")
                
            for employee in employees_data:
                table.add_row(str(employee[0]), employee[1], employee[2], employee[3], employee[4], "+56 " + str(employee[5]), employee[6], str(employee[7]) + " años", employee[8].strftime("%Y-%m-%d"), "$" + str(employee[9]), str(employee[10]))
                table.add_row("")
                                
            console.print(table)
            pause()

            if not no_redirect:
                if self._perfil_id == 1:
                    redirect("Volviendo a Menu Gestion Empleados...")
                    return self.employee_menu()
                elif self._perfil_id == 2:
                    redirect("Volviendo a Menu de Supervisor...")
                    return self.supervisor_menu()
                
        except Exception as error:
            console.print(f"[bold red]{error}")
            pause()
            return self.employee_menu() if self._perfil_id == 1 else self.supervisor_menu()

  
    def delete_employee(self):
        console = self.console80
        while True:
            try:
                system("cls")
                redirect("Mostrando Empleados disponibles para Eliminar...")
                self.list_employees(no_redirect=True)
                console.rule(title="[cyan]ELIMINAR EMPLEADO", style="bold yellow")
                rut = self.__person_data.get_rut(console)
                
                if not self.__employee_controller.employee_exists_by_rut(rut):
                    console.print("[bold red]¡Empleado no existe!, Ingreselo uno válido.")     
                    if not show_confirmation():
                        redirect("Volviendo a menu Gestión Empleados...")
                        return self.employee_menu()
                    continue
                
                if not show_confirmation(f"¿Esta seguro de eliminar al empleado con Rut {rut}?"):
                    redirect("Volviendo a menu Gestión Empleados...")
                    return self.employee_menu()
                
                self.__employee_controller.delete_employee(rut)
                console.print("[bold green]¡Empleado eliminado Exitosamente!")
                 
                if not show_confirmation("¿Desea eliminar otro empleado?"):
                    redirect("Volviendo a menu Gestión Empleados...")
                    return self.employee_menu()
                
                redirect("Volviendo a opcion Eliminar Empleado...")
            except Exception as error:
                console.print(f"[bold red]{error}")
                pause()
                redirect("Volviendo a menu Gestion Empleados...")
                return self.employee_menu()


    def modify_employee(self):
        console = self.console80
        while True:
            try:
                system("cls")
                redirect("Mostrando Empleados disponibles para Modificar...")
                self.list_employees(no_redirect=True)
                console.rule("[cyan]MODIFICAR EMPLEADO", style="bold yellow")
                
                employee_id = get_employee_id(self.__employee_controller)
                rut, names, paternal_surname, maternal_surname, phone_number, email = self.__person_data.get_data()
                experience, hire_date, salary = self.__employee_data.get_data()
                
                self.__employee_controller.modify_employee(employee_id, rut, names, paternal_surname, maternal_surname, phone_number, email, experience, hire_date, salary)
                
                console.print("[bold green]¡Empleado modificado exitosamente!")
                
                if not show_confirmation("¿Desea modificar otro empleado?"):
                    redirect("Volviendo a menu Gestión Empleados...")
                    return self.employee_menu()
                
                redirect("Volviendo a opcion modificar Empleado...") 
            except Exception as error:
                console.print(f"[bold red]{error}")
                pause()
                redirect("Volviendo a menu Gestión Empleados...")
                return self.employee_menu()
                  
        
    def sucursal_menu(self):
        while True:
            try:
                console = self.console
                system('cls')
                table = Table(title="[cyan]MENU SUCURSALES[cyan]", style="bold yellow")
                table.add_column("[cyan]Opción[cyan]", style="bold white", justify="center")
                table.add_column("[cyan]Descripción[cyan]", style="bold white", )
                table.add_row("1", "Agregar Sucursal")
                table.add_row("2", "Listar Sucursales")
                table.add_row("3", "Modificar Sucursales")
                table.add_row("4", "Eliminar Sucursal")
                table.add_row("5", "Volver")
                console.print(table)

                option = int(console.input("[bold white]Digite opción: "))
                if option == 1: 
                    return self.add_sucursal()
                elif option == 2:
                    return self.list_sucursals()
                elif option == 3:
                    return self.modificarSucursal()
                elif option == 4:
                    return self.eliminarSucursal()
                elif option == 5:
                    return self.admin_menu()
                else:
                    raise Exception
            except:
                print(MESSAGES["error"])
                pause()

    
    def add_sucursal(self):
        console = self.console80
        while True:
            try:
                system("cls")
                console.rule(title="[cyan]CREAR SUCURSAL", style="bold yellow")
                name, address, constitution_date = self.__sucursal_data.get_data()
                self.__sucursal_controller.add_sucursal(name, address, constitution_date)
                console.print("[bold green]¡Sucursal creada Exitosamente con!")

                if not show_confirmation("¿Desea agregar otra Sucursal?"):
                    redirect("Volviendo a menu Gestión Sucursales...")
                    return self.sucursal_menu()

                redirect("Volviendo a opcion Crear Sucursal...")
            except Exception as error:
                console.print(f"[bold red]{error}")
                pause()
                redirect("Volviendo a menu Gestion Sucursales...")
                return self.sucursal_menu()

            
    def list_sucursals(self, no_redirect:bool = False):
        try:
            sucursals_data = SucursalController().list_sucursals()
            if not sucursals_data:
                console.print("[bold red]¡No se encontraron sucursales registradas!")
                pause()
                if self._perfil_id == 1:
                    return self.sucursal_menu()
                elif self._perfil_id == 2:
                    return self.supervisor_menu()
                
            system("cls")
            console = self.console
            table = Table(title="[cyan]SUCURSALES REGISTRADAS", style="bold yellow")
            columnas = ["ID", "NOMBRE", "DIRECCION", "FECHA CONSTITUCION"]
            
            for columna in columnas:
                table.add_column("[bold cyan]" + columna + "[/bold cyan]", justify="center", style="bold white")
            
            for sucursal in sucursals_data:
                table.add_row(str(sucursal[0]), sucursal[1], sucursal[2], sucursal[3].strftime("%Y-%m-%d"))
                table.add_row("")
                
            console.print(table)
            pause()
            
            if not no_redirect:
                if self._perfil_id == 1:
                    redirect("Volviendo a menu Gestión Sucursales...")
                    return self.sucursal_menu()
                elif self._perfil_id == 2:
                    redirect("Volviendo a Menu Supervisor...")
                    return self.supervisor_menu()
        except Exception as error:
            console.print(f"[bold red]{error}")
            pause()
            return self.sucursal_menu()
            
            
    def eliminarSucursal(self):
        empleados_controller = self.__employee_controller
        sucursal_controller = self.__sucursal_controller
        console = self.console80
        system("cls")
        redirect("Mostrando Sucursales disponibles para Eliminar...")
        self.list_sucursals(True)
        console.rule(title="[cyan]ELIMINAR SUCURSAL", style="bold yellow")
        while True:
            try:
                s_id = int(console.input("[bold cyan]Ingrese ID de Sucursal: "))
                if s_id:
                    s_idEnDB = sucursal_controller.buscarSucursalID(s_id)
                    if s_idEnDB:
                        break
                    console.print("[bold red]¡Sucursal no Existe!, Ingrese un ID de Sucursal valido.")
                    if not reintentar():
                        redirect("Volviendo a menu Gestión Sucursales...")
                        return self.sucursal_menu()
                    
                    continue
            except:
                print(Fore.RED + "El ID ingresado no es válido.")
                system("pause")
        
        empleadosEnSucursal = empleados_controller.buscarEmpleadoPorSucursal(s_id)
        if empleadosEnSucursal:
            redirect(f"Mostrando Empleados asociados a Sucursal con ID {s_id}...")
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
                                redirect("Volviendo a menu Gestion Sucursales...")
                                return self.sucursal_menu()
                            elif confirmacion == "S":
                                empleados_controller.eliminarEmpleadoPorSucursal(s_id)
                                sucursal_controller.eliminarSucursal(s_id)
                                print(Fore.GREEN + "¡Eliminación completada con Éxito!")
                                while True:
                                    seguir = console.input("[bold white]¿Desea eliminar otra sucursal? [bold yellow](S/N): ").strip().upper()
                                    if seguir == 'S':
                                        redirect("Volviendo a opcion Eliminar Sucursal...")
                                        return self.eliminarSucursal()
                                    elif seguir == "N":
                                        redirect("Volviendo a menu Gestión Sucursales...")
                                        return self.sucursal_menu()
                                    else:
                                        print(MESSAGES["error"])
                            else:
                                print(MESSAGES["error"])
                    elif opcion == 2:
                        redirect("Redirigiendo a menu Gestion Asignaciones...")
                        self.gestionAsignaciones()
                    else:
                        raise Exception
                except:
                    print(MESSAGES["error"])
                    system("pause")
        else:
            while True:
                confirmacion = console.input(f"[bold white]¿Esta seguro de eliminar la sucursal con ID {s_id}? [bold yellow](S/N): ").strip().upper()
                if confirmacion == "S":
                    sucursal_controller.eliminarSucursal(s_id)
                    print(Fore.GREEN + "¡Eliminación completada con Éxito!")
                    while True:
                        opcion = console.input("[bold white]¿Desea eliminar otra sucursal? [bold yellow](S/N): ").strip().upper()
                        if opcion == 'S':
                            redirect("Volviendo a opcion Eliminar Sucursal...")
                            return self.eliminarSucursal()
                        elif opcion == "N":
                            redirect("Volviendo a menu Gestión Sucursales...")
                            return self.sucursal_menu()
                        else:
                            print(MESSAGES["error"])
                elif confirmacion == "N":
                    redirect("Volviedo a menu Gestion Sucursales...")
                    return self.sucursal_menu()
                else:
                    print(MESSAGES["error"])
            
        
    def listarEmpleadosPorSucursal(self, empleados, s_id):
        try:
            console = self.console
            system("cls")
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
        sucursal_controller = self.__sucursal_controller
        console = self.console80
        system("cls")
        redirect("Mostrando Sucursales disponibles para Modificar...")
        self.list_sucursals(True) 
        console.rule(title="[cyan]MODIFICAR SUCURSAL", style="bold yellow")
        while True:

            try:
                s_id = int(console.input("[bold cyan]Ingrese ID de Sucursal: "))
                if s_id:
                    s_idEnDB = sucursal_controller.buscarSucursalID(s_id)
                    if s_idEnDB:
                        break
                    console.print("[bold red]¡Sucursal no Existe!, Ingrese un ID de Sucursal valido.")
                    if not reintentar():
                        redirect("Volviendo a menu Gestión Sucursales...")
                        self.sucursal_menu()
                
                    # redirect("Volviendo a opcion Eliminar Sucursal...")
                    continue
            except:
                print(Fore.RED + "El ID ingresado no es válido.")
                if not reintentar():
                    redirect("Volviendo a menu Gestión Sucursales...")
                    self.sucursal_menu()
                redirect("Volviendo a opcion Eliminar Sucursal...")
                
        try:
            print(Fore.GREEN + f"Sucursal con ID {s_id} seleccionada!")
            nombre, direccion, fecha_constitucion = self.__sucursal_data.obtenerDatosSucursal()
            sucursal_controller.modificarSucursal(s_id, nombre, direccion, fecha_constitucion)
            print(Fore.GREEN + "¡Sucursal modificada exitosamente!")
            while True:
                confirmacion = console.input("[bold white]¿Desea modificar otra sucursal? [bold yellow](S/N): ").strip().upper()
                if confirmacion == 'S':
                    redirect("Volviendo a opcion Modificar Sucursal...")
                    return self.modificarSucursal()
                elif confirmacion == "N":
                    redirect("Volviendo a menu Gestión Sucursales...")
                    return self.sucursal_menu()
                else:
                    print(MESSAGES["error"])
        except:
            redirect("Volviendo a opcion menu Gestion Sucursal...")
            return self.sucursal_menu()
    
    
    def gestionAsignaciones(self):
        try:
            console = self.console
            system('cls')
            table = Table(title="[cyan]MENU ASIGNACIONES[cyan]", style="bold yellow", box=box.ROUNDED)
            table.add_column("[cyan]Opción[cyan]", style="bold white", justify="center")
            table.add_column("[cyan]Descripción[cyan]", style="bold white", )
            table.add_row("1", "Listar Asignaciones")
            table.add_row("2", "Reasignar Empleado")
            table.add_row("3", "Volver")
            console.print(table)
            
            opcion = int(console.input("[bold white]Digite opción: "))
            if opcion == 1: 
                return self.listarAsignaciones()
                
            elif opcion == 2:
                return self.reasignarEmpleado()
                
            elif opcion == 3:
                if self._perfil_id == 1:
                    self.admin_menu()
                else:
                    self.supervisor_menu()
            else:
                print(MESSAGES["error"])
                system("pause")
                return self.gestionAsignaciones()
        except ValueError:
            print(MESSAGES["error"])
            system("pause")
            return self.gestionAsignaciones()
        
        
    def listarAsignaciones(self):
        try:
            asignaciones_controller = AsignacionesController()
            console = self.console
            datosAsignaciones = asignaciones_controller.listarAsignaciones()
            if not datosAsignaciones:
                print(Fore.RED + "¡No existen asignaciones!")
                system("pause")
                self.gestionAsignaciones()

            system("cls")
            table = Table(title="[cyan]ASIGNACIONES DE EMPLEADOS A SUCURSALES[cyan]", style="bold yellow")
            columnas = ["ID EMPLEADO", "RUT EMPLEADO", "NOMBRES EMPLEADO", "APELLIDOS EMPLEADO", "ID SUCURSAL", "NOMBRE SUCURSAL", "DIRECCION SUCURSAL" ]
    
            for columna in columnas:
                table.add_column("[bold cyan]" + columna + "[bold cyan]", justify="center", style="bold white")
    
            for asignacion in datosAsignaciones:
                table.add_row(str(asignacion[0]), asignacion[1], asignacion[2], asignacion[3], str(asignacion[4]), asignacion[5], asignacion[6])
                table.add_row("")
            console.print(table)
            
            volver = input("Presione una tecla para continuar...")
            redirect("Volviendo a menu Asignaciones...")
            self.gestionAsignaciones()
        except Exception as e:
            print(e)
            
            
    def reasignarEmpleado(self):
        try:
            while True:
                empleado_controller = self.__employee_controller
                sucursal_controller = self.__sucursal_controller
                asignaciones_controller = self.__asignaciones_controller
                system("cls")
                redirect("Mostrando Empleados disponibles para Reasignación...")
                self.list_employees(True, from_assignments=True)
                console = self.console80
                console.rule(title="[cyan]REASIGNAR EMPLEADO", style="bold yellow")
                console.print("[bold white]Ingrese RUT de Empleado y Sucursal a la que desea reasignar")
                rut = self.__person_data.get_rut(console)
                empleado = empleado_controller.buscarEmpleadoPorRut(rut)

                if not empleado:
                    print(Fore.RED + "¡Empleado no existe!, Ingrese un RUT válido.")
                    if not reintentar():
                        redirect("Volviendo a menu Gestion Asignaciones")
                        return self.gestionAsignaciones()
                    continue

                redirect("Mostrando Sucursales disponibles para Reasignación...")
                self.list_sucursals(True)
                
                while True:
                    try:
                        s_id = int(console.input("[bold cyan]Ingrese ID de Sucursal Nueva: "))
                        if s_id:
                            s_idEnDB = sucursal_controller.buscarSucursalID(s_id)
                            if s_idEnDB:
                                break
                            console.print("[bold red]¡Sucursal no existe!, Ingrese un ID de sucursal valido.")
                            if not reintentar():
                                redirect("Volviendo a menu Gestión Asignaciones")
                                return self.gestionAsignaciones()
                    except:
                        print(Fore.RED + "¡ID de Sucursal es necesaria!, Ingresela nuevamente.")
                
                
                try:
                    asignaciones_controller.reasignarEmpleado(rut, s_id, empleado)
                    
                except Exception as e:
                    print(e)
                    if not reintentar():
                        redirect("Volviendo a menu Gestion Asignaciones")
                        return self.gestionAsignaciones()
                    continue
                
                print(Fore.GREEN + "¡Reasignacion Exitosa!")
                while True:
                    confirmacion = console.input("[bold white]¿Desea reasignar a otro Empleado? [bold yellow](S/N): ").strip().upper()
                    if confirmacion == 'S':
                        redirect("Volviendo a opcion Reasignar Empleado...")
                        break
                    elif confirmacion == "N":
                        redirect("Volviendo a menu Gestión Asignaciones...")
                        return self.gestionAsignaciones()
                    else:
                        print(MESSAGES["error"])
                        
                continue
        except Exception as e:
            
            redirect("Volviendo a menu Gestion Asignaciones")
            return self.gestionAsignaciones()
        
        
    def salirPrograma(self):
        console = self.console
        while True:
            confirmacion = console.input("[bold white]¿Esta seguro de salir de sistema? [bold yellow](S/N): ").strip().upper()
            if confirmacion == 'S':
                redirect("Saliendo...")
                console.print("[bold yellow]¡Gracias por usar el sistema!")
                os._exit(0)
            elif confirmacion == "N":
                return self.main_menu()
            else:
                print(MESSAGES["error"])
                system("pause")
            

    def listarBecasAPI(self):
        try:
            console = self.console
            system("cls")
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
            redirect("Volviendo a Menu Administrador...")
            self.admin_menu()
                
        except Exception as e:
            console.print(f"[bold white]Error en la solicitud: [bold red]{e}")
            volver = console.input("[bold white]Presione una tecla para continuar...")
            redirect("Volviendo a Menu Administrador")
            self.admin_menu()
            
            