import users.users as users

class Login(users.Users):    
    def __init__(self, email, password):
        super().__init__(email, password)    

    def tipoDeAcceso(self, type_of_user="regular"):
        self.type_of_user = type_of_user
        print(f"ha iniciado Sesion: {self.email}")
        return self