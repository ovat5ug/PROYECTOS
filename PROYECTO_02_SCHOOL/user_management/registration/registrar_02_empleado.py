from datetime import datetime
from database import conexion as conn
from security import contrasena as passw 
from security.contrasena_encriptacion_y_desencriptacion import desencriptar_clave as des_clave
from .registrar_00_funciones import tipo_de_usuario as t_usuario, cargo 
from .registrar_01_persona import registrar_persona

def registrar_empleado(validar_cuantos_datos = True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantidad de empleados que ingresara al sistema: "))
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
            for i in range(cuantos_datos):

                carnet ='sin registrar'
                tipo_de_usuario = t_usuario("empleado")
                c_encriptada = passw.contrasena_encriptada(carnet)
                c_desencriptada = des_clave.desencriptar(c_encriptada)
                fecha = datetime.now()
                fecha_actual = fecha.strftime("%Y-%m-%d")
                hora_actual = fecha.strftime("%H:%M:%S")
                # fecha_contratacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                r_persona = registrar_persona(False)
                id_cargo = cargo()

                uID_empleado = conexion.cursor()
                uID_empleado.execute("SELECT MAX(id_empleado) FROM empleado") # Obtenemos el último id_empleado de la tabla empleado
                row1 = uID_empleado.fetchone() # Captura el ID generado
                ultimo_idE = row1[0] if row1[0] is not None else 0  # row1[0] almacena valor mas alto del id_persona
                cursor1 = conexion.cursor()
                query1 = f"DBCC CHECKIDENT ('empleado', RESEED, {ultimo_idE})" # Reinicia el ID de la tabla empleado en "ultimo_idE"
                cursor1.execute(query1)
                conexion.commit()   # Confirma la transacción

                id_persona = r_persona[2]  # obtenemo id generado de la funcion registrar_persona
                cursor2 = conexion.cursor()
                cursor2.execute('''--insertar registro empleado
                INSERT INTO empleado (id_persona, id_cargo) 
                OUTPUT INSERTED.id_empleado, INSERTED.id_persona
                VALUES (?,?) ''', 
                (id_persona,id_cargo))
                row2 = cursor2.fetchone()  # Captura el ID generado
                conexion.commit()  # Confirma la transacción
                id_empleado = row2[0] # row2[0] almacena valor del id_empleado

                          # Usuario,Email,Password,id_tipo_de_usuario,Fecha,Hora,id_persona,tipo_de_usuario
                return r_persona[0],r_persona[1],c_encriptada,tipo_de_usuario[0],fecha_actual,hora_actual,id_empleado,tipo_de_usuario[1]
        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)