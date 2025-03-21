import os
import csv
import importar_data
import registrar

def docCreado():
    func_registrar = registrar.registrar()
    lista_datos = func_registrar[0]# Retorna la primera lista de la tupla (datos del usuario)
    nombre_del_archivo = input( "ingrese el nombre para el archivo: ")
    if __name__ == "__main__":
        # Definiendo la ruta del archivo
        ruta_archivo = f"DATA\\{nombre_del_archivo}.csv"       
        # Definiendo los encabezados
        encabezados = ["Usuario", "Email", "Password", "Tipo_de_Usuario","Fecha","Hora"]    
        # invocando a la funcion
        importar_data.creaando_csv_si_no_existe(ruta_archivo, encabezados, lista_datos)
        
# documento = docCreado() # TEST
# documento