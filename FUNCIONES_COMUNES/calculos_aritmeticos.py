def ciclo_numerico():
    while True:  # Se repetirá hasta que se obtengan datos válidos
        try:
            cantidad_de_numeros = int(input("Introduzca la cantidad de números que va a usar: "))
            lista = []
            for i in range(cantidad_de_numeros):        
                numero = float(input("Introduzca valor numérico: "))
                lista.append(numero)      
            return lista  # Si todo va bien, retornamos la lista
        except ValueError as e:   
            print("⚠️ Error: Ingrese un número válido.")
            print(f"⚠️ Error: {type(e).__name__}")            

def tSumar():
    lista=ciclo_numerico()
    return print(f"con los numeros introducidos: {lista} el resultado de la suma es: {sum(lista)}"),operaciones_aritmeticas()

def tRestar():
    # return sum(ciclo_numerico())*-1 # Resumen del codigo de abajo
    lista=ciclo_numerico()
    if not lista or len(lista)==1:  # Si la lista es vacía, None o solo tiene un dato, mostramos un error
        print(f'⚠️ Error: no introdujo algun dato o solo ingreso uno. dato ingresado fue: "{lista[0]}"')
        print("Intente de nuevo hacer la resta, introduzca un minimo de dos numeros")
        tRestar()
        return  # Salimos de la función sin ejecutar el bucle    
    n = 1
    numerador=-lista[0] #----> 1
    for i in lista[:-1]: #[2.0, 4.0, 6.0, 8.0]
        #                    2-4
        #                    r-6
        #                    r-8
        resultado = (numerador) - (lista[n])
        n = n+1
        numerador=resultado
    return print(f"con los numeros introducidos: {lista} el resultado de la resta es: {resultado}"),operaciones_aritmeticas()

def tProducto():
    while True:  # Se repetirá hasta que se obtengan datos válidos
        try:
            cantidad_de_numeros = int(input("introdusca la cantidad de numeros que va a usar: "))
            if cantidad_de_numeros >= 2:
                lista_resultados = []
                lista = list()
                a=1
                for i in range(cantidad_de_numeros):
                    try:                                    
                        numero = float(input("introdusca valor numerico: "))
                        lista.append(numero)        
                        numero = a * numero
                        a = numero
                        lista_resultados.append(numero)
                    except ValueError:
                        print("⚠️ Error: Ingrese un númersso válido.")
                        return  # Sale de la función si hay un error en la entrada de datos     
                return print(f"con los numeros introducidos: {lista} el resultado del producto es: {lista_resultados[-1]}"),operaciones_aritmeticas()
            else:
                print(f'⚠️ Error: no introdujo algun dato o solo ingreso un dato')
                print("Intente de nuevo hacer el producto, introduzca un minimo de dos numeros")
                tProducto()
        except ValueError as e:   
            print("⚠️ Error: Ingrese un número válido.")
            print(f"Error: {type(e).__name__}")     

def tDivision():
    while True:
        try:
            lista=ciclo_numerico()
            if not lista or len(lista)==1:  # Si la lista es vacía o None, mostramos un error
                print(f"⚠️ Error: no introdujo algun dato o solo ingreso un dato. y el dato que introdujo es: {lista}")
                return  tDivision()# Salimos de la función sin ejecutar el bucle            
            n = 1
            numerador=lista[0]
            for i in lista[:-1]: #[2.0, 4.0, 6.0, 8.0]
                #                    2/4
                #                    r/6
                #                    r/8
                resultado = numerador / lista[n] 
                #  print(f"sale resultado: {resultado}") # TEST
                n = n+1
                numerador=resultado
            return print(f"con los numeros introducidos: {lista} el resultado de la Division es: {resultado}"),operaciones_aritmeticas()
        except ZeroDivisionError as e:# error si el valor es cero   
            print("ingresa un numero valido")
            print(f"El error es: {type(e).__name__}")

def operaciones_aritmeticas():        
    while True:
                print("\n📌 MENÚ:")
                print("1️⃣ Sumar")
                print("2️⃣ Restar")
                print("3️⃣ Multiplicar")
                print("4️⃣ Dividir")
                print("5️⃣ Salir")
                opcion = input("\nSeleccione una opción: ")

                if opcion == "1":                     
                    return tSumar()
                elif opcion == "2": 
                    return tRestar()
                elif opcion == "3":
                    return tProducto()                 
                elif opcion == "4":
                    return tDivision()
                elif opcion == "5":
                    print("\n👋 Saliendo de Operaciones aritmeticas")
                    break 
                else:
                     print(f"la opcion: '{opcion}' introducida no esta dentro del rango de opciones")

# operaciones_aritmeticas()
# ciclo_numerico()
# print(tSumar())
# print(tRestar())
# print(tProducto())
# print(tDivision())s




