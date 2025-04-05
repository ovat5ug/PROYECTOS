import login
import crear_archivo
import FUNCIONES_COMUNES.calculos_aritmeticos as calculos_aritmeticos

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
            calculos_aritmeticos.operaciones_aritmeticas()
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

# usuario # Marcos
#  correo # antonio22@gmail.com.org
#    pass # skmkakskss
#    hash # gAAAAABn21mu_iI1saixEn0SyoWsgjypypzmZTzI3KMyq4jEzYvurMS3NcAdDBysk3fTvxJkE4QTM62DpbcJtL-gHUhZt66JPQ==
