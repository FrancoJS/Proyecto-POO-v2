from database.dao import DAO
from models.Usuario import Usuario
from colorama import Fore, Style, init
from os import system

class UsuarioController:
    
    def __init__(self):
        self.__dao = DAO()
    
    
    def registroUsuarios(self, rut: str, nombres: str, ape_paterno: str, ape_materno: str, telefono: int, correo: str, clave: str, p_id: int):
        try:
            if self.buscarUsuario(rut):
                print(Fore.RED + f"¡El RUT '{rut}' ya está registrado en el sistema!")
                return
            usuario = Usuario(rut, nombres, ape_paterno, ape_materno, telefono, correo, clave, p_id)

            sql = "INSERT INTO USUARIOS (RUT, NOMBRES, APE_PATERNO, APE_MATERNO, TELEFONO, CORREO, CLAVE, p_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (usuario.rut, usuario.nombres, usuario.ape_paterno, usuario.ape_materno, usuario.telefono, usuario.correo, usuario.clave, usuario.p_id)

            self.__dao.cursor.execute(sql, values)
            self.__dao.connection.commit()
            print(Fore.GREEN + "¡Usuario creado exitosamente!")

        except Exception as e:
            print(Fore.RED + f"Error al registrar usuario: {e}")
            raise

        
    def buscarUsuario(self, rut:str, clave:str = None) -> bool:
        try:
            sql = "SELECT rut, clave, p_id FROM USUARIOS WHERE rut = %s"
            self.__dao.cursor.execute(sql, (rut,))
            usuario = self.__dao.cursor.fetchone()
            if not usuario:
                return False
            
            if clave:    
                clave_en_DB = usuario[1]
                if not clave == clave_en_DB:
                    return False

            return usuario[2] if clave else True
            
        except Exception as e:
            print("Se Falló en la busqueda del Usuario en la Base de Datos")
            return False