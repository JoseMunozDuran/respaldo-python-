#Solución Control 2 
from random import randint

# Paso 1: Ingreso de datos
nroEmpleado = randint(1000, 9999)
nombre = str(input("Ingrese su nombre: "))
edad = int(input("Ingrese su edad: "))
sueldo_bruto = float(input("Ingrese su sueldo bruto mensual: "))
cargas = int(input("Ingrese cantidad de cargas familiares: "))

# Paso 2: Cálculo del descuento por edad
descuento_edad = 0
if edad < 25:
    descuento_edad = sueldo_bruto * 0.05
elif 25 <= edad <= 50:
    descuento_edad = sueldo_bruto * 0.10
else:  # edad > 50
    descuento_edad = sueldo_bruto * 0.15

# Paso 3: Cálculo del impuesto por renta
impuesto = 0
if sueldo_bruto > 1800000:
    impuesto = sueldo_bruto * 0.08
elif 1200000 <= sueldo_bruto <= 1800000:
    impuesto = sueldo_bruto * 0.04
# Si el sueldo es menor a 1.200.000 no hay impuesto (impuesto = 0)

# Paso 4: Cálculo de bonificación por cargas familiares
bonificacion = 0
if cargas >= 2:
    bonificacion = 75000
elif cargas == 1:
    bonificacion = 40000

# Paso 5: Cálculo del sueldo líquido
sueldo_liquido = sueldo_bruto - descuento_edad - impuesto + bonificacion

# Paso 6: Mostrar resultados
print("\n--- RESUMEN DE LIQUIDACIÓN ---")
print("Nro. Empleado\t\t:", nroEmpleado)
print("Empleado\t\t:", nombre)
print("Edad\t\t\t:", edad)
print("Sueldo Bruto\t\t:", int(sueldo_bruto))
print("Cargas Familiares\t:",cargas)
print("*************Liquidación de Sueldo**************")
print("Descuento por edad\t: $", int(descuento_edad))
print("Impuesto por renta\t: $", int(impuesto))
print("Bonificación por cargas\t: $", int(bonificacion))
print("Sueldo líquido final\t: $", int(sueldo_liquido))