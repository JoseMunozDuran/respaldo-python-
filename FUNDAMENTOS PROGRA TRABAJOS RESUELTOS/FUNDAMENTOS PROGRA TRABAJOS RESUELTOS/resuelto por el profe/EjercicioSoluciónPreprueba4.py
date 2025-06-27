def main():
    entradas = {}
    while True:
        print("\nMENU PRINCIPAL")
        print("-----------------")
        print("1.- Comprar entradas.")
        print("2.- Consultar Comprador.")
        print("3.- Cancelar compra.")
        print("4.- Salir.")
        print("-----------------")
        opcion = input("Ingrese Opción: ")

        if opcion == "1":
            comprar_entradas(entradas)
        elif opcion == "2":
            consultar_comprador(entradas)
        elif opcion == "3":
            cancelar_compra(entradas)
        elif opcion == "4":
            print("Programa terminado....")
            break
        else:
            print("Debe ingresar opción válida¡¡¡")

def comprar_entradas(entradas):
    while True:
        nombre = input("Ingrese nombre de comprador: ")
        if nombre not in entradas:
            break
        else:
            print("Comprador Ya Registrado. Intente con otro Nombre¡¡")
            
    while True:
        tipo = input("Ingrese tipo de entrada [G/V]").upper()
        if tipo in ("G", "V"):
            break
        else:
            print("Tipo Inválido. Ingrese G para General o V para VIP. Intente nuevamente")
    while True:
        codigo = input("Ingrese código de confirmación (6 dígitos, al menos una mayuscula y al menos un numero):  ")
        tiene_mayus = any(i.isupper() for i in codigo)
        tiene_num   = any(i.isdigit() for i in codigo)
        sin_espacio = " " not in codigo
        if len(codigo) >= 6 and tiene_mayus and tiene_num and sin_espacio:
            print("Código validado")
            break
        else:
            print("Código no válido. Intente nuevamente.")
    
    entradas[nombre] = {"tipo": tipo, "codigo": codigo}
    print("¡Entrada registrada conéxito¡¡¡")


def consultar_comprador(entradas):
    nombre = input("Ingrese nombre del comprador a buscar: ")
    if nombre in entradas:
        info = entradas[nombre]
        print(f"Tipo de entrada: {info['tipo']}, Codigo: {info['codigo']}")
    else:
        print("EL comprador no se encuentra")

def cancelar_compra(entradas):
    nombre = input("Ingrese nombre del comprador a Cancelar: ")
    if nombre in entradas:
        del entradas[nombre]
        print("¡Compra Cancelada¡¡")
    else:
        print("No se pudo cancelar la compra")    


if __name__ == "__main__":
    main()