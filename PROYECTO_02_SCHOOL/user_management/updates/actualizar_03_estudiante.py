from datetime import datetime
from database import conexion as conn
from security.contrasena_encriptacion_y_desencriptacion import desencriptar_clave as des_clave
from security import contrasena as passw
from ..registration.registrar_00_funciones import nombre_competo,grado,genero,carnet,tipo_de_usuario as t_usuario

def actualizar_estudiante(validar_cuantos_datos=True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantida de personas que ingresara al sistema: "))
                aP='un'
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
                aP='su'
            for i in range(cuantos_datos):
                
                aCorreo = input(f"Estudiante ingrese {aP} antiguo correo electronico valido: ").lower()
                nCorreo  = input(f"Estudiante ingrese {aP} nuevo correo electronico valido: ").lower()             
                carne = carnet()
                nom_com = nombre_competo()
                edad = int(input(f"ingrese {aP} edad: "))
                id_genero = genero()
                id_grado = grado()
                tipo_de_usuario = t_usuario("estudiantes") 
                estado = 1

                c_encriptada = passw.contrasena_encriptada(carne)
                c_desencriptada = des_clave.desencriptar(c_encriptada)
                fecha = datetime.now()
                fecha_actual = fecha.strftime("%Y-%m-%d")
                hora_actual = fecha.strftime("%H:%M:%S")    
                
                eID_estudiante = conexion.cursor()
                eID_estudiante.execute("""
                select id_estudiante from estudiante
                where correo_electronico = ?""",(aCorreo))  # Obtener el último ID de la tabla matricula
                row0 = eID_estudiante.fetchone() 
                extraer_idES = row0[0] if row0[0] is not None else 0  # Retorna el valor mas alto de la tabla matricula
                id_estudiante = extraer_idES

                cursor2 = conexion.cursor()
                cursor2.execute('''--actualizar registro estudiante
                UPDATE estudiante
                SET id_grado = ?
                    ,id_genero = ?
                    ,carnet = ?
                    ,primer_nombre = ?
                    ,segundo_nombre = ?
                    ,apellido_paterno = ?
                    ,apellido_materno = ?
                    ,edad = ?
                    ,correo_electronico = ?
                WHERE id_estudiante = ?''', 
                (id_grado,id_genero,carne,nom_com[0],nom_com[1], nom_com[2], nom_com[3],edad,nCorreo,id_estudiante))
                conexion.commit() # Confirma la transacción

                # Usuario,Email,Password,id_tipo_de_usuario,Fecha,Hora,id_estudiante,Tipo_de_Usuario
                return nom_com[0],nCorreo,c_encriptada,tipo_de_usuario[0],fecha_actual,hora_actual,tipo_de_usuario[1],id_estudiante,aCorreo
        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)
            return nom_com[0],nCorreo,c_encriptada,tipo_de_usuario[0],fecha_actual,hora_actual,tipo_de_usuario[1],id_estudiante,aCorreo