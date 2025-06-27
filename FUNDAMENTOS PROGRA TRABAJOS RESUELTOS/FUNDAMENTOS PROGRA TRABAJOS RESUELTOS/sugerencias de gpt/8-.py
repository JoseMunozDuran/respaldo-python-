"""🔸 7. Sistema de Control de Asistencia
Datos: nombre alumno, presente o ausente.

Funciones:

Marcar asistencia.

Ver asistencia general.

Consultar asistencia de un alumno."""

def main():
    asistencia = {}
    while True:
        print("\n📝 ASISTENCIA")
        print("1. Marcar asistencia")
        print("2. Ver asistencia")
        print("3. Consultar alumno")
        print("4. Salir")

        op = input("Opción: ")
        if op == "1":
            marcar(asistencia)
        elif op == "2":
            mostrar(asistencia)
        elif op == "3":
            consultar(asistencia)
        elif op == "4":
            break
        else:
            print("Inválido")

def marcar(asistencia):
    nombre = input("Nombre alumno: ")
    estado = input("¿Presente o Ausente?: ").capitalize()
    if estado in ["Presente", "Ausente"]:
        asistencia[nombre] = estado
        print("Asistencia registrada.")
    else:
        print("Estado inválido.")

def mostrar(asistencia):
    if not asistencia:
        print("Nada registrado.")
    for nombre, estado in asistencia.items():
        print(f"{nombre}: {estado}")

def consultar(asistencia):
    nombre = input("Alumno: ")
    if nombre in asistencia:
        print(f"{nombre}: {asistencia[nombre]}")
    else:
        print("No registrado.")

if __name__ == "__main__":
    main()
