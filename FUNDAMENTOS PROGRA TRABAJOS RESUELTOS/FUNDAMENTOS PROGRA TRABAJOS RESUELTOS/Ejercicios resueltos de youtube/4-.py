"""programa que valide si una contarseña especificada por el usuario es segura.
Una contraseña segura:
-> tiene mas de 8 caracteres
-> tiene al menos una letra mayuscula
-> tiene al menos un numero"""

def comprobarContrasena(password):
    largo = False
    mayus = False
    numer = False
    if len(password) > 8:
        largo = True
    for i in range(len(password)):
        if password[i].isupper():
            mayus = True
        if password[i].isnumeric():
            numer = True

    if largo and mayus and numer:
        return True
    else:
        return False
    
password = input("ingrese una contrasena: ")
verificacion = comprobarContrasena(password)
if verificacion:
    print("la contrasena es segura")
else:
    print("la contrasena no es segura")