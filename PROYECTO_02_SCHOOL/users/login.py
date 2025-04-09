import csv
import os
import users.users as users
import users.login_users as login_users
import security.contrasena_encriptacion_y_desencriptacion as contrasena
import roots.rutinhas as r2
# ======= Función para iniciar sesión =======
def validar_login():
    # while True:
        try:
            correo = input("Ingrese su correo: ").strip()
            contraseña=input("Ingrese su contraseña: ")
            usuario= users.Users(correo,contraseña)
            login_usuario = login_users.Login(usuario.email,usuario.password)
            
        # ====================== HACER CAMBIO SI ES NECESRIO ===============================================
            uCarpeta = r2.rc.uCARPETA
            archivo = r2.ac.archivo
        # ==================================================================================================

            with open(f"{uCarpeta}/{archivo}",encoding="utf-8",) as file:
                    encontrado = False  # # Variable para verificar si se encontró el usuario
                    usuario = csv.reader(file)
                    for row in  usuario:
                        # print(sow[0],row[1],row[2]) # nombre, correo y contraseña       
                        # Comparar correo y contraseña
                        if row[1] == login_usuario.email and contrasena.desencriptar_clave.desencriptar(row[2][:]) == login_usuario.password:
                            desen=contrasena.desencriptar_clave.desencriptar(row[2][:])
                            print(f"\n✅ {row[0]} has hecho inicio de sesión exitoso con: {login_usuario.email}")
                            encontrado=True # Marcamos que el usuario fue encontrado
                            break 
                    if not encontrado:                
                        # des=contrasena.desencriptar_clave.desencriptar(row[2][:])
                        print(f"\n❌ Correo o contraseña incorrectos. {desen}")
        except UnboundLocalError as e:   
            print("⚠️ Error: Ingrese un valor válido.")
            print(f"Error: {type(e).__name__}")
            validar_login()     