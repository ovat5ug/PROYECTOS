def ciclo_numerico():
    cantidad_de_numeros = int(input("introdusca la cantidad de numeros que va a usar: "))
    lista =[]
    for i in range(cantidad_de_numeros):        
        numero = float(input("introdusca valor numerico: "))
        lista.append(numero)      
    return lista[:]

def tSumar():
    return print(sum(ciclo_numerico()))

def tRestar():
    # return sum(ciclo_numerico())*-1 # Resumen del codigo de abajo
    cantidad_de_numeros = int(input("introdusca la cantidad de numeros que va a usar: "))
    lista =[]
    for i in range(cantidad_de_numeros):        
        numero = float(input("introdusca valor numerico: "))
        a=0
        numero = a - numero
        lista.append(numero)      
    return print(sum(lista[:]))

def tProducto():    
    cantidad_de_numeros = int(input("introdusca la cantidad de numeros que va a usar: "))
    lista =[]
    a=1
    for i in range(cantidad_de_numeros):        
        numero = float(input("introdusca valor numerico: "))        
        numero = a * numero
        a= numero
        lista.append(numero)      
    return print(lista[-1])

def tDivision():
    lista=ciclo_numerico()
    n = 1
    numerador=lista[0]
    for i in lista[:-1]: #  t0dos los datos de la cadena menos uno
                         #  L[0]/L[1] R/L[2] R/L[3]     
         resultado = numerador / lista[n] 
        #  print(f"{resultado}") TEST
         n = n+1
         numerador=resultado
    return print(resultado)

def operaciones_aritmeticas():        
    while True:
                print("\n📌 MENÚ:")
                print("1️⃣ Sumar")
                print("2️⃣ Restar")
                print("3️⃣ Multiplicar")
                print("3️⃣ Dividirr")
                opcion = input("\nSeleccione una opción: ")

                if opcion == "1":                     
                    return tSumar()
                if opcion == "2": 
                    return tRestar()
                if opcion == "3":
                    return tProducto()                 
                if opcion == "4":
                    return tDivision() 
                else:
                     print(f"la opcion: '{opcion}' introducida no esta dentro del rango de opciones")

# operaciones_aritmeticas()
# print(tSumar())
# print(tRestar())
# print(tProducto())
# print(tDivision())