"""🔸 9. Control de Notas
Datos: nombre estudiante, lista de 3 notas.

Funciones:

Agregar estudiante con notas.

Calcular promedio.

Mostrar aprobados (promedio ≥ 4.0).

Eliminar estudiante."""

def main():
    notas = {}
    while True:
        print("\n📚 CONTROL DE NOTAS")
        print("1. Agregar estudiante")
        print("2. Ver promedio")
        print("3. Mostrar aprobados")
        print("4. Eliminar estudiante")
        print("5. Salir")

        op = input("Opción: ")
        if op == "1":
            agregar(notas)
        elif op == "2":
            promedio(notas)
        elif op == "3":
            aprobados(notas)
        elif op == "4":
            eliminar(notas)
        elif op == "5":
            break
        else:
            print("Opción inválida")

def agregar(notas):
    nombre = input("Nombre: ")
    if nombre in notas:
        print("Ya existe.")
        return
    try:
        n1 = float(input("Nota 1: "))
        n2 = float(input("Nota 2: "))
        n3 = float(input("Nota 3: "))
        if all(1.0 <= n <= 7.0 for n in [n1, n2, n3]):
            notas[nombre] = [n1, n2, n3]
            print("Notas registradas.")
        else:
            print("Notas fuera de rango.")
    except:
        print("Entrada inválida.")

def promedio(notas):
    nombre = input("Estudiante: ")
    if nombre in notas:
        prom = sum(notas[nombre]) / 3
        print(f"Promedio: {prom:.2f}")
    else:
        print("No registrado.")

def aprobados(notas):
    for nombre, n in notas.items():
        prom = sum(n) / 3
        if prom >= 4.0:
            print(f"{nombre}: {prom:.2f} ✅")

def eliminar(notas):
    nombre = input("Eliminar estudiante: ")
    if nombre in notas:
        del notas[nombre]
        print("Eliminado.")
    else:
        print("No existe.")

if __name__ == "__main__":
    main()
