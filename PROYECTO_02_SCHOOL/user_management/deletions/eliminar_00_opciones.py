from .eliminar_01_persona import eliminar_persona
from .eliminar_02_empleado import eliminar_empleado
from .eliminar_03_estudiante import eliminar_estudiante
from .eliminar_04_padres_estudiantes import eliminar_padres_estudiantes
def eliminar_opciones():
    if __name__ == "__main__" or __name__ != True:
        while True:
            print("\n📌 MENÚ:")
            print("1️⃣ Eliminar Persona")
            print("2️⃣ Eliminar Empleado")
            print("3️⃣ Eliminar Padre de Familia")
            print("4️⃣ Eliminar Estudiante")
            print("5️⃣ Salir")
            
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                print("\n👤 Eliminar Persona")
                print("===================================")
                eliminar_persona(False)  # un solo registro usando "false"
                break
            elif opcion == "2":
                print("\n👔 Eliminar Empleado")
                print("===================================")
                eliminar_empleado(False)
                break
            elif opcion == "3":
                print("\n👪 Eliminar Padre de Familia")
                print("===================================")
                eliminar_padres_estudiantes(False)
                break
            elif opcion == "4":
                print("\n👩‍🎓 Eliminar Estudiante")
                print("===================================")
                eliminar_estudiante(False)
                break
            elif opcion == "5":
                print("\n👋 Saliendo del sistema...")
                break
            else:
                print("\n⚠ Opción inválida, intente de nuevo.")
        