"""🔸 3. Sistema de Inscripción a Talleres
Datos del inscrito: nombre, edad, taller (de una lista).

Funciones:

Inscribirse a taller.

Consultar inscrito por nombre.

Ver inscritos por taller.

Eliminar inscripción.

Validaciones:

Edad mínima 15 años.

No repetir nombres."""

def main():
    inscritos = {}
    while True:
        print("\n🧑‍🎨 MENÚ TALLERES")
        print("1. Inscribirse")
        print("2. Consultar inscrito")
        print("3. Ver inscritos por taller")
        print("4. Eliminar inscripción")
        print("5. Salir")

        op = input("Opción: ")
        if op == "1":
            inscribir(inscritos)
        elif op == "2":
            consultar(inscritos)
        elif op == "3":
            por_taller(inscritos)
        elif op == "4":
            eliminar(inscritos)
        elif op == "5":
            break
        else:
            print("Opción inválida.")

def inscribir(inscritos):
    nombre = input("Nombre: ")
    if nombre in inscritos:
        print("Ya inscrito.")
        return
    try:
        edad = int(input("Edad: "))
        if edad < 15:
            print("Debes tener al menos 15 años.")
            return
        taller = input("Taller (Arte, Música, Deportes): ").capitalize()
        if taller not in ["Arte", "Música", "Deportes"]:
            print("Taller no válido.")
            return
        inscritos[nombre] = {"edad": edad, "taller": taller}
        print("Inscripción exitosa.")
    except:
        print("Edad inválida.")

def consultar(inscritos):
    nombre = input("Nombre: ")
    if nombre in inscritos:
        print(inscritos[nombre])
    else:
        print("No inscrito.")

def por_taller(inscritos):
    taller = input("Taller a buscar: ").capitalize()
    for nombre, datos in inscritos.items():
        if datos["taller"] == taller:
            print(f"{nombre} - {datos['edad']} años")

def eliminar(inscritos):
    nombre = input("Eliminar inscripción de: ")
    if nombre in inscritos:
        del inscritos[nombre]
        print("Eliminado.")
    else:
        print("No existe.")

if __name__ == "__main__":
    main()
