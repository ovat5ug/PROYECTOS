from datetime import datetime
from database import conexion as conn
from security import contrasena as passw 
from security.contrasena_encriptacion_y_desencriptacion import desencriptar_clave as des_clave
from ..registration.registrar_00_funciones import tipo_de_usuario as t_usuario, cargo 
from .actualizar_01_persona import actualizar_persona

def actualizar_empleado(validar_cuantos_datos = True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantida de personas que ingresara al sistema: "))
                aP='un'
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
                aP='su'
            for i in range(cuantos_datos):

                u_persona = actualizar_persona(False)
                id_persona = u_persona[2]
                nCorreo = u_persona[1]

                carnet ='sin registrar'
                tipo_de_usuario = t_usuario("empleado")
                c_encriptada = passw.contrasena_encriptada(carnet)
                c_desencriptada = des_clave.desencriptar(c_encriptada)
                fecha = datetime.now()
                fecha_actual = fecha.strftime("%Y-%m-%d")
                hora_actual = fecha.strftime("%H:%M:%S")
                # fecha_contratacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                
                id_cargo = cargo()

                eID_EmPe = conexion.cursor()
                eID_EmPe.execute("""
                select e.id_empleado from empleado e
                join persona p
                on p.id_persona = e.id_persona
                join cargo c
                on c.id_cargo = e.id_cargo
                where p.correo_electronico = ? and e.id_persona = ?
                """,(nCorreo,id_persona)) # Obtenemos el último id_empleado de la tabla empleado
                row1 = eID_EmPe.fetchone() # Captura el ID generado
                Extraer_idEM = row1[0] if row1[0] is not None else 0  # row1[0] almacena valor mas alto del id_persona
                id_empleado = Extraer_idEM
                # Extraer_idP = row1[1] if row1[1] is not None else 0  # row1[0] almacena valor mas alto del id_persona
                # id_persona = Extraer_idP
                print("estos son los valores: ",u_persona[0],u_persona[1],c_encriptada,tipo_de_usuario[0],fecha_actual,hora_actual,id_empleado,tipo_de_usuario[1],id_empleado,id_persona,id_cargo,nCorreo)

                cursor2 = conexion.cursor()
                cursor2.execute('''--actualizar registro empleado
                UPDATE empleado
                SET id_persona = ?
                    ,[id_cargo] = ?
                WHERE id_empleado = ?''', 
                (id_persona,id_cargo,id_empleado))
                conexion.commit()  # Confirma la transacción
                # ---------------------------------------- falla la obtencion del id empleado para el cambio de cargo
                          # Usuario,nEmail,Password,id_tipo_de_usuario,Fecha,Hora,id_persona,tipo_de_usuario
                return u_persona[0],u_persona[1],c_encriptada,tipo_de_usuario[0],fecha_actual,hora_actual,id_persona,tipo_de_usuario[1],id_empleado,id_cargo,nCorreo
        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)
            return print("los valores: ",u_persona[0],u_persona[1],c_encriptada,tipo_de_usuario[0],fecha_actual,hora_actual,id_empleado,tipo_de_usuario[1],id_empleado,id_persona,id_cargo,nCorreo)