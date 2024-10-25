from database.dao import DAO
from models.Usuario import Usuario
#from models.Sucursal import Sucursal
from colorama import Fore, Style, init
#from sucursal_controller import SucursalController
from os import system

class UsuarioController:
    def __init__(self):
        self.__dao = DAO()
        
    def buscarUsuario(self, rut, telefono, correo):
        try:
              sql = "SELECT * FROM USUARIOS WHERE rut = %s or telefono = %s or correo = %s"
              value = (rut, telefono, correo)
              self.__dao.execute(sql, value)
              usuario = self.__dao.cursor.fetchone()
              return usuario
        except:
            print("Se Falló en la busqueda del Usuario en la Base de Datos")
            #system("pause")
            
   
   # Inicio de Sesión por REVISAR
   
    def __iniciarSesion(self):
        while True:
            try:
                system("cls")
                print("--- Menu Inicio de Sesión ---", end="\n\n")
                rut = input("Digite su RUT : ")
                if len(rut.strip()) <= 0 and len(rut.strip()) > 12:
                    print("\n--- Debe ingresar un rut con un N° de Carácteres Permitido!!! ---", end="\n\n")
                    system("pause")
                    self.menuMesaAyuda()  
                else:
                    break
            except:
                print("\n--- Error en capturar carácteres validos del RUT ---", end="\n\n")
                system("pause")
                self.menuMesaAyuda()
            
        while True:
            try:
                system("cls")
                con = input("Digite la Contraseña : ")
                if len(con.strip()) <= 0 or len(con.strip()) > 30:
                    print("\n--- Debe digitar una contraseña de entre 1 y 30 Carácteres!!! ---", end="\n\n")
                    system("pause")
                    self.menuMesaAyuda()
                else:
                    break
            except:
                print("\n--- Error en Capturar la Contraseña!!! ---", end="\n\n")
                system("pause")
                self.menuMesaAyuda()
        
        try:
            pass
        except:
            pass
        

        
            
                    