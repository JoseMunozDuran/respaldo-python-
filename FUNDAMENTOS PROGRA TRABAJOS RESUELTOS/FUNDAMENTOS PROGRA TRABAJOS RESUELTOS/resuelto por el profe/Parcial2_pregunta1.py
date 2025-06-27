# Solicitar datos al usuario
quintil = int(input("Ingrese su quintil (1-5): "))
condicion = input("Ingrese su condición laboral (empleado/desempleado): ").strip().lower()
edad = int(input("Ingrese su edad: "))

# Determinar el subsidio base según quintil y condición laboral
if quintil in [1, 2]:
    subsidio = 55000 if condicion == "desempleado" else 45000
elif quintil == 3:
    subsidio = 35000 if condicion == "desempleado" else 25000
else:
    subsidio = 0  # No hay subsidio para quintiles 4 y 5

# Aplicar bonos adicionales
if quintil in [1, 2]:
    subsidio += 15000
if quintil in [1, 2] and edad > 65:
    subsidio += 25000

# Mostrar resultado
print(f"El valor del subsidio de agua es: {subsidio}") #.replace(",", ".")


