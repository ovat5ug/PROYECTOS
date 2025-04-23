from cryptography.fernet import Fernet
from security import contrasena_configuracion_de_clave as c2

class encriptar_clave(c2.hacer_clave):
    def __init__(self, contrasena):
        super().__init__(contrasena)
    # Encriptar contraseña
    def encriptar(contrasena):
        clave = c2.hacer_clave.cargar_clave()
        if clave:
            cipher_suite = Fernet(clave)
            enc=cipher_suite.encrypt((contrasena).encode()).decode()
            return enc  # Retorna string en lugar de bytes
        return None
    
class desencriptar_clave(c2.hacer_clave):
    def __init__(self, contrasena):
        super().__init__(contrasena)
    # Desencriptar contraseña
    def desencriptar(contrasena_encriptada):
        clave = c2.hacer_clave.cargar_clave()
        if clave:
            cipher_suite = Fernet(clave)
            return cipher_suite.decrypt((contrasena_encriptada).encode()).decode()  # Convertimos string a bytes antes de descifrar
        return None