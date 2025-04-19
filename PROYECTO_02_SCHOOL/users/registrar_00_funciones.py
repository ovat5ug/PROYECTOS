import random

def elegir_numero_azar(inicio, fin):
    return random.randint(inicio, fin)
def grado():
    grado = input("ingrese el grado: ").strip().lower()  
    if grado == 'Primero' or grado == '1':
        numero_aleatorio = elegir_numero_azar(1, 2)
        id_grado=numero_aleatorio
    elif grado == 'Segundo' or grado == '2':
        numero_aleatorio = elegir_numero_azar(3, 4)
        id_grado=numero_aleatorio
    elif grado == 'Tercero' or grado == '3':
        numero_aleatorio = elegir_numero_azar(5, 6)
        id_grado=numero_aleatorio
    elif grado == 'Cuarto' or grado == '4':
        numero_aleatorio = elegir_numero_azar(7, 8)
        id_grado=numero_aleatorio
    elif grado == 'Quinto' or grado == '5':
        numero_aleatorio = elegir_numero_azar(9, 10)
        id_grado=numero_aleatorio
    elif grado == 'Sexto' or grado == '6':
        numero_aleatorio = elegir_numero_azar(11, 12)
        id_grado=numero_aleatorio
    elif grado == 'Septimo' or grado == '7':
        numero_aleatorio = elegir_numero_azar(13, 14)
        id_grado=numero_aleatorio
    elif grado == 'Octavo' or grado == '8':
        numero_aleatorio = elegir_numero_azar(15, 16)
        id_grado=numero_aleatorio
    elif grado == 'Noveno' or grado == '9':
        numero_aleatorio = elegir_numero_azar(17, 18)
        id_grado=numero_aleatorio
    elif grado == 'Bachillerato Primer Año' or grado == '10':
        ingresar_tipo_Bachillerato = input("es Bach. General ingresar uno o es Bach. Tecnico ingresar dos: ").strip().lower()
        if ingresar_tipo_Bachillerato == '1':
            numero_aleatorio = elegir_numero_azar(19, 20)
            id_grado=numero_aleatorio
        elif ingresar_tipo_Bachillerato == '2':
            numero_aleatorio = elegir_numero_azar(23, 24)
            id_grado=numero_aleatorio 
        else: print("Valor ingresado incorrecto")                       
    elif grado == 'Bachillerato Segundo Año' or grado == '11':
        ingresar_tipo_Bachillerato = input("es Bach. General ingresar uno o es Bach. Tecnico ingresar dos: ").strip().lower()
        if ingresar_tipo_Bachillerato == 'general' or ingresar_tipo_Bachillerato == '1':
            numero_aleatorio = elegir_numero_azar(21, 22)
            id_grado=numero_aleatorio
        elif ingresar_tipo_Bachillerato == 'tecnico'  or ingresar_tipo_Bachillerato == '2':
            numero_aleatorio = elegir_numero_azar(25, 26)
            id_grado=numero_aleatorio
        else: print("Valor ingresado incorrecto")
    elif grado == 'Bachillerato Tercer Año' or grado == '12':
        numero_aleatorio = elegir_numero_azar(27, 28)
        id_grado=numero_aleatorio
    else: print("Valor ingresado incorrecto")
    return id_grado 

def genero():
    genero=input("ingrese el genero: ").strip().lower()
    if genero == 'masculino' or genero == 'm' or genero == '1':
        id_genero=1
    elif genero == 'femenino' or genero == 'f' or genero == '2':
        id_genero=2 
    elif genero == 'no definido' or genero == 'n' or genero == '3':
        id_genero=3
    else: print("Valor ingresado incorrecto")
    return id_genero

def nombre_competo():
    nombre=input("Favor ingresar los nombres: ").strip().title().split()
    P_nombre=nombre[0]
    S_nombre=" ".join(nombre[1:])

    apellido=input("Favor ingresar los apellidos: ").strip().title().split()
    P_apellido=apellido[0]
    S_apellido=" ".join(apellido[1:])
    return P_nombre, S_nombre, P_apellido, S_apellido

