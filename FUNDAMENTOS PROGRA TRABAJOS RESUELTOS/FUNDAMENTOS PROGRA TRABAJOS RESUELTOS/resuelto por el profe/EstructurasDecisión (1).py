#Conjunción
'''edad = 17
tiene_licencia = True
if edad >= 18 or tiene_licencia:
	print("Puede conducir")'''

'''edad = 42
if edad < 18:
	print("Eres menor de edad.")
elif 18 <= edad <= 40:
	print("Eres adulto joven.")
elif 41 <= edad < 65:
	print("Eres adulto.")
else:
	print("Eres un adulto mayor.")

edad = 66
if edad < 18:
	print("Eres menor de edad.")
elif edad >= 18 and edad <= 40:
	print("Eres adulto joven.")
elif edad >= 41 and edad < 65:
	print("Eres adulto.")
else:
	print("Eres un adulto mayor.")'''


from typing import Union #Importa Union desde el módulo typing

def verificar_tipo(valor: Union[int | str |float]) -> str:
    #def define una función llamada verificar_tipo
    #valor puede recibir un dato tipo entero, caracter, o decimal
    #-> str esta función al finalizar debe devolver o retornar un string, una cadena de texto
    match valor:
        #Iniciamos una estructura match
        #que evaluará un valor
        case 1: #Si el valor = a 1 devolverá mensaje "Es número entero"
            return "Es un número entero"
        case "texto": ##Si el valor = a "texto" devolverá mensaje "Es una cadena de caracteres"
            return "Es una cadena de caracteres"
        case 3.14: #Si el valor = a 3.14 devolverá mensaje "Es un número decimal"
            return "Es un número decimal"
        case _: #Este case se ejecutará en caso que no se cumpla ningún case
            return "Es un tipo de dato no reconocido"

resultado = verificar_tipo(3.14)
#Se llama a la función verificar_tipo pasamos el valor 3.14
#como 3.14 es igual al case 3.14
print(resultado)
#mostrará el resultado del return o mensaje.



