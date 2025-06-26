#Promedio de Notas

sw = 1
listaNotas = []
try:
    print("Presione 1 para ingresar sus notas: ")
    print("Presione cualquier tecla para salir¡¡¡")
    op = int(input("Seleccione Opción: "))
    if(op == 1):
        while sw == 1:
            try:
                print("-------------------------------------------")
                nota = int(input("Ingrese su nota, si desea salir, presione 0: "))
                if(nota != 0):
                    listaNotas.append(nota)
                    print(f"Sus notas cargadas son: {listaNotas}")
                    print(f"Cantidad de notas cargadas son: {len(listaNotas)}")
                    print(f"Su promedio de notas es: {sum(listaNotas)/len(listaNotas)}")
                else:
                    print("Adiós¡¡¡¡")
                    sw=0    
            except:
                print("Ingreso Erróneo")
    else:
        print("Adiós¡¡¡") 
except:
    print("dsadsadasdsa")