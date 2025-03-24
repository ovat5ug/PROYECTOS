class Users:
    def __init__(self, email, password):        
        self.email = email
        self.password = password
        # print(f"Usuario creado: {self.email}")  # confirmacion de usuario creado TEST
    
class TypeOfUsers(Users):
    def __init__(self, user, email, password, date, hour, type_of_user="regular"):
        super().__init__(email, password)
        self.user = user
        self.type_of_user = type_of_user
        self.date = date
        self.hour = hour
        # print(f"Soy un usuario de tipo: {self.type_of_user}") # confirmacion de TIPO usuario creado TEST

# holaMundo = TypeOfUsers("carlos", "admin@email.com", "admin123", '2025-03-18', '15:56:30',"administrador")
# holaMundo #TEST