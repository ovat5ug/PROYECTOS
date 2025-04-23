import pyodbc
from config import database_config as cr
# import config.database_config as cr

def get_connection():
    try:
        conn = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={cr.connexion.server};"
            f"DATABASE={cr.connexion.database};"
            f"UID={cr.connexion.username};"
            f"PWD={cr.connexion.password};"
        )
        print("Conexión exitosa a la base de datos.")
        return conn
    except pyodbc.Error as error:
        print(f"Error en la conexión: {error}")
        return None
