from database import conexion as conn   
import users.registrar_00_funciones as funcs

def registrar_persona(validar_cuantos_datos=True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantida de personas que ingresara al sistema: "))
                aP='la'
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
                aP='su'
            for i in range(cuantos_datos):
                               
                nom_com = funcs.nombre_competo()
                id_genero = funcs.genero()  
                edad = int(input(f"ingrese {aP} edad: "))
                correo = input(f"ingrese {aP} correo: ").lower()
                direccion = input(f"ingrese {aP} direccion: ").lower()
                telefono = input(f"ingrese el telefono: ").lower()  
                
                uID_persona= conexion.cursor()
                uID_persona.execute("SELECT MAX(id_persona) FROM persona") # Obtenemos el último id_persona de la tabla persona
                row1 = uID_persona.fetchone() # Captura el ID generado
                ultimo_idP = row1[0] if row1[0] is not None else 0  # row1[0] almacena valor mas alto del id_persona
                cursor1 = conexion.cursor()
                query1 = f"DBCC CHECKIDENT ('persona', RESEED, {ultimo_idP})" # Reinicia el ID de la tabla persona en "ultimo_idP"
                cursor1.execute(query1)  
                conexion.commit() # Confirma la transacción
                
                cursor2 = conexion.cursor()
                # Insertar registro en la tabla persona
                cursor2.execute('''--insertar registro persona 
                INSERT INTO persona (id_genero, primer_nombre, segundo_nombre, apellido_paterno, 
                apellido_materno, edad, direccion, correo_electronico, telefono)
                OUTPUT INSERTED.id_persona 
                VALUES (?,?,?,?,?,?,?,?,?) ''', 
                (id_genero,nom_com[0],nom_com[1], nom_com[2], nom_com[3],edad,direccion,correo,telefono))
                row2 = cursor2.fetchone()  # Captura el ID generado
                id_persona = row2[0]  # row2[0] almacena valor mas alto del id_persona
                conexion.commit() # Confirma la transacción

                return nom_com[0],correo,id_persona
        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)
