import user_management.login as validar_login
import user_management.login_opciones_multiples as lm
# import data_analytics.crear_archivo as crear_archivo

def login():
    # ======= MENÚ =======
    if (__name__ == "__main__" or __name__ != True): # o solo poner True como condicion
        print("👋 Bienvenido al sistema de gestión de usuarios")
        while True:
            print("\n📌 MENÚ:")
            print("1️⃣  Iniciar sesión")
            print("2️⃣  Acciones Persona")
            print("3️⃣  Acciones Empleado")
            print("4️⃣  Acciones Estudiantes")
            print("5️⃣  Acciones Padres de Familia")
            print("6️⃣  Salir")

            
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                validar_login.validar_login()
                # calculos_aritmeticos.operaciones_aritmeticas()
                break
            elif opcion == "2":
                print("\n📌 MENÚ:")
                lm.opciones_multiples('persona')
                # crear_archivo.docCreado(False)# valida_cuantos_datos introducira el usuario
                print("\n✅ Usuario Validado...")
                print("👋 Saliendo del sistema...")
                break
            elif opcion == "3":
                print("\n📌 MENÚ:")
                lm.opciones_multiples('empleado')
                # crear_archivo.docCreado(False)# valida_cuantos_datos introducira el usuario
                print("\n✅ Usuario Validado...")
                print("👋 Saliendo del sistema...")
                break
            elif opcion == "4":
                print("\n📌 MENÚ:")
                lm.opciones_multiples('estudiante')
                # crear_archivo.docCreado(False)# valida_cuantos_datos introducira el usuario
                print("\n✅ Usuario Validado...")
                print("👋 Saliendo del sistema...")
                break
            elif opcion == "5":
                print("\n📌 MENÚ:")
                lm.opciones_multiples('padres')
                # crear_archivo.docCreado(False)# valida_cuantos_datos introducira el usuario
                print("\n✅ Usuario Validado...")
                print("👋 Saliendo del sistema...")
                break
            elif opcion == "6":
                print("👋 Saliendo del sistema...")
                break
            else:
                print("\n⚠ Opción inválida, intente de nuevo.")