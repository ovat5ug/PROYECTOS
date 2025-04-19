from datetime import datetime  # datetime
from database import conexion as conn   
from security import contrasena as pass1, contrasena_encriptacion_y_desencriptacion as pass2
import users.registrar_00_funciones as funcs

def registrar_estudiante(validar_cuantos_datos=True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantidad de estudiantes que ingresara al sistema: "))
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
            for i in range(cuantos_datos):                
             
                carnet='sin registrar'
                nom_com=funcs.nombre_competo()
                id_grado=funcs.grado()
                id_genero=funcs.genero()
                tipo_de_usuario=funcs.tipo_de_usuario("estudiantes") 
                edad=int(input("ingrese la edad: "))
                correo=input("ingrese el correo: ").lower()
                estado=1

                c_encriptada= pass1.contrasena_encriptada(carnet)
                fecha = datetime.now()
                fecha_actual = fecha.strftime("%Y-%m-%d")
                hora_actual = fecha.strftime("%H:%M:%S")    
                
                uID_matricula = conexion.cursor()
                uID_matricula.execute("SELECT MAX(id_matricula) FROM matricula")  # Obtener el último ID de la tabla matricula
                row0 = uID_matricula.fetchone() 
                ultimo_id = row0[0] if row0[0] is not None else 0  # Retorna el valor mas alto de la tabla matricula
                cursor0 = conexion.cursor()
                query0 = f"DBCC CHECKIDENT ('matricula', RESEED, {ultimo_id})"
                cursor0.execute(query0)  # Reinicia el ID de la tabla matricula
                conexion.commit()   # Confirma la transacción
                
                cursor1 = conexion.cursor()
                cursor1.execute('''
                    INSERT INTO matricula (id_estado)
                    OUTPUT INSERTED.id_matricula, INSERTED.id_estado
                    VALUES (?);
                ''', (estado))
                row1 = cursor1.fetchone()  # Captura el ID generado
                conexion.commit()  # Confirma la transacción
                id_estudiante = row1[0]# asignando el id_estudiante al valor recuperado de cursor1

                cursor2 = conexion.cursor()
                cursor2.execute('''--insertar registro estudiante
                INSERT INTO estudiante (id_estudiante,id_grado,id_genero,carnet,primer_nombre,
                segundo_nombre,apellido_paterno,apellido_materno,edad,correo_electronico)
                VALUES (?,?,?,?,?,?,?,?,?,?) ''', 
                (id_estudiante,id_grado,id_genero,carnet,nom_com[0],nom_com[1], nom_com[2], nom_com[3],edad,correo))
                conexion.commit() # Confirma la transacción

                # Usuario,Email,Password,id_tipo_de_usuario,Fecha,Hora,id_estudiante,Tipo_de_Usuario
                return nom_com[0],correo,c_encriptada,tipo_de_usuario[0],fecha_actual,hora_actual,id_estudiante,tipo_de_usuario[1]
        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)