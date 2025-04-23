from datetime import datetime  # datetime
from database import conexion as conn
from security import contrasena as passw
from security.contrasena_encriptacion_y_desencriptacion import desencriptar_clave as des_clave
from ..registration.registrar_00_funciones import tipo_de_usuario as t_usuario
from .actualizar_01_persona import actualizar_persona
from .actualizar_03_estudiante import actualizar_estudiante

def actualizar_padres_estudiantes(validar_cuantos_datos=True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantidad de padres que ingresara al sistema: "))
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
            for i in range(cuantos_datos):

                # vCorreo_ES = input('Introduzca el correo enlace del estudiante: ')
                r_persona = actualizar_persona(False)
                r_estudiante = actualizar_estudiante(False)
                id_persona = r_persona[2]  # obtenemo id generado de la funcion registrar_persona
                nCorreo_PE = r_persona[1]
                id_estudiante = r_estudiante[7]  # obtenemo id generado de la funcion registrar_estudiante
                nCorreo_ES = r_estudiante[1]

                dui='sin registrar'
                tipo_de_usuario = t_usuario("padres")
                c_encriptada = passw.contrasena_encriptada(dui)
                c_desencriptada = des_clave.desencriptar(c_encriptada)
                fecha = datetime.now()
                fecha_actual = fecha.strftime("%Y-%m-%d")
                hora_actual = fecha.strftime("%H:%M:%S")

# 1- edita persona      --> correo
# 2- edita estudiante   --> correo
# 3- teniendo los correos --> me retona el id_padres
     

                eID_PE = conexion.cursor()
                eID_PE.execute("""
                select id_padres from padres_estudiantes pe
                join persona p
                on p.id_persona = pe.id_persona
                join estudiante e
                on e.id_estudiante = pe.id_estudiante
                where e.correo_electronico = ? 
                and p.correo_electronico = ? """,(nCorreo_ES,nCorreo_PE)) # Obtenemos el último id_padres de la tabla padres_estudiantes
                row1 = eID_PE.fetchone() 
                extraer_idPE = row1[0] if row1[0] is not None else 0  # row1[0] almacena valor mas alto del id_padres
                id_padres = extraer_idPE

  

                cursor2 = conexion.cursor()
                cursor2.execute('''--actualizar registro empleado
                --actualizar registro empleado
                UPDATE padres_estudiantes
                SET id_persona = ?
                    ,id_estudiante = ?
                WHERE id_padres = ?  ''', 
                (id_persona,id_estudiante,id_padres))
                conexion.commit()  # Confirma la transacción
                
                    # Usuario,Email,Password,id_Tipo_de_Usuario,Fecha,Hora,id_padre,Tipo_de_Usuario
            return id_persona,id_estudiante,id_padres
        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)
            return id_persona,id_estudiante,id_padres