def cargo():
    cargos_dict = {# cargos_dict es un diccionario que contiene los cargos y sus respectivos ID
        1: "Director", 2: "Subdirector", 3: "Maestro de Matemáticas",
        4: "Maestro de Ciencias", 5: "Maestro de Sociales", 6: "Maestro de Lenguaje",
        7: "Maestro de Inglés", 8: "Bibliotecario", 9: "Secretario", 10: "Tesorero",
        11: "Encargado de Ornato", 12: "Conserje", 13: "Vigilante", 14: "Enfermero",
        15: "Maestro Ciencias Naturales", 16: "Técnico Informático", 17: "Coordinador Académico",
        18: "Coordinador Refrigerio", 19: "Maestro de Arte", 20: "Maestro de Historia",
        21: "Maestro de Educación Física", 22: "Maestro de Idiomas (Francés)", 23: "Maestro de Tecnología",
        24: "Coordinador Cultural", 25: "Ayudante General", 26: "Inspector Escolar",
        27: "Personal de Apoyo", 28: "Encargado de Cafetería", 29: "Asesor Pedagógico",
        30: "Encargado de Materiales", 31: "Operador de Equipo", 32: "Encargado de Recursos Humanos",
        33: "Encargado de Laboratorio", 34: "Contador", 35: "Encargado de Inventario",
        36: "Recepcionista", 37: "Encargado de Transporte", 38: "Auxiliar de Enfermería",
        39: "Asistente Técnico", 40: "Director de Deportes", 41: "Gestor de Actividades",
        42: "Encargado de Talleres", 43: "Profesor de Tecnología", 44: "Coordinador de Cultura",
        45: "Administrador", 46: "Encargado de Suministros", 47: "Encargado de Comunicación",
        48: "Cocinera(o)", 49: "Ayudante de Cocina"
    }

    # Mostrar opciones disponibles
    print("\n📌 Opciones disponibles:")
    for id_cargo, nombre in cargos_dict.items():
        print(f"{id_cargo}: {nombre}")

    cargo_input = input("\nIngrese el número o nombre del cargo: ").strip().title()

    # Validar si es un número
    if cargo_input.isdigit():
        id_cargo = int(cargo_input)
        if id_cargo in cargos_dict:
            return id_cargo
        else:
            print("❌ ID de cargo inválido.")
            return None

    # Validar si es un nombre
    for id_cargo, nombre in cargos_dict.items():
        if cargo_input.lower() == nombre.lower():  # Comparación en minúsculas para evitar problemas de formato
            return id_cargo

    print("❌ Nombre de cargo inválido.")
    return None

def tipo_de_usuario(validacion):
    ti_us_dic = {# ti_us_dic es un diccionario que contiene los tipos de usuario y sus respectivos ID
    1: "Administrador", 2: "regular", 3: "Otros"
    }
    if validacion == "estudiantes" or validacion == "padres":
        id_tipo_usuario = 2
        descripcion = "Regular"
        ti_us_input = "2"
    else:
        print("\n📌 Opciones disponibles:")
        for id_tipo_usuario, descripcion in ti_us_dic.items():
            print(f"{id_tipo_usuario}: {descripcion}")

        ti_us_input = input("\nIngrese el número o nombre del tipo de usuario: ").strip().title()

    # Validar si es un número

    if 0 < ti_us_input.isdigit() <= 3:
        id_tipo_usuario = int(ti_us_input)  # Convertir entrada a entero
        
        # Verificar si el ID está en el diccionario
        if id_tipo_usuario in ti_us_dic:
            return id_tipo_usuario, ti_us_dic[id_tipo_usuario]
        else:
            print("❌ Tipo de Usuario inválido.")
            print("✅ intente nuevamente")        
            return tipo_de_usuario(validacion)
    elif ti_us_input.isalpha():            
        # Validar si es un nombre
        for id_tipo_usuario, descripcion in ti_us_dic.items():
            if ti_us_input.lower() == descripcion.lower():  # Comparación en minúsculas para evitar problemas de formato
                return id_tipo_usuario,descripcion
            else:
                print("❌ Tipo de Usuario inválido.")
                print("✅ intente nuevamente")        
                return tipo_de_usuario(validacion)