import os
import csv
import importar_data
import registrar

def docCreado(validar_cuantos_datos=True):
    func_registrar = registrar.registrar(validar_cuantos_datos)
    lista_datos = func_registrar[0]# Retorna la primera lista de la tupla (datos del usuario)
    nombre_del_archivo = input( "ingrese el nombre para el archivo: ")
    nCarpeta="DATA" # Se guarda en la raiz de la carpeta en donde se ejecuta
    if (__name__ == "__main__" or __name__ != True): # o solo poner True como condicion        
        if nombre_del_archivo.strip():# Verifica que no esté vacío ni solo contenga espacios
            # Definiendo la ruta del archivo
            ruta_archivo = f"{nCarpeta}\\{nombre_del_archivo}.csv"       
            # Definiendo los encabezados
            encabezados = ["Usuario", "Email", "Password", "Tipo_de_Usuario","Fecha","Hora"]    
            # invocando a la funcion
            importar_data.creaando_csv_si_no_existe(ruta_archivo, encabezados, lista_datos)
        else:
            print("No se creó el archivo porque no ingresaste un nombre válido.")

# poner "(false)" para iniciar solamente una vez el registro de datos        
# documento = docCreado() # TEST
# documento