"""🔸 1. Sistema de Registro de Estudiantes
Funciones:

Registrar estudiante: nombre, RUT, carrera.

Consultar estudiante por RUT.

Eliminar estudiante.

Mostrar todos los estudiantes.

Validaciones:

Que el RUT no se repita.

Que el nombre no esté vacío."""

def main():
    estudiantes = {}
    while True:
        print("\n🎓 MENÚ ESTUDIANTES")
        print("1. Registrar estudiante")
        print("2. Consultar estudiante")
        print("3. Eliminar estudiante")
        print("4. Mostrar todos")
        print("5. Salir")

        opcion = input("Ingrese opción: ")
        if opcion == "1":
            registrar(estudiantes)
        elif opcion == "2":
            consultar(estudiantes)
        elif opcion == "3":
            eliminar(estudiantes)
        elif opcion == "4":
            mostrar(estudiantes)
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")

def registrar(estudiantes):
    rut = input("Ingrese RUT: ").strip()
    if rut in estudiantes:
        print("RUT ya registrado.")
        return
    nombre = input("Ingrese nombre: ").strip()
    carrera = input("Ingrese carrera: ").strip()
    estudiantes[rut] = {"nombre": nombre, "carrera": carrera}
    print("Estudiante registrado.")

def consultar(estudiantes):
    rut = input("Ingrese RUT: ").strip()
    if rut in estudiantes:
        print(estudiantes[rut])
    else:
        print("No encontrado.")

def eliminar(estudiantes):
    rut = input("Ingrese RUT a eliminar: ")
    if rut in estudiantes:
        del estudiantes[rut]
        print("Estudiante eliminado.")
    else:
        print("No encontrado.")

def mostrar(estudiantes):
    if not estudiantes:
        print("No hay registros.")
    for rut, datos in estudiantes.items():
        print(f"{rut}: {datos}")

if __name__ == "__main__":
    main()
