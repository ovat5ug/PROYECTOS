# from datetime import datetime
from database import conexion as conn
# from security import contrasena as passw 
# from security.contrasena_encriptacion_y_desencriptacion import desencriptar_clave as des_clave
# from ..registration.registrar_00_funciones import tipo_de_usuario as t_usuario, cargo 
# from .eliminar_01_persona import eliminar_persona

def eliminar_empleado(validar_cuantos_datos = True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantida de personas que eliminara del sistema: "))
                aP='un'
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
                aP='su'
            for i in range(cuantos_datos):

                correo = input(f"ingrese {aP} correo electronico valido para poder eliminar el registro: ").lower()    
                cursor = conexion.cursor()

                # Verificar si la persona está asociada a empleado o padres_estudiantes
                cursor.execute("""
                SELECT e.id_empleado, e.id_persona
                FROM empleado e
                JOIN persona p ON p.id_persona = e.id_persona
                WHERE p.correo_electronico = ?
                """, (correo,))
                row = cursor.fetchone() # Captura el ID generado
                print("estos valores devuelve",row)
                if row:
                    id_empleado, id_persona = row  # Desempaquetar valores directamente
                else:
                    id_empleado, id_persona = None, None  # Asignar valores nulos si no hay coincidencia
                # Si la persona no está en empleado ni en padres_estudiantes, eliminamos
                if id_empleado and id_persona:
                    cursor.execute("""
                        DELETE FROM empleado WHERE id_empleado = ? and id_persona = ?
                    """, (id_empleado,id_persona))
                    conexion.commit()
                    print(f"Registro del empleado con correo: {correo} eliminado exitosamente.")
                else:
                    print(f"No se pudo eliminar el registro del correo: '{correo}' del empleado.")
                # Cerrar cursor
                cursor.close()
            return correo
        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)
            return correo