"""programa que toma las tres notas de un estudiante y diga la nota final del curso.
tenga en cuenta que la primera y segunda nota valen el 30% de la nota final. La tercera nota vale el 40% """

def calcularNota(n1, n2, n3):
    return (n1*0,3) + (n2*0.3) +(n3*0.4)

n1 = float(input("ingrese la primera nota: "))
n2 = float(input("ingrese la segunda nota: "))
n3 = float(input("ingrese la tercera nota: "))

notaFinal = calcularNota(n1, n2, n3)

print("La nota final del estudiante es: ",round(notaFinal,2)) #round hace que de los decimales que uno desea en este caso 2