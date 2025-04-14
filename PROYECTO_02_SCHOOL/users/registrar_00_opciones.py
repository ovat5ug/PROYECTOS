import users.registrar_01_persona as registrar_persona
import users.registrar_02_empleado as registrar_empleado
import users.registrar_03_padres_estudiantes as registrar_padre_familia
import users.registrar_04_estudiante as registrar_estudiante

if __name__ == "__main__" or __name__ == "users.registrar_00_opciones":
    while True:
        print("\n📌 MENÚ:")
        print("1️⃣ Registrar Persona")
        print("2️⃣ Registrar Empleado")
        print("3️⃣ Registrar Padre de Familia")
        print("4️⃣ Registrar Estudiante")
        print("5️⃣ Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\n👤 Registrar Persona")
            print("===================================")
            registrar_persona.registrar_persona(False)  # un solo registro usando "false"
            break
        elif opcion == "2":
            print("\n👔 Registrar Empleado")
            print("===================================")
            registrar_empleado.registrar_empleado(False)
            break
        elif opcion == "3":
            print("\n👪 Registrar Padre de Familia")
            print("===================================")
            registrar_padre_familia.registrar_padres_estudiantes(False)
            break
        elif opcion == "4":
            print("\n👩‍🎓 Registrar Estudiante")
            print("===================================")
            registrar_estudiante.registrar_estudiante(False)
            break
        elif opcion == "5":
            print("\n👋 Saliendo del sistema...")
            break
        else:
            print("\n⚠ Opción inválida, intente de nuevo.")
        