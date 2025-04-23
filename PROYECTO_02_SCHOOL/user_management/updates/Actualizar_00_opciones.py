from .actualizar_01_persona import actualizar_persona
from .actualizar_02_empleado import actualizar_empleado
from .actualizar_03_estudiante import actualizar_estudiante
from .actualizar_04_padres_estudiantes import actualizar_padres_estudiantes


def actualizar_opciones():
    if __name__ == "__main__" or __name__ != True:
        while True:
            print("\n📌 MENÚ:")
            print("1️⃣ Actualizar Persona")
            print("2️⃣ Actualizar Empleado")
            print("3️⃣ Actualizar Padre de Familia")
            print("4️⃣ Actualizar Estudiante")
            print("5️⃣ Salir")
            
            opcion = input("\nSeleccione una opción: ")

            if opcion == "1":
                print("\n👤 Actualizar Persona")
                print("===================================")
                actualizar_persona(False)  # un solo registro usando "false"
                break
            elif opcion == "2":
                print("\n👔 Actualizar Empleado")
                print("===================================")
                actualizar_empleado(False)
                break
            elif opcion == "3":
                print("\n👪 Actualizar Padre de Familia")
                print("===================================")
                actualizar_padres_estudiantes(False)
                break
            elif opcion == "4":
                print("\n👩‍🎓 Actualizar Estudiante")
                print("===================================")
                actualizar_estudiante(False)
                break
            elif opcion == "5":
                print("\n👋 Saliendo del sistema...")
                break
            else:
                print("\n⚠ Opción inválida, intente de nuevo.")
        