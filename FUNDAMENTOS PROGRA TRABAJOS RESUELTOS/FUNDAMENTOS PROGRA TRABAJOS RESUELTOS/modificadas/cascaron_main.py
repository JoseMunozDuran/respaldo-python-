def main():
    entradas = {}
    while True:
        print("\nMENU PRINCIPAL")
        print("-----------------")
        print("1.- Comprar pasajes.")
        print("2.- Consultar Comprador.")
        print("3.- Cancelar compra.")
        print("4.- Salir.")
        print("-----------------")
        opcion = input("Ingrese Opción: ")

        if opcion == "1":
            comprar_pasajes(entradas)
        elif opcion == "2":
            consultar_comprador(entradas)
        elif opcion == "3":
            cancelar_compra(entradas)
        elif opcion == "4":
            print("Programa terminado....")
            break
        else:
            print("Debe ingresar opción válida¡¡¡")

def comprar_pasajes(entradas):
    print("Seleccionaste comprar entradas")



def consultar_comprador(entradas):
    print("Seleccionaste consultar")

def cancelar_compra(entradas):
    print("Seleccionaste cancelar compra")    


if __name__ == "__main__":
    main()