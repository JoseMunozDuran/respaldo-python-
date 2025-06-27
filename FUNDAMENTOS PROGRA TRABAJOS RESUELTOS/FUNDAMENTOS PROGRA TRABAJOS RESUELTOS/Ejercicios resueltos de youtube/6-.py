"""programa que calcule el nuevo salario de un trabajador si obtuvo un incremeto del x%"""

def calcularIncremento(salario, x):
    nuevoSalario = salario + (salario + (x/100))
    return nuevoSalario

salarioActual = float(input("ingrese el salario actual del trabajador: "))
incremento = float(input("ingrese el porcentaje de incremento que tendra el salario del trabajador: "))
nuevoSalario = calcularIncremento(salarioActual, incremento)
print("el nuevo salario del trabajador es de: ", nuevoSalario)