from datetime import datetime  # datetime
from USER import users
from PASS_MANAGER import contrasena

def registrar(validar_cuantos_datos=True):
    while True:
                try:    
                    lista_datos=[]
                    if validar_cuantos_datos:
                        cuantos_datos = int(input("ingrese la cantidad de datos que ingresara: "))
                    else:
                        cuantos_datos = 1  # Solo se registrara un solo usuario por login 
                    for i in range(cuantos_datos):
                        nombre=input("ingrese su nombre: ").title()
                        correo=input("ingrese su correo: ")
                        c_encriptada= contrasena.contrasena_encriptada()
                        tipo_de_usuario="Regular"
                        fecha = datetime.now()# Obteniendo Fecha Actual
                        fecha_actual = fecha.strftime("%Y-%m-%d")
                        hora_actual = fecha.strftime("%H:%M:%S")    
                        # sUsuario=users.Users(correo,contrasena.contrasena_encriptada())
                        tUsuario = users.TypeOfUsers(nombre, correo, c_encriptada, fecha_actual, hora_actual, tipo_de_usuario)
                        # print("hola mundo") #TEST
                        lista_datos.append([tUsuario.user,tUsuario.email,tUsuario.password, tUsuario.type_of_user,tUsuario.date,tUsuario.hour])
                    return lista_datos,contrasena.desencriptar_clave.desencriptar(c_encriptada)
                except ValueError as e:   
                    print("⚠️ Error: Ingrese un número válido.")
                    print(f"Error: {type(e).__name__}")      

# func_registrar = registrar()

# c_desencriptada = func_registrar[1] #Retorna la contraseña
# print(f"esta es la contraseña: {c_desencriptada}")# TEST

# lista_datos# = ["Usuario", "Email", "Password", "Tipo_de_Usuario","Fecha","Hora"] 
# lista_datos = func_registrar[0]# Retorna la primera lista de la tupla
# lista_datos1 = func_registrar[0][0][:]
# lista_datos2 = ["Email", "Password", "Fecha","Hora"] 
# lista_datos2 = lista_datos4[1],lista_datos4[2],lista_datos4[4],lista_datos4[5]           
# print(f"esta es la lista de datos: \n{lista_datos}")# TEST
# print(f"esta es la lista de datos1: \n{lista_datos2}")# TEST
# print(f"esta es la lista de focalizada: \n{lista_datos3}")# TEST
# # print()