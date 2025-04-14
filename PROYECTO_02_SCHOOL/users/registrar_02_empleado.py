from datetime import datetime  # datetime
from database import conexion as conn   
from security import contrasena as pass1, contrasena_encriptacion_y_desencriptacion as pass2
import users.registrar_00_funciones as calc
import users.registrar_01_persona as registrar_persona

def registrar_empleado(validar_cuantos_datos=True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantidad de empleados que ingresara al sistema: "))
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
            for i in range(cuantos_datos):
                id_persona=registrar_persona.registrar_persona(False)
                id_cargo=calc.cargo()
                # fecha_contratacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                uID_empleado= conexion.cursor()
                uID_empleado.execute("SELECT MAX(id_empleado) FROM empleado") # Obtener el último ID de la tabla empleado
                row0 = uID_empleado.fetchone() 
                ultimo_idE = row0[0] if row0[0] is not None else 0  # Retorna el valor mas alto de la tabla empleado
                cursor0 = conexion.cursor()
                query0 = f"DBCC CHECKIDENT ('empleado', RESEED, {ultimo_idE})"
                cursor0.execute(query0)  # Reinicia el ID de la tabla empleado en "ultimo_idE"
                conexion.commit()   # Confirma la transacción

                uID_persona= conexion.cursor()
                uID_persona.execute("SELECT MAX(id_persona) FROM persona") # Obtener el último ID de la tabla persona
                row1 = uID_persona.fetchone() 
                ultimo_idP = row1[0] if row1[0] is not None else 0  # Retorna el valor mas alto de la tabla persona
                
                id_persona= ultimo_idP  # ID para el nuevo registro de la persona actual
                cursor1 = conexion.cursor()
                cursor1.execute('''--insertar registro empleado
                INSERT INTO empleado (id_persona,
                id_cargo) VALUES (?,?) ''', 
                (id_persona,id_cargo))            
                conexion.commit() # Confirma la transacción

        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)
