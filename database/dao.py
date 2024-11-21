import pymysql

class DAO:
    
    def __init__(self):
        self.__conectar()
     
    def __conectar(self):
        try:
            self.connection = pymysql.connect(
                host = "localhost",
                user = "root",
                password = "",
                db = "bd_ecotech"
            )

            self.cursor = self.connection.cursor()
            # print("Conexion establecida correctamente")
        except:
            print("Error al conectar a la base de datos")
        
    def desconectar(self):
        self.connection.close()
        # print("Desconectado")
        
