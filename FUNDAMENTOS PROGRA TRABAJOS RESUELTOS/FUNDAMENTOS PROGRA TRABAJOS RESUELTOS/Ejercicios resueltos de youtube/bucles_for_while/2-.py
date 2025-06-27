"""programa que calcule el IVA de una compra, siendo el IVA del 19% sobre el valor total de compra"""

def caluclarIVA(p):
    IVA = p * 0.19
    return IVA

precioCompra = float(input("Ingrese el valor de la compra: "))
IVA = caluclarIVA(precioCompra)
print("El valor de la compra sin IVA es de: ", precioCompra)
print("El valor a pagar en total (IVA incluido) es de: ", (precioCompra+IVA))
