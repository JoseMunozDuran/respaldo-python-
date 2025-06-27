print("---BIENVENIDO AL SISTEMA DE VENTAS CINE DUOC")

continuar = True
while continuar:
    try:
        #Pregunta si pertenece a Duoc
        respuesta = input("\n¿El Cliente Pertenece a Duoc? (si/no): ").strip().lower()
        pertenece_duoc = respuesta == "si"

        #Menú de entradas 
        while True:
            print("\n-----Tipos de Entradas-----")
            print("A) Estreno -> $4.800")
            print("B) Normal  -> $2.900")
            opcion_entrada = input("Seleccione una opción: ").strip().upper()

            if opcion_entrada == "A":
                precio_entrada = 4800
                break
            elif opcion_entrada == "B":
                precio_entrada = 2900
                break
            else: 
                print("Opción no Válida. Intente Nuevamente¡¡¡¡")
        
        while True:
            try:
                cantidad_entrada = int(input("Ingrese la cantidad de entradas: "))
                if cantidad_entrada > 0:
                    break
                else:
                    print("Debe ingresar una cantidad mayor que 0.¡¡¡¡")    
            except ValueError:
                print("Entrada Inválida. Debe ingresar un número¡¡¡")   

        total_entradas = precio_entrada * cantidad_entrada

        #Descuento si pertenece a Duoc
        if pertenece_duoc:
            descuento = total_entradas  * 0.30
            total_entradas -= descuento
            print(f"Descuento Aplicado: $ {descuento:.0f}")
            #Supongamos que descuento dió en total $7895.50 con .0f quedá redondeado a 7896
        else:
            print("NO se aplica descuento")

        #Palomitas
        total_palomitas = 0
        respuesta_palomita = input("¿Desea agregar palomitas? (si/no): ").strip().lower()
        #Strip función que permite eliminar espacio al principio y fin del ingreso
        if respuesta_palomita == "si":
            while True:
                print("\n----Tipos de Palomitas-----")        
                print("A) Pequeña ->  $2.500")
                print("B) Mediana ->  $4.500")
                print("C) Grande  ->  $7.800")
                opcion_palomitas = input("Seleccione una opción: ").strip().upper()

                if opcion_palomitas == "A":
                    precio_palomitas = 2500
                    break
                elif opcion_palomitas == "B":
                    precio_palomitas = 4500
                    break
                elif opcion_palomitas == "C":
                    precio_palomitas = 7800
                    break
                else:
                    print("Opción no Válida. Intente Nuevamente¡¡¡¡")

            while True:
                try:
                    cantidad_palomitas = int(input("Ingrese la cantidad de Palomitas: "))
                    if cantidad_palomitas > 0:
                        break
                    else:
                        print("Debe ingresar una cantidad mayor a 0¡¡¡¡")
                except ValueError:
                    print("Entrada Inválida. Debe ingresar un número¡¡¡")
            
            total_palomitas = precio_palomitas * cantidad_palomitas

        #Bebidas
        total_bebidas = 0
        respuesta_bebidas = input("¿Desea agregar bebidas? (si /no ): ").strip().lower()
        if respuesta_bebidas == "si":
            while True:
                print("\n----Tipos de Bebidas-----")        
                print("A) Bebida Pequeña ->  $1.000")
                print("B) Bebida Mediana ->  $1.250")
                print("C) Bebida Grande  ->  $2.000")
                opcion_bebidas = input("Seleccione una opción: ").strip().upper()

                if opcion_bebidas == "A":
                    precio_bebida = 1000
                    break
                elif opcion_bebidas == "B":
                    precio_bebida = 1250
                    break
                elif opcion_bebidas == "C":
                    precio_bebida = 2000
                    break
                else:
                    print("Opción no válida. Intente Nuevamente¡¡¡¡")

            while True:
                try:
                    cantidad_bebidas = int(input("Ingrese la cantidad de Bebidas: "))
                    if cantidad_bebidas > 0:
                        break
                    else:
                        print("Debe ingresar una cantidad mayor a 0¡¡¡¡")
                except ValueError:
                    print("Entrada Inválida. Debe ingresar un número¡¡¡")  

            total_bebidas = precio_bebida * cantidad_bebidas

        #Cálculo del total
        total_a_pagar = total_entradas + total_palomitas + total_bebidas
        print(f"\nTotal a Pagar: ${total_a_pagar:.0f}")

        #Cobro y vuelto
        while True:
            try:
                efectivo = int(input("Ingrese el efectivo entregado por el cliente $: "))
                if efectivo >= total_a_pagar:
                    break
                else:
                    print("El efectivo ingresado es insuficiente. Intente Nuevamente")
            except ValueError:
                print("Entrada inválida. Debe ingresar un número") 
        
        vuelto = efectivo - total_a_pagar
        print(f"Vuelto a Entregar:  ${vuelto}")

        #Preguntar si desea realizar otra compra
        respuesta = input("\n¿Desea Realizar otra compra? (si/no): ").strip().lower()
        if respuesta != "si":
            continuar = False
            print("Gracias por usar el sistema bkn de venta de entradas Cine Duoc.")
    except Exception as e:
        print(f"Ocurrio un Error inesperado:  {e}")
        print("Reiniciando Venta....\n")