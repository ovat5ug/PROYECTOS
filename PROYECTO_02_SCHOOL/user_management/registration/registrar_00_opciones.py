from .registrar_01_persona import registrar_persona
from .registrar_02_empleado import registrar_empleado
from .registrar_03_estudiante import registrar_estudiante
from .registrar_04_padres_estudiantes import registrar_padres_estudiantes

def registrar_opciones():      
    if __name__ == "__main__" or __name__ != True:
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
                registrar_persona(False)  # un solo registro usando "false"
                break
            elif opcion == "2":
                print("\n👔 Registrar Empleado")
                print("===================================")
                registrar_empleado(False)
                break
            elif opcion == "3":
                print("\n👪 Registrar Padre de Familia")
                print("===================================")
                registrar_padres_estudiantes(False)
                break
            elif opcion == "4":
                print("\n👩‍🎓 Registrar Estudiante")
                print("===================================")
                registrar_estudiante(False)
                break
            elif opcion == "5":
                print("\n👋 Saliendo del sistema...")
                break
            else:
                print("\n⚠ Opción inválida, intente de nuevo.")