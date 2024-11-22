from database.dao import DAO
from models.User_model import User
from utils.password_service import hash_password, compare_password

class UserController:
    
    def __init__(self):
        self.__dao = DAO()
    
    
    def register_user(self, rut:str, name:str, paternal_surname:str, maternal_surname:str, phone_number:int, email:str, password:str, perfil_id:int):
        try:
            if self.user_exists(rut, phone_number, email):
                raise Exception("¡Ya existe un Usuario con Rut, Telefono o Correo proporcionados!")
            
            hashed_password = hash_password(password)
            user = User(rut, name, paternal_surname, maternal_surname, phone_number, email, hashed_password, perfil_id)

            sql = "INSERT INTO USUARIOS (RUT, NOMBRES, APE_PATERNO, APE_MATERNO, TELEFONO, CORREO, CLAVE, P_ID) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (user.rut, user.names, user.paternal_surname, user.maternal_surname, user.phone_number, user.email, user.password, user.perfil_id)

            self.__dao.cursor.execute(sql, values)
            self.__dao.connection.commit()

        except Exception as error:
            raise Exception(error)
        
    def user_exists(self, rut:str, phone_number:int, email:str):
        try:
            sql = "SELECT RUT FROM USUARIOS WHERE rut = %s OR telefono = %s OR correo = %s"
            values = (rut, phone_number, email)
            self.__dao.cursor.execute(sql, values)
            user = self.__dao.cursor.fetchone()
            if user:
                return True
            
            return False
        except:
            raise Exception("Error al verificar el usuario")

        
    def validate_credentials(self, rut:str, password:str):
        try:
            sql = "SELECT rut, clave, p_id FROM USUARIOS WHERE rut = %s"
            self.__dao.cursor.execute(sql, (rut,))
            user = self.__dao.cursor.fetchone()
            if not user:
                return False
               
            password_in_db = user[1]
            return user[2] if compare_password(password, password_in_db) else False
                
        except:
            raise Exception("Se Falló en la busqueda del Usuario en la Base de Datos")
            