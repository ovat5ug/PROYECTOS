# from datetime import datetime  # datetime
from database import conexion as conn
# from security import contrasena as passw
# from security.contrasena_encriptacion_y_desencriptacion import desencriptar_clave as des_clave
# from ..registration.registrar_00_funciones import tipo_de_usuario as t_usuario
# from .eliminar_01_persona import actualizar_persona
# from .eliminar_03_estudiante import actualizar_estudiante

def eliminar_padres_estudiantes(validar_cuantos_datos=True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantida de personas que eliminara del sistema: "))
                aP='el'
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
                aP='su'
            for i in range(cuantos_datos):

                correo = input(f"ingrese {aP} correo electronico del padre valido para poder eliminar el registro: ").lower()    
                cursor = conexion.cursor()

                # Verificar si la persona está asociada a padres_estudiantes
                cursor.execute("""
                select pe.id_padres from padres_estudiantes pe
                join persona p
                on p.id_persona = pe.id_persona
                join estudiante e
                on e.id_estudiante = pe.id_estudiante
                where p.correo_electronico = ?
                """, (correo,))
                row = cursor.fetchone() # Captura el ID generado
                # print("estos valores devuelve",row)
                if row:
                    id_padres = row  # Desempaquetar el valor directamente
                else:
                    id_padres = None  # Asignar valores nulos si no hay coincidencia
                # Si la persona no está en padres_estudiantes, eliminamos
                if id_padres:
                    cursor.execute("""
                        DELETE FROM padres_estudiantes WHERE id_padres = ?
                    """, (id_padres))
                    conexion.commit()
                    print(f"Registro del padre de familia con correo: {correo} eliminado exitosamente.")
                else:
                    print(f"No se pudo eliminar el registro del correo: '{correo}' del padre de familia.")
                cursor.close()
            return correo
        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)
            return correo