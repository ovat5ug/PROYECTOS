from cryptography.fernet import Fernet
import security.contrasena_encriptacion_y_desencriptacion as c1
import base64
import os

def contrasena_encriptada():
    introduce_contra=input("Introduce tu contraseña: ")
    contrasena_cifrada = c1.encriptar_clave.encriptar(introduce_contra)
    print(f"Contraseña encriptada: {contrasena_cifrada}")
    # return print(contrasena_cifrada) # TEST
    return contrasena_cifrada

def contrasena_desencriptada():
    introduce_hash = input("Introduce tu hash: ")
    contrasena_descifrada = c1.desencriptar_clave.desencriptar(introduce_hash)
    print(f"Contraseña desencriptada: {contrasena_descifrada}")
    # return print(contrasena_descifrada) # TEST
    return contrasena_descifrada