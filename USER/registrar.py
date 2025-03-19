import users
from datetime import datetime  # datetime

lista_datos=[]
cuantos_datos = int(input("ingrese la cantidad de datos que ingresara: "))

for i in range(cuantos_datos):
    nombre=input("ingrese su nombre: ").title()
    correo=input("ingrese su correo: ")
    contrasenha=input("ingrese su contraseña: ")
    tipo_de_usuario="Regular"
    fecha = datetime.now()# Obteniendo Fecha Actual
    fecha_actual = fecha.strftime("%Y-%m-%d")
    hora_actual = fecha.strftime("%H:%M:%S")
    
    # usuario = Users("usuario1", "usuario1@email.com", "contraseña123",'2025-03-18', '15:56:30','Regular')
    tUsuario = users.TypeOfUsers(nombre, correo, contrasenha, fecha_actual, hora_actual, tipo_de_usuario)
    # print("hola mundo") #TEST
    lista_datos.append([tUsuario.user,tUsuario.email,tUsuario.password, tUsuario.type_of_user,tUsuario.date,tUsuario.hour])

# Para ver los datos de la tabla
# print(f"{lista_datos}")#TEST