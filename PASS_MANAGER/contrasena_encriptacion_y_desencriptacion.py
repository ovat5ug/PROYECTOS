from cryptography.fernet import Fernet #pip install cryptography para poder usar la libreria
from contrasena_configuracion_de_clave import hacer_clave as hacer_clave
import base64
import os

class encriptar_clave(hacer_clave):
    def __init__(self, contrasena):
        super().__init__(contrasena)
    # Encriptar contraseña
    def encriptar(contrasena):
        clave = hacer_clave.cargar_clave()
        if clave:
            cipher_suite = Fernet(clave)
            return cipher_suite.encrypt(str(contrasena).encode()).decode()  # Retorna string en lugar de bytes
        return None
    
class desencriptar_clave(hacer_clave):
    def __init__(self, contrasena):
        super().__init__(contrasena)
    # Desencriptar contraseña
    def desencriptar(contrasena_encriptada):
        clave = hacer_clave.cargar_clave()
        if clave:
            cipher_suite = Fernet(clave)
            return cipher_suite.decrypt(str(contrasena_encriptada).encode()).decode()  # Convertimos string a bytes antes de descifrar
        return None