from cryptography.fernet import Fernet #pip install cryptography para poder usar la libreria
import base64
import os

class hacer_clave:
    uCARPETA = "PROYECTO_01_USERS/"
    nArchivo = "clave.key"
    aCompleto = uCARPETA+nArchivo
    def __init__(self,contrasena):
        self.comtrasena = contrasena
        pass
    # Genera y guarda la clave (solo se ejecuta si no existe)
    def generar_clave():        
        if not os.path.exists(f"{hacer_clave.aCompleto}"):
            clave = Fernet.generate_key()
            with open(f"{hacer_clave.aCompleto}", "wb") as clave_file:
                clave_file.write(clave)

    # cargar clave desde el archivo
    def cargar_clave():
        if not os.path.exists(f"{hacer_clave.aCompleto}"):#Debe tener 32 bytes y estar en base64
            print("Error: No se encontró la clave. Primero genera la clave con 'generar_clave()'.")
            return None
        return open(f"{hacer_clave.aCompleto}", "rb").read()
    
    # def cargar_clave():
    #     return clave # retorna la clave que tiene 2 bytes y estar en base64
#clave = b'XFLleU2plW6hTbOqr4vrQ0xk6jqmZajr9Lm8NMXvh78='# por si deceas ejecutar el codigo sin usar 
                                                        # la funsion de arriba y asi poder descifrar
                                                        # las pass de documento "prueba.csv"