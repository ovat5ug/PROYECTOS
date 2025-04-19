import os
import csv
import data_analytics.importar_data as importar_data
import users.registrar_02_empleado as r_empleado
import users.registrar_03_padres_estudiantes as r_padres
import users.registrar_04_estudiante as r_estudiante
import roots.rutinhas as r3
import database.conexion as conn

def docCreado(tipo_registro):
    lista_datos = [] # Inicializa la lista de datos
    if tipo_registro == "empleado":
        func_registrar = r_empleado.registrar_empleado(False)
        id_empleado = int(func_registrar[6]) # ID del empleado
        id_estudiante = None
        id_padres = None
    elif tipo_registro == "estudiante":
        func_registrar = r_estudiante.registrar_estudiante(False)
        id_estudiante = int(func_registrar[6]) # ID del estudiante
        id_empleado = None
        id_padres = None
    elif tipo_registro == "padres":
        func_registrar = r_padres.registrar_padres_estudiantes(False)
        id_padres = int(func_registrar[6]) # ID del padre
        id_estudiante = None
        id_empleado = None
    else:
        print("Tipo de registro no válido.")
        return
    
    if func_registrar:            # Usuario,Email,Password,Tipo_de_Usuario,Fecha,Hora
            lista_datos.append((func_registrar[0], func_registrar[1], func_registrar[2], 
                                func_registrar[7], func_registrar[4], func_registrar[5]))  # Almacenar datos
    uCarpeta = r3.rc.uCARPETA
    archivo = r3.ac.archivo         
    # Definiendo la ruta del archivo
    ruta_archivo = f"{uCarpeta}/{archivo}"       
    # Definiendo los encabezados
    encabezados = ["Usuario", "Email", "Password", "Tipo_de_Usuario","Fecha","Hora"]
        
    if (__name__ == "__main__" or __name__ != True): # o solo poner True como condicion 
        importar_data.creaando_csv_si_no_existe(ruta_archivo, encabezados, lista_datos)    
        conexion = conn.get_connection()
        # Verificar que "func_registrar" tiene datos válidos
        if func_registrar is None or len(func_registrar) < 6:
            print("❌ Error: `func_registrar` no tiene suficientes datos.")
        else:
            # Asegurar que `id_empleado`, `id_padres`, `id_estudiante` existen o permiten NULL
            id_empleado = id_empleado if id_empleado else None
            id_padres = id_padres if id_padres else None
            id_estudiante = id_estudiante if id_estudiante else None
            id_tipo_usuario = func_registrar[3] # ID del tipo de usuario (1=admin, 2=regular y 3=otros)

            uID_docC = conexion.cursor()
            uID_docC.execute("select MAX(id_login_usuario) from login_usuario") # Obtener el último ID de la tabla empleado
            row0 = uID_docC.fetchone() 
            ultimo_idDC = row0[0] if row0[0] is not None else 0  # Retorna el valor mas alto de la tabla empleado
            cursor0 = conexion.cursor()
            query0 = f"DBCC CHECKIDENT ('login_usuario', RESEED, {ultimo_idDC})"
            cursor0.execute(query0)  # Reinicia el ID de la tabla empleado en "ultimo_idE"
            conexion.commit()   # Confirma la transacción

            # print("📌 Valores a insertar:", id_empleado, id_padres, id_estudiante, id_tipo_usuario, 
            #       func_registrar[1], func_registrar[2], func_registrar[4], func_registrar[5])
            
            cursor1 = conexion.cursor()
            cursor1.execute("""
                INSERT INTO login_usuario(id_empleado, id_padres, id_estudiante, id_tipo_usuario, correo_electronico,
                passwords, fecha_creacion, hora_creacion) VALUES(?,?,?,?,?,?,?,?)
            """, (id_empleado, id_padres, id_estudiante, id_tipo_usuario, func_registrar[1], func_registrar[2], func_registrar[4], func_registrar[5]))
            conexion.commit()  # Confirmar cambios
            print("✅ Datos insertados correctamente.")# Tipo_de_Usuario,Email,Password,Fecha,Hora  
            return id_empleado, id_padres, id_estudiante, id_tipo_usuario, func_registrar[1], func_registrar[2], func_registrar[4], func_registrar[5]
    else:
        print("No se creó el archivo porque no ingresaste un nombre válido.")