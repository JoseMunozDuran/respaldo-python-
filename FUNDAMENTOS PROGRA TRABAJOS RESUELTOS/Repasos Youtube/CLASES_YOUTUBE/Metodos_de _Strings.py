animal = "chanCHito"

print(animal.upper()) #a mayuscula
print(animal.lower()) # a minuscula
print(animal.capitalize()) #primer caracter a mayuscula
print(animal.strip().capitalize()) #ejemplo de concatenacion de metodos
print(animal.title()) #primeras letras de cada palabra a mayuscula
print(animal.strip()) #remueve los espacios en blanco
print(animal.lstrip()) #remueve los espacios en blanco de la izquierda
print(animal.rstrip()) #remueve los espacios en blanco de la derecha
print(animal.find()) #busca cadena de caracteres y devuelve el indice (entrega numero)(si da -1 no lo encontro)
print(animal.replace("nCH" , "j")) #cambia el caracter que le pedi por el que esta escrito (si no encunetra no ejecuta )
print("nCH" in animal) #devuelve boolean (si es que se encuentra o no)
print("nCH" not in animal) #busca si no se encuentra dentro del string