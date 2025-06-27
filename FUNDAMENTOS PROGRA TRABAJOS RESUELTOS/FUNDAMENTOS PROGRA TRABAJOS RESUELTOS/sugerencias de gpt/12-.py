"""🔸 2. Reserva de Asientos en un Cine
Funciones:

Reservar asiento (A1, A2, ..., B1, B2…).

Ver asientos disponibles.

Cancelar reserva.

Salir."""

#Estructura sugerida:

#asientos = {"A1": None, "A2": None, "B1": None}

#🧩 10. Sistema de Reserva de Asientos en un Cine
#🎯 Objetivo:
#Reservar asientos (por ejemplo: A1, A2, B1, B2...).

#Ver disponibilidad.

#Cancelar reserva.

#Mostrar ocupación.

#🧠 Lógica:
#Usamos un diccionario asientos donde cada asiento es una clave ("A1", "A2", etc.), y su valor es None si está libre, o el nombre del cliente si está reservado.



def main():
    asientos = {
        "A1": None, "A2": None, "A3": None,
        "B1": None, "B2": None, "B3": None,
        "C1": None, "C2": None, "C3": None
    }

    while True:
        print("\n🎬 MENÚ CINE")
        print("1. Reservar asiento")
        print("2. Ver disponibilidad")
        print("3. Cancelar reserva")
        print("4. Ver ocupación")
        print("5. Salir")

        opcion = input("Seleccione opción: ")
        if opcion == "1":
            reservar_asiento(asientos)
        elif opcion == "2":
            ver_disponibles(asientos)
        elif opcion == "3":
            cancelar_reserva(asientos)
        elif opcion == "4":
            ver_ocupacion(asientos)
        elif opcion == "5":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción inválida.")

def reservar_asiento(asientos):
    ver_disponibles(asientos)
    asiento = input("Ingrese código de asiento a reservar (Ej: A1): ").upper()
    if asiento in asientos:
        if asientos[asiento] is None:
            nombre = input("Ingrese nombre del comprador: ").strip()
            if nombre:
                asientos[asiento] = nombre
                print(f"✅ Asiento {asiento} reservado para {nombre}.")
            else:
                print("Nombre no puede estar vacío.")
        else:
            print("❌ Asiento ya reservado.")
    else:
        print("Código de asiento inválido.")

def ver_disponibles(asientos):
    print("\n🪑 Asientos disponibles:")
    for fila in ["A", "B", "C"]:
        fila_asientos = [f"{fila}{n}" for n in range(1, 4)]
        print(fila, end=": ")
        for codigo in fila_asientos:
            estado = "✅" if asientos[codigo] is None else "❌"
            print(f"{codigo}{estado}", end="  ")
        print()

def cancelar_reserva(asientos):
    asiento = input("Ingrese asiento a cancelar (Ej: B2): ").upper()
    if asiento in asientos:
        if asientos[asiento] is not None:
            print(f"Reserva de {asientos[asiento]} cancelada.")
            asientos[asiento] = None
        else:
            print("Ese asiento no está reservado.")
    else:
        print("Asiento no válido.")

def ver_ocupacion(asientos):
    print("\n📋 Asientos ocupados:")
    ocupados = {k: v for k, v in asientos.items() if v is not None}
    if not ocupados:
        print("No hay asientos reservados.")
    else:
        for asiento, nombre in ocupados.items():
            print(f"{asiento}: {nombre}")

if __name__ == "__main__":
    main()
