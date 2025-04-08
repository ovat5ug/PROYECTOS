from cryptography.fernet import Fernet
import base64
import os
import roots.rutinhas as r1

class hacer_clave:
    uCARPETA = r1.rh.uCARPETA 
    nArchivo = r1.rh.nArchivo
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