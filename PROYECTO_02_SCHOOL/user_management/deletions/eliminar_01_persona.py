from database import conexion as conn
from ..registration.registrar_00_funciones import nombre_competo,genero

def eliminar_persona(validar_cuantos_datos=True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantida de personas que ingresara al sistema: "))
                aP='un'
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
                aP='su'
            for i in range(cuantos_datos):

                correo = input(f"ingrese {aP} correo electronico valido para poder eliminar el registro: ").lower()    
                cursor = conexion.cursor()

                # Verificar si la persona está asociada a empleado o padres_estudiantes
                cursor.execute("""
                    SELECT COUNT(*) 
                    FROM empleado e
                    JOIN persona p ON p.id_persona = e.id_persona
                    WHERE p.correo_electronico = ?
                """, (correo,))
                registro_empleado = cursor.fetchone()[0]

                cursor.execute("""
                    SELECT COUNT(*) 
                    FROM padres_estudiantes pe
                    JOIN persona p ON p.id_persona = pe.id_persona
                    WHERE p.correo_electronico = ?
                """, (correo,))
                registro_padre_estudiante = cursor.fetchone()[0]

                # Si la persona no está en empleado ni en padres_estudiantes, se elimina
                if registro_empleado == 0 and registro_padre_estudiante == 0:
                    cursor.execute("""
                        DELETE FROM persona WHERE correo_electronico = ?
                    """, (correo,))
                    conexion.commit()
                    print(f"Registro de persona con correo {correo} eliminado exitosamente.")
                else:
                    if registro_empleado >= 1:
                        print(f"No se puede eliminar el correo '{correo}' del empleado porque está asociado a empleado o padres_estudiantes.")
                    else:
                        print(f"No se puede eliminar el correo '{correo}' del padre_familia porque está asociado a empleado o padres_estudiantes.")
                cursor.close()
            return correo
        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)
            return correo
