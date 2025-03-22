import login
import crear_archivo
import funciones

# ======= MENÚ =======
if __name__ == "__main__":
    # generar_clave()  # Asegura que haya una clave de cifrado

    while True:
        print("\n📌 MENÚ:")
        print("1️⃣ Iniciar sesión")
        print("2️⃣ Registrar usuario")
        print("3️⃣ Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            login.login()
            funciones.operaciones_aritmeticas()
            break
        elif opcion == "2":
            crear_archivo.docCreado(False)# validar_cuantos_datos introducira el usuario
            print("\n✅ Usuario Registrado...")
            print("👋 Saliendo del sistema...")
            break
        elif opcion == "3":
            print("\n👋 Saliendo del sistema...")
            break
        else:
            print("\n⚠ Opción inválida, intente de nuevo.")

# usuario # Marcos
#  correo # maksmaskmas
#    pass # skmkakskss
#    hash # gAAAAABn21mu_iI1saixEn0SyoWsgjypypzmZTzI3KMyq4jEzYvurMS3NcAdDBysk3fTvxJkE4QTM62DpbcJtL-gHUhZt66JPQ==



    # login_usuario.email
    # login_usuario.password
    # print(login_usuario,login_usuario.password)

    # correo = "maksmaskmas"
    # contraseña = "gAAAAABn21mu_iI1saixEn0SyoWsgjypypzmZTzI3KMyq4jEzYvurMS3NcAdDBysk3fTvxJkE4QTM62DpbcJtL-gHUhZt66JPQ=="
  



        #   opcion = input('''\nSeleccione una opción: 
        #                1️⃣ Registrar usuario
        #                2️⃣ Iniciar sesión
        #                3️⃣ Salir''')
