from database import conexion as conn

def eliminar_estudiante(validar_cuantos_datos=True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantida de personas que eliminara del sistema: "))
                aP='el'
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
                aP='su'
            for i in range(cuantos_datos):

                correo = input(f"ingrese {aP} correo electronico del estudiante valido para poder eliminar el registro: ").lower()    
                cursor = conexion.cursor()

                # Verificar si la persona está asociada a estudiante
                cursor.execute("""
                select id_estudiante from estudiante 
                where correo_electronico = ?
                """, (correo,))
                row = cursor.fetchone() # Captura el ID generado
                # print("estos valores devuelve",row)
                if row:
                    id_estudiante = row  # Desempaquetar el valor directamente
                else:
                    id_estudiante = None  # Asignar valores nulos si no hay coincidencia
                # Si la persona no está en estudiante, eliminamos
                if id_estudiante:
                    cursor.execute(""" --- eliminar registro estudiante
                        DELETE FROM estudiante WHERE id_estudiante = ?
                    """, (id_estudiante))
                    conexion.commit()
                    print(f"Registro del estudiante con correo: {correo} eliminado exitosamente.")
                else:
                    print(f"No se pudo eliminar el registro del correo: '{correo}' del estudiante.")
                cursor.close()
            return id_estudiante,correo
        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)
            return id_estudiante,correo