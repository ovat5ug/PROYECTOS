from USER import users
from datetime import datetime  # datetime
# import contrasena

lista_datos=[]
cuantos_datos = int(input("ingrese la cantidad de datos que ingresara: "))

for i in range(cuantos_datos):
    nombre=input("ingrese su nombre: ").title()
    correo=input("ingrese su correo: ")
    import contrasena  # Se importa dentro de la función    
    contrasenha= contrasena.encriptar_clave.encriptar
    tipo_de_usuario="Regular"
    fecha = datetime.now()# Obteniendo Fecha Actual
    fecha_actual = fecha.strftime("%Y-%m-%d")
    hora_actual = fecha.strftime("%H:%M:%S")
    
    tUsuario = users.TypeOfUsers(nombre, correo, contrasena.contrasena_encriptada(), fecha_actual, hora_actual, tipo_de_usuario)
    # print("hola mundo") #TEST
    lista_datos.append([tUsuario.user,tUsuario.email,tUsuario.password, tUsuario.type_of_user,tUsuario.date,tUsuario.hour])

# Para ver los datos de la tabla
# print(f"{lista_datos}")#TEST
