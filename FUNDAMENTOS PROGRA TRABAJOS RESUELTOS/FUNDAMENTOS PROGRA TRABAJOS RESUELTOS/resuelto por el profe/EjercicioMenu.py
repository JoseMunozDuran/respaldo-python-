#Tabla de Multiplicar
'''for n in range(1,11):
    print("----TABLA---",n,"-----")
    for i in range(11):
        resultado = i * n
        print(i,"X", n, "=", resultado)'''

#Menú Opción 1
'''while True:
    print("--Menú Opciones--")
    print("1.- Realizar Opción 1")
    print("2.- Realizar Opción 2")
    print("3.- Salir")
    opcion = input("Seleccione una opción [1 - 3]: ")
    if opcion == "1":
        print("Has Seleccionado la Opción 1: ")
        #Código para esta acción
    elif opcion == "2":
        print("Has Seleccionado la opción 2: ")
        #Código para esta acción
    elif opcion == "3":
        print("Saliendo del Programa")
        break
    else:
        print("Opción Inválida")'''

#Menú Opción 2    
'''sw = 1
while sw == 1:
    print("--Menú Opciones--")
    print("1.- Realizar Opción 1")
    print("2.- Realizar Opción 2")
    print("3.- Salir")
    try:
        op = int(input("Seleccione una opción: "))
        if(op > 0 and op < 4):
            if op == 1:
                print("Has Seleccionado la Opción 1: ")
                continuar = int(input("Desea Salir 1=Si 2=No"))
                if continuar == 1:
                    print("Adiós")
                    sw = 0
            if op == 2:
                print("Has Seleccionado la Opción 2: ")
                continuar = int(input("Desea Salir 1=Si 2=No"))
                if continuar == 1:
                    print("Adiós")
                    sw = 0
            if op == 3:
                print("Saliendo del Programa")
                sw = 0
    except ValueError:
        print("Ingreso Erróneo")'''
#Menú Opción 3
op = 1
while op != 3:
    print("--Menú Opciones--")
    print("1.- Realizar Opción 1")
    print("2.- Realizar Opción 2")
    print("3.- Salir")
    op = int(input("Ingrese su Opcíon [1 - 3]: "))
    if op == 1:
        print("Has Seleccionado la Opción 1: ")
        print("")
        #Código para esta acción
    elif op == 2:
        print("Has Seleccionado la Opción 2: ")
        print("")
        #Código para esta acción
    elif op == 3:
        print("Ha Selecionado Salir")
        print("")
    else:
        print("Ingreso opción inválida")



