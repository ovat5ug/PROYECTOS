import user_management.registration.registrar_01_persona as rp
import user_management.registration.registrar_02_empleado as rem
import user_management.registration.registrar_03_estudiante as res
import user_management.registration.registrar_04_padres_estudiantes as rpe

import user_management.updates.actualizar_01_persona as up
import user_management.updates.actualizar_02_empleado as uem
import user_management.updates.actualizar_03_estudiante as ues
import user_management.updates.actualizar_04_padres_estudiantes as upe

import user_management.deletions.eliminar_01_persona as dp
import user_management.deletions.eliminar_02_empleado as dem
import user_management.deletions.eliminar_03_estudiante as des
import user_management.deletions.eliminar_04_padres_estudiantes as dpe

def opciones_multiples(tipo_usuario):
    while True:
            
        modo ={
            1: "Registrar",
            2: "Actualizar",
            3: "Eliminar"
        }
        usuario = {    
            1: 'Persona',
            2: 'Empleado',
            3: 'Estudiante',
            4: 'Padre de Estudiante'
            }
        emoji_num = {
        0: "0️⃣",
        1: "1️⃣",
        2: "2️⃣",
        3: "3️⃣",
        4: "4️⃣",
        5: "5️⃣",
        6: "6️⃣",
        7: "7️⃣",
        8: "8️⃣",
        9: "9️⃣"
    }

        try:
            n = 0 #  1: "registrar", 2: "actualizar", 3: "eliminar"
            if bool(modo) == True: 
                for i in range(3):
    # -----------------------------> valida tipo de usuario para msg
                    if tipo_usuario == 'persona':
                        c=usuario[1]
                        d='la'                    
                    elif tipo_usuario == 'empleado':
                        c=usuario[2]
                        d='el'
                    elif tipo_usuario == 'estudiante':
                        c=usuario[3]
                        d='el'
                    elif tipo_usuario == 'padres':
                        c=usuario[4]
                        d='al'
                    else:
                        print("dato invalidado")
                        break
    # -----------------------> crea estructura del menu           
                    i+=1
                    n+=1
                    if i == 1:
                        b = c
                    elif i == 2:
                        b = c
                    elif i == 3:
                        b = c
                    else:
                        b = c
                    print(f"{emoji_num[i]}  {modo[n]} {d} {b}")
    # -------------------------> valida tipo de funcion
                elejir_accion(tipo_usuario)
                break
            else: 
                print("dato invalido")
                print("intentelo de nuevo")
                opciones_multiples(tipo_usuario)
        except ValueError as e:
            print(f"ingrese un valor valido el error es: {e}")

def elejir_accion(tipo_usuario):
    while True:   
        try:
            if tipo_usuario == 'persona' or tipo_usuario == 'empleado' or tipo_usuario == 'estudiante' or tipo_usuario == 'padres':
                accion=int(input("ingrese que tipo de accion desea hacer: "))
# ------------------------------------------> FUNCION PARA PERSONA
                if tipo_usuario == 'persona':
                    if accion == 1:
                        rp.registrar_persona(False)
                        print(f"🚀 {tipo_usuario} acción Finalizada...")
                        print(f"👋 Saliendo del sistema...")
                        break
                    elif accion == 2:
                        up.actualizar_persona(False)
                        print(f"🚀 {tipo_usuario} acción Finalizada...")
                        print(f"👋 Saliendo del sistema...")
                        break
                    elif accion == 3:
                        dp.eliminar_persona(False)
                        print(f"🚀 {tipo_usuario} acción Finalizada...")
                        print(f"👋 Saliendo del sistema...")
                        break
                    else:
                        print("accion no valida")
                        print("intente de nuevo")
                        elejir_accion(tipo_usuario)
# -------------------------------------------> FUNCION PARA EMPLEADO
                if tipo_usuario == 'empleado':
                    if accion == 1:
                        rem.registrar_empleado(False)
                        print(f"🚀 {tipo_usuario} acción Finalizada...")
                        print(f"👋 Saliendo del sistema...")
                        break
                    elif accion == 2:
                        uem.actualizar_empleado(False)
                        print(f"🚀 {tipo_usuario} acción Finalizada...")
                        print(f"👋 Saliendo del sistema...")
                        break
                    elif accion == 3:
                        dem.eliminar_empleado(False)
                        print(f"🚀 {tipo_usuario} acción Finalizada...")
                        print(f"👋 Saliendo del sistema...")
                        break
                    else:
                        print("accion no valida2")
                        print("intente de nuevo")
                        elejir_accion(tipo_usuario)
# ---------------------------------------------> FUNCION PARA ESTUDIANTE   
                if tipo_usuario == 'estudiante':
                    if accion == 1:
                        res.registrar_estudiante(False)
                        print(f"🚀 {tipo_usuario} acción Finalizada...")
                        print(f"👋 Saliendo del sistema...")
                        break
                    elif accion == 2:
                        ues.actualizar_estudiante(False)
                        print(f"🚀 {tipo_usuario} acción Finalizada...")
                        print(f"👋 Saliendo del sistema...")
                        break
                    elif accion == 3:
                        des.eliminar_estudiante(False)
                        print(f"🚀 {tipo_usuario} acción Finalizada...")
                        print(f"👋 Saliendo del sistema...")
                        break
                    else:
                        print("accion no valida3")
                        print("intente de nuevo")
                        elejir_accion(tipo_usuario)
# ------------------------------------------> FUNCION PARA PADRES_ESTUDIANTES
                if tipo_usuario == 'padres':
                    if accion == 1:
                        rpe.registrar_padres_estudiantes(False)
                        print(f"🚀 {tipo_usuario} acción Finalizada...")
                        print(f"👋 Saliendo del sistema...")
                        break
                    elif accion == 2:
                        upe.actualizar_padres_estudiantes(False)
                        print(f"🚀 {tipo_usuario} acción Finalizada...")
                        print(f"👋 Saliendo del sistema...")
                        break
                    elif accion == 3:
                        dpe.eliminar_padres_estudiantes(False)
                        print(f"🚀 {tipo_usuario} acción Finalizada...")
                        print(f"👋 Saliendo del sistema...")
                        break
                    else:
                        print("accion no valida4")
                        print("intente de nuevo")
                        elejir_accion(tipo_usuario)
                else:
                    print(f"🚀 {tipo_usuario} acción Finalizada...")
                    print(f"👋 Saliendo del sistema...")
                    break
                    # print("intente de nuevo")
                    # elejir_accion(tipo_usuario)
            else:
                print("no existe esa accion3")
                break
        except ValueError as e:
            print(f"ingrese un valor valido el error es: {e}")
            print("intente de nuevo")
            elejir_accion(tipo_usuario)

opciones_multiples('empleado')