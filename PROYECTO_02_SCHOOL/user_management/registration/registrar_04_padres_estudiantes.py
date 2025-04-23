from datetime import datetime  # datetime
from database import conexion as conn
from security import contrasena as passw
from security.contrasena_encriptacion_y_desencriptacion import desencriptar_clave as des_clave
from .registrar_00_funciones import tipo_de_usuario as t_usuario
from .registrar_01_persona import registrar_persona
from .registrar_03_estudiante import registrar_estudiante

def registrar_padres_estudiantes(validar_cuantos_datos=True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantidad de padres que ingresara al sistema: "))
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
            for i in range(cuantos_datos):

                dui='sin registrar'
                tipo_de_usuario = t_usuario("padres")
                c_encriptada = passw.contrasena_encriptada(dui)
                c_desencriptada = des_clave.desencriptar(c_encriptada)
                fecha = datetime.now()
                fecha_actual = fecha.strftime("%Y-%m-%d")
                hora_actual = fecha.strftime("%H:%M:%S")

                r_persona = registrar_persona(False)
                r_estudiante = registrar_estudiante(False)
                id_persona = r_persona[2]  # obtenemo id generado de la funcion registrar_persona
                id_estudiante = r_estudiante[6]  # obtenemo id generado de la funcion registrar_estudiante

                uID_PE = conexion.cursor()
                uID_PE.execute("SELECT MAX(id_padres) FROM padres_estudiantes") # Obtenemos el último id_padres de la tabla padres_estudiantes
                row1 = uID_PE.fetchone() 
                ultimo_idPE = row1[0] if row1[0] is not None else 0  # row1[0] almacena valor mas alto del id_padres
                cursor1 = conexion.cursor()
                query1 = f"DBCC CHECKIDENT ('padres_estudiantes', RESEED, {ultimo_idPE})" # Reinicia el ID de la tabla empleado en "ultimo_idPE"
                cursor1.execute(query1) 
                conexion.commit()   # Confirma la transacción

                cursor2 = conexion.cursor()
                cursor2.execute('''--insertar registro empleado
                INSERT INTO padres_estudiantes (id_persona,
                id_estudiante) 
                OUTPUT INSERTED.id_padres, INSERTED.id_persona
                VALUES (?,?) ''', 
                (id_persona,id_estudiante))
                row2 = cursor2.fetchone()  # Captura el ID generado
                conexion.commit()  # Confirma la transacción
                id_padre = row2[0] # row2[0] almacena valor del id_padre                    
                conexion.commit() # Confirma la transacción
                                
                    # Usuario,Email,Password,id_Tipo_de_Usuario,Fecha,Hora,id_padre,Tipo_de_Usuario
            return r_persona[0],r_persona[1],c_encriptada,tipo_de_usuario[0],fecha_actual,hora_actual,id_padre,tipo_de_usuario[1]
        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)