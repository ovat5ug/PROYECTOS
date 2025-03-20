import users

class Login(users.Users):    
    def __init__(self, email, password):
        super().__init__(email, password)    

    def tipoDeAcceso(self, type_of_user="regular"):
        self.type_of_user = type_of_user
        print(f"ha iniciado Sesion: {self.email}")
        return self

# Datos de prueba
nombre, fecha_actual, hora_actual, tipo_de_usuario = "usuario1", '2025-03-18', '15:56:30', 'Regular'
email, password = "marcos@qwerty.com", "qwasdefrg45wqxx-.,,"

# Creando instancia
usuario = users.Users(email, password) 

marcos = Login(usuario.email,usuario.password)
marcos.tipoDeAcceso(tipo_de_usuario)

# if (correo=CVcorreo): VALIDACION
