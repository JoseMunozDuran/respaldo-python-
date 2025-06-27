"""🔸 8. Agenda Telefónica
Datos: nombre, número.

Funciones:

Agregar contacto.

Consultar por nombre.

Modificar número.

Eliminar contacto.

Validaciones:

Número debe tener 9 dígitos."""

def main():
    agenda = {}
    while True:
        print("\n📞 AGENDA")
        print("1. Agregar contacto")
        print("2. Consultar contacto")
        print("3. Modificar número")
        print("4. Eliminar contacto")
        print("5. Salir")

        opcion = input("Opción: ")
        if opcion == "1":
            agregar(agenda)
        elif opcion == "2":
            consultar(agenda)
        elif opcion == "3":
            modificar(agenda)
        elif opcion == "4":
            eliminar(agenda)
        elif opcion == "5":
            print("Chao!")
            break
        else:
            print("Opción inválida.")

def agregar(agenda):
    nombre = input("Nombre: ")
    if nombre in agenda:
        print("Ya existe.")
        return
    numero = input("Número (9 dígitos): ")
    if numero.isdigit() and len(numero) == 9:
        agenda[nombre] = numero
        print("Contacto agregado.")
    else:
        print("Número inválido.")

def consultar(agenda):
    nombre = input("Nombre: ")
    if nombre in agenda:
        print(f"📱 {agenda[nombre]}")
    else:
        print("No encontrado.")

def modificar(agenda):
    nombre = input("Nombre: ")
    if nombre in agenda:
        nuevo = input("Nuevo número (9 dígitos): ")
        if nuevo.isdigit() and len(nuevo) == 9:
            agenda[nombre] = nuevo
            print("Número actualizado.")
        else:
            print("Número inválido.")
    else:
        print("No existe el contacto.")

def eliminar(agenda):
    nombre = input("Nombre a eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print("Contacto eliminado.")
    else:
        print("No existe.")

if __name__ == "__main__":
    main()
