import pyodbc
import pandas as pd
import matplotlib.pyplot as plt
import config.database_config as cr

try:
    conn = pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={cr.connexion.server};"      # Por ejemplo, 'localhost\\SQLEXPRESS'
        f"DATABASE={cr.connexion.database};"  # El nombre de la base de datos
        f"UID={cr.connexion.username};"       # Usuario de SQL Server
        f"PWD={cr.connexion.password};"       # Contraseña de SQL Server
    )
    print("Conexión exitosa a la base de datos.")
# OBTENIENDO IRMOCION GENERAL DE NOTAS DE LOS ESTUDIANTES
    query = '''
    SELECT id_calificaciones,e.id_estudiante, primer_nombre,apellido_materno,
	    g.nGrado,nMateria,nMes, correo_electronico, n_prom_final 
    FROM calificaciones c
    JOIN
    estudiante e
    ON c.id_estudiante = e.id_estudiante
    JOIN
    materia m
    ON m.id_materia = c.id_materia
    JOIN grado g
    ON g.id_grado = e.id_grado
    ORDER BY id_estudiante
'''
    # Ejecutar la consulta y guardar el resultado en un DataFrame
    estudiantes = pd.read_sql_query(query, conn)
    
    # Mostrar el producto más rentable
    print(estudiantes)
except pyodbc.Error as error:
    print(f"Error en la conexión o consulta: {error}")
    if 'conn' in locals() and conn is not None:
        conn.rollback() # revierte los cambios si hubo un error.
        print("Cambios revertidos.")

finally:
    if 'conn' in locals() and conn is not None:
        conn.close() # cerramos la conn para liberar recursos del sistema
        print("Conexión cerrada.")