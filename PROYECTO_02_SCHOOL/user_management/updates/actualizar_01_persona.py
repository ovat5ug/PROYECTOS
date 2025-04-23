from database import conexion as conn
from ..registration.registrar_00_funciones import nombre_competo,genero

def actualizar_persona(validar_cuantos_datos=True):
    with conn.get_connection() as conexion:
        try:
            if validar_cuantos_datos:
                cuantos_datos = int(input("ingrese la cantida de personas que ingresara al sistema: "))
                aP='un'
            else:
                cuantos_datos = 1  # Solo se registrara un solo usuario por login 
                aP='su'
            for i in range(cuantos_datos):

                aCorreo = input(f"ingrese {aP} antiguo correo electronico valido: ").lower()
                nCorreo  = input(f"ingrese {aP} nuevo correo electronico valido: ").lower()
                nom_com = nombre_competo()
                edad = int(input(f"ingrese {aP} edad: "))
                id_genero = genero()  
                direccion = input(f"ingrese {aP} direccion: ").lower()
                telefono = input(f"ingrese el telefono: ").lower()  
                
                eID_persona = conexion.cursor()
                eID_persona.execute("""
                select id_persona from persona
                where correo_electronico = ? """,(aCorreo)) # Obtenemos el último id_persona de la tabla persona
                row1 = eID_persona.fetchone() # Captura el ID persona
                extraer_idP = row1[0] if row1[0] is not None else 0  # row1[0] almacena valor mas alto del id_persona
                id_persona = extraer_idP

                print("hola estos son los datos hasta el momento: ",id_genero,nom_com[0],nom_com[1], nom_com[2], nom_com[3],edad,direccion,aCorreo,nCorreo,telefono,id_persona)
                cursor2 = conexion.cursor()
                # Insertar registro en la tabla persona
                cursor2.execute('''
                --actualizar registro persona
                UPDATE persona
                    SET id_genero = ?
                    ,primer_nombre = ?
                    ,segundo_nombre = ?
                    ,apellido_paterno = ?
                    ,apellido_materno = ?
                    ,edad = ?
                    ,direccion = ?
                    ,correo_electronico = ?
                    ,telefono = ?
                WHERE id_persona = ?  ''', 
                (id_genero,nom_com[0],nom_com[1], nom_com[2], nom_com[3],edad,direccion,nCorreo,telefono,id_persona))
                conexion.commit() # Confirma la transacción

                return nom_com[0],nCorreo,id_persona,aCorreo
        except Exception as e:
            conexion.rollback()  # Revierte los cambios en caso de error
            print("❌ Error en la transacción:", e)
            return nom_com[0],nCorreo,id_persona,aCorreo
