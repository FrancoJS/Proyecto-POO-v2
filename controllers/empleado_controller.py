from models.Empleado import Empleado
from database.dao import DAO
from datetime import date
from colorama import Fore, Style, init
from .sucursal_controller import SucursalController
init(autoreset=True)

class EmpleadoController:
    
    def __init__(self):
        self.__dao = DAO()


    def crearEmpleado(self, rut:str, nombres:str, ape_paterno:str, ape_materno:str, telefono:int, correo:str, experiencia:int, inicio_contrato:date, salario:int, s_id:int):
        try:
            self.__dao.conectar()
            empleadoEnDB = self.buscarEmpleado(rut, telefono, correo)
            if empleadoEnDB:
                raise Exception(Fore.RED + "¡Empleado ya se encuentra registrado con Rut, Telefono o Correo!")

            empleado = Empleado(rut, nombres, ape_paterno, ape_materno, telefono, correo, experiencia, inicio_contrato, salario, s_id)
            sql = "INSERT INTO EMPLEADOS (RUT, NOMBRES, APE_PATERNO, APE_MATERNO, TELEFONO, CORREO, EXPERIENCIA, INICIO_CON, SALARIO, S_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (empleado.rut, empleado.nombres, empleado.ape_paterno, empleado.ape_materno, empleado.telefono, empleado.correo, empleado.experiencia, empleado.inicio_contrato, empleado.salario, empleado.s_id)
            self.__dao.cursor.execute(sql, values)
            self.__dao.connection.commit()
        except Exception as e:
            raise Exception(e)
        finally:
            self.__dao.desconectar()


    def listarEmpleados(self):
        try:
            self.__dao.conectar()
            sql = "SELECT * FROM EMPLEADOS where es_id = 1"
            self.__dao.cursor.execute(sql)
            result = self.__dao.cursor.fetchall()
            return result
        except:  
            print(Fore.RED + "Ocurrió un error al buscar los datos")
        finally:
            self.__dao.desconectar()
        
            
    def buscarEmpleado(self, rut:str, telefono:int, correo:str):
        try:
            self.__dao.conectar()
            sql = "SELECT * FROM EMPLEADOS WHERE rut = %s or telefono = %s or correo = %s"
            values = (rut, telefono, correo)
            self.__dao.cursor.execute(sql, values)
            empleado = self.__dao.cursor.fetchone()
            return empleado
        except:
            print("Error al buscar empleado")
        finally:
            self.__dao.desconectar()
          
            
    def buscarEmpleadoModificar(self, rut:str, telefono:int, correo:str, e_id:int):
        try:
            self.__dao.conectar()
            sql = "SELECT * FROM EMPLEADOS WHERE (rut = %s or telefono = %s or correo = %s) and e_id != %s and es_id = 1"
            values = (rut, telefono, correo, e_id)
            self.__dao.cursor.execute(sql, values)
            empleado = self.__dao.cursor.fetchone()
            return empleado
        except:
            print("Error al buscar empleado")
        finally:
            self.__dao.desconectar()
            
            
    def buscarEmpleadoPorSucursal(self, s_id:int):
        try:
            self.__dao.conectar()
            sql = "SELECT E_ID, RUT, NOMBRES, CONCAT(APE_PATERNO, ' ', APE_MATERNO), TELEFONO, CORREO, S_ID FROM EMPLEADOS WHERE s_id = %s and es_id = 1"
            value = (s_id)
            self.__dao.cursor.execute(sql, (s_id))
            empleado = self.__dao.cursor.fetchall()
            return empleado
        except:
            print("Error al buscar empleado")
        finally:
            self.__dao.desconectar()
            
            
    def buscarEmpleadoPorRut(self, rut:str):
        try:
            self.__dao.conectar()
            sql = "SELECT RUT, S_ID FROM EMPLEADOS WHERE rut = %s and es_id = 1"
            self.__dao.cursor.execute(sql, (rut))
            empleado = self.__dao.cursor.fetchone()
            return empleado
        except:
            print("Error al buscar empleado")
        finally:
            self.__dao.desconectar()


    def eliminarEmpleado(self, rut:str):
        try:
            self.__dao.conectar()
            sql = "UPDATE EMPLEADOS SET es_id = 2 WHERE rut = %s" #%s = dato dinamico   
            self.__dao.cursor.execute(sql, (rut))
            self.__dao.connection.commit()
        except:
            raise Exception("Error al eliminar empleado")
        finally:
            self.__dao.desconectar()
        
            
    def eliminarEmpleadoPorSucursal(self, s_id:int):
        try:
            self.__dao.conectar()
            empleado = self.buscarEmpleadoPorSucursal(s_id)
            if not empleado:
                raise Exception(Fore.RED + "¡EMPLEADO NO EXISTE!")
                
            sql = "UPDATE EMPLEADOS SET es_id = 2 WHERE s_id = %s" #%s = dato dinamico   
            self.__dao.cursor.execute(sql, (s_id))
            self.__dao.connection.commit()
        except Exception as e:
            raise Exception(e)
        finally:
            self.__dao.desconectar()
            
    
    def modificarEmpleado(self, e_id: int, rut: str, nombres: str, ape_paterno: str, ape_materno: str,
                          telefono: int, correo: str, experiencia: int, inicio_con, salario:int):
        try:
            self.__dao.conectar()
            empleado = self.buscarEmpleadoModificar(rut, telefono, correo, e_id)
            
            if empleado:
                raise Exception(Fore.RED + "¡Ya existen Empleados registrados con el Rut, Telefono o Correo proporcionados!")
                
            sql = "UPDATE EMPLEADOS SET RUT = %s, NOMBRES = %s, APE_PATERNO = %s, APE_MATERNO = %s, TELEFONO = %s, CORREO = %s, EXPERIENCIA = %s, INICIO_CON = %s, SALARIO = %s WHERE e_id = %s and es_id = 1"
            values = (rut, nombres, ape_paterno, ape_materno, telefono, correo, experiencia, inicio_con, salario, e_id)
            self.__dao.cursor.execute(sql,values)
            self.__dao.connection.commit()
        except Exception as e:
            raise Exception(e)
        finally:
            self.__dao.desconectar()  
        
            
    def verificarE_ID(self, e_id:int):
        try:
            self.__dao.conectar()
            sql = "SELECT COUNT(*) FROM EMPLEADOS WHERE E_ID = %s AND es_id = 1"
            self.__dao.cursor.execute(sql, (e_id,))
            resultado = self.__dao.cursor.fetchone() #devuelve el valor de la tupla a resultado
            if resultado[0] > 0:
                return True
        except Exception as e:
            print(f"Error al verificar el ID del Empleado : {e}")
            return False
        finally:
            self.__dao.desconectar()