class Users:
    def __init__(self, user, email, password):
        self.user = user
        self.email = email
        self.password = password
        print(f"Usuario creado: {self.user}")  # Si realmente necesitas imprimir algo
    
class TypeOfUsers(Users):
    def __init__(self, user, email, password, date, hour, type_of_user="regular"):
        super().__init__(user, email, password)
        self.type_of_user = type_of_user
        self.date = date
        self.hour = hour
        print(f"Soy un usuario de tipo: {self.type_of_user}")

# holaMundo = TypeOfUsers("carlos", "admin@email.com", "admin123", '2025-03-18', '15:56:30',"administrador")
# holaMundo #TEST