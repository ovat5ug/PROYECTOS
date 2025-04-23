import security.contrasena_encriptacion_y_desencriptacion as c1

def contrasena_encriptada(introduce_contra):
    # introduce_contra=input("Introduce tu contraseña: ")
    contrasena_cifrada = c1.encriptar_clave.encriptar(introduce_contra)
    # print(f"Contraseña encriptada: {contrasena_cifrada}")
    return contrasena_cifrada

def contrasena_desencriptada(introduce_hash):
    # introduce_hash = input("Introduce tu hash: ")
    contrasena_descifrada = c1.desencriptar_clave.desencriptar(introduce_hash)
    # print(f"Contraseña desencriptada: {contrasena_descifrada}")
    return contrasena_descifrada