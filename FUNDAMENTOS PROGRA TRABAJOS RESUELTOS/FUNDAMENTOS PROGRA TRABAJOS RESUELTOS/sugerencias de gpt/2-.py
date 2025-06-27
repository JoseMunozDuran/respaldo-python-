"""🧪 EJERCICIO: Sistema de Registro de Libros en Biblioteca
🎯 Objetivo:
Registrar libros con título, autor y año de publicación. Permitir consultar libros por título, eliminar libros y mostrar todos los registrados."""

"""📝 Requisitos:
Cada libro debe tener:

Título (clave)

Autor

Año de publicación (número entero, mayor a 0)

Validar que:

No se repita el título.

El año sea válido."""

def main():
    biblioteca = {}
    while True:
        print("\n📚 MENÚ BIBLIOTECA")
        print("1. Registrar libro")
        print("2. Consultar libro")
        print("3. Eliminar libro")
        print("4. Mostrar todos los libros")
        print("5. Salir")

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            registrar_libro(biblioteca)
        elif opcion == "2":
            consultar_libro(biblioteca)
        elif opcion == "3":
            eliminar_libro(biblioteca)
        elif opcion == "4":
            mostrar_todos(biblioteca)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("⚠️ Opción inválida.")


def registrar_libro(biblioteca):
    titulo = input("Ingrese título del libro: ").strip()
    if titulo in biblioteca:
        print("⚠️ Libro ya registrado.")
        return

    autor = input("Ingrese autor: ").strip()
    try:
        año = int(input("Ingrese año de publicación: "))
        if año <= 0:
            print("⚠️ Año inválido.")
            return
    except ValueError:
        print("⚠️ Año inválido (debe ser número).")
        return

    biblioteca[titulo] = {"autor": autor, "año": año}
    print("✅ Libro registrado con éxito.")


def consultar_libro(biblioteca):
    titulo = input("Ingrese título a consultar: ").strip()
    if titulo in biblioteca:
        datos = biblioteca[titulo]
        print(f"📘 Autor: {datos['autor']}, Año: {datos['año']}")
    else:
        print("⚠️ Libro no encontrado.")


def eliminar_libro(biblioteca):
    titulo = input("Ingrese título a eliminar: ").strip()
    if titulo in biblioteca:
        del biblioteca[titulo]
        print("🗑️ Libro eliminado.")
    else:
        print("⚠️ Libro no encontrado.")


def mostrar_todos(biblioteca):
    if not biblioteca:
        print("📭 No hay libros registrados.")
        return
    print("\n📚 Libros registrados:")
    for titulo, datos in biblioteca.items():
        print(f"📘 {titulo} - Autor: {datos['autor']}, Año: {datos['año']}")


if __name__ == "__main__":
    main()
