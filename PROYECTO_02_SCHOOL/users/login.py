import csv
import os
import users.users as u
import roots.rutinhas as r2
import database.conexion as conn
import users.login_users as login_users
import security.contrasena_encriptacion_y_desencriptacion as contrasena
# ======= Función para iniciar sesión =======
def validar_login():
    # while True:
        try:
            correo = input("Ingrese su correo: ").strip()
            contraseña=input("Ingrese su contraseña: ")
            usuario= u.Users(correo,contraseña)
            login_usuario = login_users.Login(usuario.email,usuario.password)

            with conn.get_connection() as conexion:
                cursor1 = conexion.cursor()
                cursor1.execute('''
                SELECT p.primer_nombre, p.apellido_materno, lu.correo_electronico, lu.passwords
                FROM login_usuario lu
                JOIN empleado e ON e.id_empleado = lu.id_empleado
                JOIN persona p ON p.id_persona = e.id_persona
                WHERE lu.correo_electronico = ?
''', (usuario.email))
                row1 = cursor1.fetchone()
                print(f"Buscando usuario con email: {usuario.email} y contraseña cifrada: {row1[3]}")
                # print(row1,"estamos ready")
                # ('Rosa', 'Sosa', 'rosalk6874@gmail.com', 'gAAAAABn3aCblNjbuLUkKyWaV57a0RUpfM9rvv4jYpt6LutaFl58vNgjLGGtWcMRtzWvRxtyc88ANvwIDQXJmPCMZnCZM24CLg==')
                if row1 and contrasena.desencriptar_clave.desencriptar(row1[3]) == login_usuario.password:
                    print(f"\n✅ {row1[0]} has hecho inicio de sesión exitoso con: {login_usuario.email}")
                    return
                else:
                    print(f"\n❌ Correo o contraseña incorrectos. ")
        except Exception as e:
            print(f"\n❌ Ocurrió un error: {e} ")
            print(f"Error: {type(e).__name__}")
            validar_login() 
        finally:
            print("\n🔒 Finalizando proceso de inicio de sesión.")
