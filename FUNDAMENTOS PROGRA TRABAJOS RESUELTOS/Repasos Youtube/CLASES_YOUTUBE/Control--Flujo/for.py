# for tiene multiples funciones pero lo principal; 
# sirve para iterar una lista de elementos
# buscar elementos, operaciones matematicas, etc

"""for numero in range(5): #range crea una secuencia de numeros que se podra utilizar en for y comienza desde el 0
    print(numero, numero * 'hola mundo')
"""
#for

"""buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break"""

#for else
buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontré el numero")

#iterables: listas, tuplas, strings

"""for usuario in usuarios:
    usuario.id
    print("no encontré el numero")""" # se ve mas adelante

for char in "ultimate python": #char : caracter
    print(char)