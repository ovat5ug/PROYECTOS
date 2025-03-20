import users
import login_users

# Datos de prueba
nombre, fecha_actual, hora_actual, tipo_de_usuario = "usuario1", '2025-03-18', '15:56:30', 'Regular'
email, password = input("Ingrese su correo "), input("Ingrese si contraseña: ")

# Creando instancia
usuario = users.Users(email, password) 

login = login_users.Login(usuario.email,usuario.password)
login.tipoDeAcceso(tipo_de_usuario)

# print(marcos)  # Para ver la representación del objeto

# if (correo=CVcorreo): VALIDACION