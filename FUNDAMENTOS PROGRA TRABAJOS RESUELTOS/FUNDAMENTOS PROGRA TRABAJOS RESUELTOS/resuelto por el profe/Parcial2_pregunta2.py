from random import randint

# Ingresar límites del rango
n1 = int(input('Ingrese límite inferior: '))
n2 = int(input('Ingrese límite superior: '))

# Generar el número aleatorio en el rango completo
num = randint(n1, n2) // 4  # El número generado se divide por 4

# Primer intento
i1 = int(input('Intente adivinar: '))
if i1 == num:
    print('Felicitaciones, pudiste adivinar en el primer intento.')
else:
    print('El número es menor.' if i1 > num else 'El número es mayor.')

    # Segundo intento
    i2 = int(input('Intente de nuevo: '))
    if i2 == num:
        print('Felicitaciones, adivinó en su segundo intento.')
    else:
        print('El número es menor.' if i2 > num else 'El número es mayor.')
        
        # Pista de cuál número estuvo más cerca
        print("Te daré una pista:")
        d1 = abs(num - i1)
        d2 = abs(num - i2)
        if d1 < d2:
            print(f'El número que buscas está más cerca de {i1} que de {i2}')
        elif d1 > d2:
            print(f'El número que buscas está más cerca de {i2} que de {i1}')
        else:
            print(f'El número que buscas está a la misma distancia de {i1} que de {i2}')

        # Tercer intento
        i3 = int(input('Intente la última vez: '))
        if i3 == num:
            print('Felicitaciones, pudiste adivinar.')
        else:
            print(f'Perdiste.\nEl número era: {num}')
