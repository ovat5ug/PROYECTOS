import csv
import os
import users
import login_users
from PASS_MANAGER import contrasena

# ======= Función para iniciar sesión =======
def login():
    # while True:
        try:
            correo = input("Ingrese su correo: ").strip()
            contraseña=input("Ingrese su contraseña: ")
            usuario=users.Users(correo,contraseña)
            login_usuario = login_users.Login(usuario.email,usuario.password)
            
        # ====================== HACER CAMBIO SI ES NECESRIO ===============================================
            uCarpeta = "PROYECTO_01_USERS/DATA/"
            nArchivo = "prueba" # poner el nombre de tu archivo
            aExtencion = ".csv" # poner la extencion del archivo que sea valida
            # print(f"\\DATA\\{nArchivo}{aExtencion}")
        # ==================================================================================================

            with open(f"{uCarpeta}{nArchivo}{aExtencion}",encoding="utf-8",) as file:
                    encontrado = False  # # Variable para verificar si se encontró el usuario
                    usuario = csv.reader(file)
                    for row in  usuario:
                        # print(row[1],row[2]) # correo y contraseña       
                        # Comparar correo y contraseña
                        if row[1] == login_usuario.email and contrasena.desencriptar_clave.desencriptar(row[2][:]) == login_usuario.password:
                            des=contrasena.desencriptar_clave.desencriptar(row[2][:])
                            print(f"\n✅ Inicio de sesión exitoso.{des}")
                            encontrado=True # Marcamos que el usuario fue encontrado
                            break 
                    if not encontrado:                
                        # des=contrasena.desencriptar_clave.desencriptar(row[2][:])
                        print(f"\n❌ Correo o contraseña incorrectos. {des}")
        except UnboundLocalError as e:   
            print("⚠️ Error: Ingrese un valor válido.")
            print(f"Error: {type(e).__name__}")
            login()     

# login() #TEST
# usuario # Marcos
#  correo # antonio22@gmail.com.org
#    pass # skmkakskss
#    hash # gAAAAABn21mu_iI1saixEn0SyoWsgjypypzmZTzI3KMyq4jEzYvurMS3NcAdDBysk3fTvxJkE4QTM62DpbcJtL-gHUhZt66JPQ==
# FALTA HACER UN MANEJO DE ERRORES