import users.login as validar_login
import data_analytics.crear_archivo as crear_archivo

def login():
    # ======= MENÚ =======
    if (__name__ == "__main__" or __name__ != True): # o solo poner True como condicion
        print("👋 Bienvenido al sistema de gestión de usuarios")
        # generar_clave()  # Asegura que haya una clave de cifrado

        while True:
            print("\n📌 MENÚ:")
            print("1️⃣ Iniciar sesión")
            print("2️⃣ Registrar usuario")
            print("3️⃣ Salir")
            
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                validar_login.validar_login()
                # calculos_aritmeticos.operaciones_aritmeticas()
                break
            elif opcion == "2":
                crear_archivo.docCreado(False)# valida_cuantos_datos introducira el usuario
                print("\n✅ Usuario Registrado...")
                print("👋 Saliendo del sistema...")
                break
            elif opcion == "3":
                print("\n👋 Saliendo del sistema...")
                break
            else:
                print("\n⚠ Opción inválida, intente de nuevo.")