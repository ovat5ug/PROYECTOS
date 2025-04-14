from datetime import datetime  # datetime
from database import conexion as conn   
from security import contrasena as pass1, contrasena_encriptacion_y_desencriptacion as pass2
import users.registrar_00_funciones as calc
import users.registrar_01_persona as registrar_persona
import users.registrar_04_estudiante as registrar_estudiante

def registrar_padres_estudiantes(validar_cuantos_datos=True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantidad de padres que ingresara al sistema: "))
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
            for i in range(cuantos_datos):                
                persona=registrar_persona.registrar_persona(False)
                estudiante=registrar_estudiante.registrar_estudiante(False)
            
                uID_PE= conexion.cursor()#Permite ejecutar consultas SQL en padres_estudiantes
                uID_PE.execute("SELECT MAX(id_padres) FROM padres_estudiantes") # Obtener el último ID de la tabla padres_estudiantes
                row0 = uID_PE.fetchone() 
                ultimo_idPE = row0[0] if row0[0] is not None else 0  # Retorna el valor mas alto de la tabla padres_estudiantes
                cursor0 = conexion.cursor()
                query0 = f"DBCC CHECKIDENT ('padres_estudiantes', RESEED, {ultimo_idPE})"
                cursor0.execute(query0)  # Reinicia el ID de la tabla padres_estudiantes en "ultimo_idPF"
                conexion.commit()   # Confirma la transacción

                uID_persona = conexion.cursor()
                uID_persona.execute("SELECT MAX(id_persona) FROM persona") # Obtener el último ID de la tabla persona
                row1 = uID_persona.fetchone() 
                ultimo_idP = row1[0] if row1[0] is not None else 0  # Retorna el valor mas alto de la tabla persona
                
                uID_estudiante = conexion.cursor()
                uID_estudiante.execute("SELECT MAX(id_estudiante) FROM estudiante") # Obtener el último ID de la tabla persona
                row2 = uID_estudiante.fetchone() 
                ultimo_idE = row2[0] if row2[0] is not None else 0  # Retorna el valor mas alto de la tabla persona
            
                id_persona= ultimo_idP  # ID para el nuevo registro de la persona actual
                id_estudiante= ultimo_idE  # ID para el nuevo registro del estudiante actual
                
                cursor1 = conexion.cursor()
                cursor1.execute('''--insertar registro empleado
                INSERT INTO padres_estudiantes (id_persona,
                id_estudiante) VALUES (?,?) ''', 
                (id_persona,id_estudiante))            
                conexion.commit() # Confirma la transacción

        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)