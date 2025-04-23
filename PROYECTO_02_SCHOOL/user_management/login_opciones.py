import user_management.login as validar_login
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
                print("\n📌 MENÚ:")                
                print("1️⃣ Registrar empleado")
                print("2️⃣ Registrar estudiante")
                print("3️⃣ Registrar padre de familia")
                opcion = input("\nSeleccione una opción: ").lower()
                if opcion == "1" or opcion == "empleado":
                    # Llama a la función para registrar empleado
                    crear_archivo.docCreado("empleado")
                elif opcion == "2" or opcion == "estudiante":
                    # Llama a la función para registrar estudiante
                    crear_archivo.docCreado("estudiante")
                elif opcion == "3" or opcion == "padres":
                    # Llama a la función para registrar padre de familia
                    crear_archivo.docCreado("padres")
                else:
                    print("⚠ Opción inválida, intente de nuevo.")
                    login()
                crear_archivo.docCreado(False)# valida_cuantos_datos introducira el usuario
                print("\n✅ Usuario Registrado...")
                print("👋 Saliendo del sistema...")
                break
            elif opcion == "3":
                print("\n👋 Saliendo del sistema...")
                break
            else:
                print("\n⚠ Opción inválida, intente de nuevo.")