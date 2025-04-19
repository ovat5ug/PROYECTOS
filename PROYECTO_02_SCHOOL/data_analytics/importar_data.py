import os
import csv

def creaando_csv_si_no_existe(ruta_archivo, encabezados=None, lista_datos=None):
    try:
        # Creando directorio si no existe
        directorio = os.path.dirname(ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
        
        # Verificando si el archivo ya existe
        existe_archivo = os.path.exists(ruta_archivo)
        existe_encabezado = False

        # Leyendo la primera línea para comprobar si los encabezados ya existen
        if existe_archivo:
            with open(ruta_archivo, 'r', encoding='utf-8') as csv_file:
                first_line = csv_file.readline().strip()
                if encabezados and first_line == ",".join(encabezados):
                    existe_encabezado = True

        # Creando el archivo CSV con condicion de existencia
        with open(ruta_archivo, 'a' if existe_archivo else 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)            
            
            # Escribir encabezados si no existen
            if encabezados and not existe_encabezado:
                writer.writerow(encabezados)
            
            # Escribir datos si se proporcionaron
            if lista_datos:
                writer.writerows(lista_datos)

            # imprimiendo segun que condicion
            print(f"El archivo CSV '{ruta_archivo}' ha sido {'actualizado' if existe_archivo else 'creado'} exitosamente."); return True
        
    except Exception as e:# manejo de exepcion de argumentos invalidos
        print(f"Error al crear el archivo CSV: {e}")
        return False