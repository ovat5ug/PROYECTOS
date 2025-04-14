from datetime import datetime  # datetime
from database import conexion as conn   
from security import contrasena as pass1, contrasena_encriptacion_y_desencriptacion as pass2
import users.registrar_00_funciones as calc

def registrar_persona(validar_cuantos_datos=True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantida de personas que ingresara al sistema: "))
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
            for i in range(cuantos_datos):               
                nom_com=calc.nombre_competo()
                id_genero=calc.genero()  
                edad=int(input("ingrese la edad: "))
                correo=input("ingrese el correo: ").lower()
                direccion=input("ingrese la direccion: ").lower()
                telefono=input("ingrese el telefono: ").lower()  
                
                uID_persona= conexion.cursor()
                uID_persona.execute("SELECT MAX(id_persona) FROM persona") # Obtener el último ID de la tabla persona
                row0 = uID_persona.fetchone() 
                ultimo_id = row0[0] if row0[0] is not None else 0  # Retorna el valor mas alto de la tabla persona
                cursor0 = conexion.cursor()
                query0 = f"DBCC CHECKIDENT ('persona', RESEED, {ultimo_id})"
                cursor0.execute(query0)  # Reinicia el ID de la tabla persona en "ultimo_idE"
                conexion.commit()   # Confirma la transacción
                
                cursor2 = conexion.cursor()
                cursor2.execute('''--insertar registro persona
                INSERT INTO persona (id_genero,primer_nombre,segundo_nombre,
                apellido_paterno,apellido_materno,edad,direccion,
                correo_electronico,telefono) VALUES (?,?,?,?,?,?,?,?,?) ''', 
                (id_genero,nom_com[0],nom_com[1], nom_com[2], nom_com[3],edad,direccion,correo,telefono))
            # return f'"registros ingresados:" {id_genero},{nom_com[0]},{nom_com[1]},{nom_com[2]},{nom_com[3]},{edad},{direccion},{correo}'
                conexion.commit() # Confirma la transacción
            # return f'"registros ingresados:" {id_estudiante},{id_grado},{id_genero},{carnet},{nombre},{nombre}, {apellido}, {apellido},{edad},{correo}'
        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)
