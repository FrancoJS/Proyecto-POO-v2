from database.dao import DAO
from models.Usuario import Usuario
from colorama import Fore, Style, init
from os import system

class UsuarioController:
    def __init__(self):
        self.__dao = DAO()
        
    def buscarUsuario(self, rut:str, clave:str):
        try:
            sql = "SELECT rut, clave, p_id FROM USUARIOS WHERE rut = %s"
            self.__dao.cursor.execute(sql, (rut))
            usuario = self.__dao.cursor.fetchone()
            if not usuario:
                return False
            
            clave_en_DB = usuario[1]
            if not clave == clave_en_DB:
                return False
            
            return usuario[2]
            
        except Exception as e:
            print("Se Falló en la busqueda del Usuario en la Base de Datos")
            