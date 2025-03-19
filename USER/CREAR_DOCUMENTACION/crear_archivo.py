import os
import csv
import importar_data
from USER import registrar

lista_datos = registrar.lista_datos

def docCreado():

    if __name__ == "__main__":
        # Definiendo la ruta del archivo
        ruta_archivo = f"DATA\\{importar_data.nombre_del_archivo}.csv"       
        # Definiendo los encabezados
        encabezados = ["Usuario", "Email", "Password", "Tipo_de_Usuario","Fecha","Hora"]    
        # invocando a la funcion
        importar_data.creaando_csv_si_no_existe(ruta_archivo, encabezados, lista_datos)

documento=docCreado()
documento