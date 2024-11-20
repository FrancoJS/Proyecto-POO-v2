from database.dao import DAO
from models.Usuario import Usuario
from colorama import Fore, Style, init
from os import system
from utils.password_service import hashPassword, comparePassword

class UsuarioController:
    
    def __init__(self):
        self.__dao = DAO()
    
    
    def registroUsuarios(self, rut:str, nombres:str, ape_paterno:str, ape_materno:str, telefono:int, correo:str, clave:str, p_id:int):
        try:
            if self.__usuarioExiste(rut, telefono, correo):
                raise Exception(f"¡Ya existe un Usuario con Rut, Telefono o Correo proporcionados!")
            
            clave_hashed = hashPassword(clave)
            usuario = Usuario(rut, nombres, ape_paterno, ape_materno, telefono, correo, clave_hashed, p_id)

            sql = "INSERT INTO USUARIOS (RUT, NOMBRES, APE_PATERNO, APE_MATERNO, TELEFONO, CORREO, CLAVE, P_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (usuario.rut, usuario.nombres, usuario.ape_paterno, usuario.ape_materno, usuario.telefono, usuario.correo, usuario.clave, usuario.p_id)

            self.__dao.cursor.execute(sql, values)
            self.__dao.connection.commit()

        except Exception as e:
            raise Exception(e)
        
    def __usuarioExiste(self, rut:str, telefono:int, correo:str):
        try:
            sql = "SELECT RUT FROM USUARIOS WHERE rut = %s OR telefono = %s OR correo = %s"
            values = (rut, telefono, correo)
            self.__dao.cursor.execute(sql, values)
            usuario = self.__dao.cursor.fetchone()
            if usuario:
                return True
            
            return False
        except:
            raise Exception(f"Error al verificar el usuario")

        
    def validarCredenciales(self, rut:str, clave:str) -> bool:
        try:
            sql = "SELECT rut, clave, p_id FROM USUARIOS WHERE rut = %s"
            self.__dao.cursor.execute(sql, (rut,))
            usuario = self.__dao.cursor.fetchone()
            if not usuario:
                return False
            
            if clave:    
                clave_en_DB = usuario[1]
                if not comparePassword(clave, clave_en_DB):
                    return False

            return usuario[2] if clave else True
            
        except Exception as e:
            print(e)
            raise Exception("Se Falló en la busqueda del Usuario en la Base de Datos")
            