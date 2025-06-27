from random import randint
#Comenzamos definiendo las constantes
ARANCEL = 1800000
MATRICULA = 90000

promedio = float(input("Ingrese su promedio: "))
quintil = int(input("Ingrese su quintil [1,2,3,4 o 5]: "))

descuento_arancel = 0
descuento_matricula = 0

#Descuento de arancel
if promedio > 6.0:
    if quintil in [1, 2]:
        descuento_arancel = 0.20
    elif quintil in [3,4]:
        descuento_arancel = 0.15
elif 5.0 < promedio <= 6.0:
    if quintil in [1, 2]:
        descuento_arancel = 0.13
    elif quintil in [3,4]:
        descuento_arancel = 0.10
    
#Descuento de Matricula
if quintil in [1,2,3]:
    descuento_matricula = 0.10
    if promedio >= 5.5:
        descuento_matricula += 0.05

#Juego de adivinanzas
print("\n Juego para Obtener un 5% extra de descuento en el arancel") 
limite_inferior = int(input("Ingrese el límite inferior al Juego: "))
limite_superior = int(input("Ingrese el límite superior al Juego: ")) 

numero_secreto = randint(limite_inferior, limite_superior)
gana_bono = False
print(numero_secreto)
intento1 = int(input("Intente adivinar: "))
if intento1 == numero_secreto:
    print("¡¡¡Felicitaciones, adivino en el primer intento")
    gana_bono = True
else:
    print("El número es mayor." if intento1 < numero_secreto else "El número es menor")
    intento2 = int(input("Intente de nuevo: "))
    if intento2 == numero_secreto:
        print("¡¡¡Felicitaciones, adivino en el segundo intento")
        gana_bono = True
    else:
        print("El número es mayor." if intento2 < numero_secreto else "El número es menor")
        d1 = abs(numero_secreto - intento1)
        d2 = abs(numero_secreto - intento2)
        if d1 < d2:
            print(f"El número secreto que buscas esta más cerca de {intento1}")
        elif d2 < d1:
            print(f"El número secreto que buscas esta más cerca de {intento2}")
        else:
            print("Ambos intentos están igual de cerca")
        intento3 = int(input("Intente la última vez: "))
        if intento3 == numero_secreto:
            print("¡¡¡¡Felicitaciones, adivinó en el tercer intento¡¡¡¡") 
            gana_bono = True
        else:
            print("Perdiste. El número Secrero era:", numero_secreto)       
if gana_bono:
    descuento_arancel += 0.05
    print("¡Ganaste un 5% aducional de descuento en el arancel")

valor_arancel = int(ARANCEL * (1 - descuento_arancel))
valor_matricula = int(MATRICULA * (1 - descuento_matricula))

print("\nResumen de Beneficios: ")
print("Valor final del Arancel: $", valor_arancel)
print("Valor final de la Matricula: $", valor_matricula)
     


