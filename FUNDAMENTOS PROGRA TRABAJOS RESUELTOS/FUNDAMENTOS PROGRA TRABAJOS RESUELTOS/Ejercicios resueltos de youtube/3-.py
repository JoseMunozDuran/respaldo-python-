"""programa que calcule la tabla de multiplicar de cualquier numero estero dado por el usuario.
Debe calcular la tabla desde el 0 hasta el 12"""

def tablaDeMultiplicar(n1, n2):
    return str(n1) + " * " + str(n2) + " = " + str(n1*n2)

n = int(input("Ingrese un numero entero: "))

for i in range(0, 13):
    print(tablaDeMultiplicar(n,i))