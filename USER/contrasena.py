from cryptography.fernet import Fernet #pip install cryptography para poder usar la libreria

import base64
import os

class hacer_clave:
    def __init__(self,contrasena):
        self.comtrasena = contrasena
        pass
    # Genera y guarda la clave (solo se ejecuta si no existe)
    def generar_clave():
        if not os.path.exists("clave.key"):
            clave = Fernet.generate_key()
            with open("clave.key", "wb") as clave_file:
                clave_file.write(clave)

    # cargar clave desde el archivo
    def cargar_clave():
        if not os.path.exists("clave.key"):
            print("Error: No se encontró la clave. Primero genera la clave con 'generar_clave()'.")
            return None
        return open("clave.key", "rb").read()
    
class encriptar_clave(hacer_clave):
    def __init__(self, contrasena):
        super().__init__(contrasena)
    # Encriptar contraseña
    def encriptar(contrasena):
        clave = hacer_clave.cargar_clave()
        if clave:
            cipher_suite = Fernet(clave)
            return cipher_suite.encrypt(contrasena.encode()).decode()  # Retorna string en lugar de bytes
        return None
    
class desencriptar_clave(hacer_clave):
    def __init__(self, contrasena):
        super().__init__(contrasena)
    # Desencriptar contraseña
    def desencriptar(contrasena_encriptada):
        clave = hacer_clave.cargar_clave()
        if clave:
            cipher_suite = Fernet(clave)
            return cipher_suite.decrypt(contrasena_encriptada.encode()).decode()  # Convertimos string a bytes antes de descifrar
        return None

introduce_contra=input("Introduce tu contraseña: ")

def contrasena_encriptada():
    contrasena_cifrada = encriptar_clave.encriptar(introduce_contra)
    print(f"Contraseña encriptada: {contrasena_cifrada}")
    # return print(contrasena_descifrada) # TEST
    return contrasena_cifrada

def contrasena_desencriptada():
    contrasena_descifrada = desencriptar_clave.desencriptar(introduce_contra)
    print(f"Contraseña desencriptada: {contrasena_descifrada}")
    # return print(contrasena_descifrada) # TEST
    return contrasena_descifrada
