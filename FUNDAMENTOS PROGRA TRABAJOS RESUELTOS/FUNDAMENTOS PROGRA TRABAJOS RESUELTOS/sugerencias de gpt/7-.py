"""🔸 6. Simulación de Cajero Automático
Datos: nombre, saldo.

Funciones:

Crear cuenta.

Depositar dinero.

Retirar dinero.

Consultar saldo.

Validaciones:

No permitir saldo negativo.

No permitir duplicados en nombre."""

def main():
    cuentas = {}
    while True:
        print("\n🏦 MENÚ CAJERO")
        print("1. Crear cuenta")
        print("2. Depositar")
        print("3. Retirar")
        print("4. Consultar saldo")
        print("5. Salir")

        opcion = input("Opción: ")
        if opcion == "1":
            crear(cuentas)
        elif opcion == "2":
            depositar(cuentas)
        elif opcion == "3":
            retirar(cuentas)
        elif opcion == "4":
            consultar(cuentas)
        elif opcion == "5":
            print("Adiós.")
            break
        else:
            print("Opción inválida.")

def crear(cuentas):
    nombre = input("Nombre: ")
    if nombre in cuentas:
        print("Ya existe.")
        return
    cuentas[nombre] = 0
    print("Cuenta creada.")

def depositar(cuentas):
    nombre = input("Nombre: ")
    if nombre in cuentas:
        try:
            monto = float(input("Monto a depositar: "))
            if monto > 0:
                cuentas[nombre] += monto
                print("Depósito realizado.")
            else:
                print("Monto debe ser mayor a 0.")
        except:
            print("Debe ingresar número.")
    else:
        print("No existe la cuenta.")

def retirar(cuentas):
    nombre = input("Nombre: ")
    if nombre in cuentas:
        try:
            monto = float(input("Monto a retirar: "))
            if 0 < monto <= cuentas[nombre]:
                cuentas[nombre] -= monto
                print("Retiro exitoso.")
            else:
                print("Fondos insuficientes o monto inválido.")
        except:
            print("Debe ingresar número.")
    else:
        print("No existe la cuenta.")

def consultar(cuentas):
    nombre = input("Nombre: ")
    if nombre in cuentas:
        print(f"Saldo: ${cuentas[nombre]:,.0f}")
    else:
        print("No existe la cuenta.")

if __name__ == "__main__":
    main()
