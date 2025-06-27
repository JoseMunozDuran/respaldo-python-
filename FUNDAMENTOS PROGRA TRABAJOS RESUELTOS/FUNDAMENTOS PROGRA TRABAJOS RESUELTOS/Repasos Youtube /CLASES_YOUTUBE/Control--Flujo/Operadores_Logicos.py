# and, or, not
# and : y (las dos condiciones se tienen que cumplir)
# or : o (una de las dos opciones se tiene que cumplir)
# not : cambia a True

gas = False
encendido = True
edad = 18

if not gas and (encendido or edad > 17): #se va a evaluar primero lo que esta en parentesis

    print("puedes avanzar")