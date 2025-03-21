from datetime import datetime  # datetime
from USER import users
from USER import contrasena

def registrar():
    lista_datos=[]
    cuantos_datos = int(input("ingrese la cantidad de datos que ingresara: "))
    for i in range(cuantos_datos):
        nombre=input("ingrese su nombre: ").title()
        correo=input("ingrese su correo: ")
        c_encriptada= contrasena.contrasena_encriptada()
        tipo_de_usuario="Regular"
        fecha = datetime.now()# Obteniendo Fecha Actual
        fecha_actual = fecha.strftime("%Y-%m-%d")
        hora_actual = fecha.strftime("%H:%M:%S")    
        tUsuario = users.TypeOfUsers(nombre, correo, c_encriptada, fecha_actual, hora_actual, tipo_de_usuario)
        lista_datos.append([tUsuario.user,tUsuario.email,tUsuario.password, tUsuario.type_of_user,tUsuario.date,tUsuario.hour])
    return lista_datos,contrasena.desencriptar_clave.desencriptar(c_encriptada) 

# func_registrar = registrar()
# lista_datos = func_registrar[0]# Retorna la primera lista de la tupla
# c_desencriptada = func_registrar[1] #Retorna la contraseña

# print(f"esta es la lista de datos: \n{lista_datos}")# TEST
# print()
# print(f"esta es la contraseña: {c_desencriptada}")# TEST