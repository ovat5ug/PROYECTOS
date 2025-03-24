from cryptography.fernet import Fernet #pip install cryptography para poder usar la libreria
from contrasena_encriptacion_y_desencriptacion import encriptar_clave as encriptar_clave
from contrasena_encriptacion_y_desencriptacion import desencriptar_clave as desencriptar_clave
import base64
import os

def contrasena_encriptada():
    introduce_contra=input("Introduce tu contraseña: ")
    contrasena_cifrada = encriptar_clave.encriptar(introduce_contra)
    print(f"Contraseña encriptada: {contrasena_cifrada}")
    # return print(contrasena_cifrada) # TEST
    return contrasena_cifrada

def contrasena_desencriptada():
    introduce_hash = input("Introduce tu hash: ")
    contrasena_descifrada = desencriptar_clave.desencriptar(introduce_hash)
    print(f"Contraseña desencriptada: {contrasena_descifrada}")
    # return print(contrasena_descifrada) # TEST
    return contrasena_descifrada

# cifrada=contrasena_encriptada() # TEST
# desifrada=contrasena_desencriptada() #TEST

# gAAAAABn20gMX6QrSqb_OGG6y7MCIcyPt-a-K6duQ5MGIxxINKLnMn-eX23DKvMksuLPJggo9tH-AVol1S9s6E0Ktz8heukc1w==
# gAAAAABn20giGMRtOS9awW555m78pQniWs19HQLIOEI8sXsDWKaUDCfzhCuxmNvGl_iHus7TOjb4pCH2yTh-zMZPjQ9zhYRT9Q==
# gAAAAABn20tlQw-J7x5vvCAU-N2os9qTTL7q_yI2zD7g9wOUEeeri-qlIzD3LUTxrjQyTPMPTt7h7OUAiH-6_ELhjpUptTXrzg==
# gAAAAABn3ICK6jWPFeVK-OBU7hfX55NHDTXfoo5bufP7Rn5Pnj6tyLxF32GWd2BBbTsGtHYe1ctslzBagKPGXL2IwFDGCF6-Hg==
# gAAAAABn3Ie8B4rmNpG2WjhdKnMhw0ibz3tSnJYj4mzS60wva1X9HTjq_mEN23u4kpmp7-zyWgUeFbyo0sD_FReIAYL8HMBxLA==
# gAAAAABn3I31pEeLiSPXhlxJqyZL6pPwmQ11pAyo2CqH3Ps69Uno3SNW5MWdKMwX7LLIWC4ruT3x2RmmB3y6L_NmWbEZa4Lxsg==

# Llamando a las funciones para capturar los datos
# contrasena_cifrada = contrasena_encriptada()
# contrasena_descifrada = contrasena_desencriptada()