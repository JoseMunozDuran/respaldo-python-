#try except finally

#programa que se encarga de sumardos numeros

'''numero1 = int(input("introduce el primer numero"))
numero2 = int(input("introduce el segundo numero"))

resultado = numero1 + numero2
print (resultado)'''

#solucion para aque no de error


'''try:
    numero1 = int(input("introduce el primer numero: "))
    numero2 = int(input("introduce el segundo numero: "))
    resultado = numero1 + numero2
    print (resultado)
except:
    print("debes ingresar un numero")'''

#sentencia finally (esto se ejecuta si o si)

'''try:
    numero1 = int(input("introduce el primer numero: "))
    numero2 = int(input("introduce el segundo numero: "))
    resultado = numero1 + numero2
    print (resultado)
except:
    print("debes ingresar un numero")
finally:
    print("se imprime si o si")'''

#control de las excepciones usando WHILE

while(True):
    try:
        numero1 = int(input("introduce el primer numero: "))
        numero2 = int(input("introduce el segundo numero: "))
        resultado = numero1 + numero2
        print (resultado)
        break
    except:
        print("debes ingresar numeros")