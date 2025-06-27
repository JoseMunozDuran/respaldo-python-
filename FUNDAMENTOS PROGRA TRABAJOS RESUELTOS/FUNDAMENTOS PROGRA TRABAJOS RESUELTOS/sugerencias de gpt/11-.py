"""🔸 10. Gestión de Turnos Médicos
Datos: nombre paciente, especialidad, hora.

Funciones:

Agendar turno.

Consultar turno.

Cancelar turno.

Ver todos los turnos.

Validaciones:

No repetir nombre.

Validar hora en formato HH:MM."""

def main():
    turnos = {}
    while True:
        print("\n🏥 TURNOS MÉDICOS")
        print("1. Agendar turno")
        print("2. Consultar turno")
        print("3. Cancelar turno")
        print("4. Ver todos los turnos")
        print("5. Salir")

        op = input("Opción: ")
        if op == "1":
            agendar(turnos)
        elif op == "2":
            consultar(turnos)
        elif op == "3":
            cancelar(turnos)
        elif op == "4":
            ver_todos(turnos)
        elif op == "5":
            break
        else:
            print("Opción inválida")

def agendar(turnos):
    nombre = input("Nombre paciente: ")
    if nombre in turnos:
        print("Ya tiene turno.")
        return
    especialidad = input("Especialidad: ")
    hora = input("Hora (HH:MM): ")
    if ":" in hora and len(hora) == 5:
        turnos[nombre] = {"especialidad": especialidad, "hora": hora}
        print("Turno agendado.")
    else:
        print("Hora inválida.")

def consultar(turnos):
    nombre = input("Paciente: ")
    if nombre in turnos:
        print(turnos[nombre])
    else:
        print("No tiene turno.")

def cancelar(turnos):
    nombre = input("Cancelar turno de: ")
    if nombre in turnos:
        del turnos[nombre]
        print("Turno cancelado.")
    else:
        print("No existe.")

def ver_todos(turnos):
    if not turnos:
        print("No hay turnos.")
    for nombre, datos in turnos.items():
        print(f"{nombre} - {datos['especialidad']} a las {datos['hora']}")

if __name__ == "__main__":
    main()
