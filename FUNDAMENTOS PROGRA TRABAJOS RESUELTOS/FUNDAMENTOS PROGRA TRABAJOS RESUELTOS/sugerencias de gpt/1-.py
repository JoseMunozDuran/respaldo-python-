"""SUGERENCIA DE ESTRUCTURA BASE EN VS CODE"""

def main():
    base_datos = {}
    while True:
        print("1. Agregar")
        print("2. Consultar")
        print("3. Eliminar")
        print("4. Salir")
        opcion = input("Seleccione opción: ")
        if opcion == "1":
            agregar(base_datos)
        elif opcion == "2":
            consultar(base_datos)
        elif opcion == "3":
            eliminar(base_datos)
        elif opcion == "4":
            print("Adiós!")
            break
        else:
            print("Opción inválida.")

# Las funciones agregar, consultar, eliminar deben estar definidas aquí

if __name__ == "__main__":
    main()
