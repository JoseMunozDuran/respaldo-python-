#Ciclo FOR
'''
for a in range(5):
    print("Hola",a)'''

'''x = range(1,5,1)
for i in x:
    print("Hola", i)'''

'''for i in ("Hola"):
    print(i)'''

#Ciclo While

'''a = 1
while(a>0):
	print(f"el valor de a es :{a}")
	a = int(input("ingrese un valor"))'''

'''a = 1
while(a<5):
	print(f"el valor de a es :{a}")
	a = a + 1'''
'''a=0
flag = True
while flag:
    print("Hola")
    a = a + 1
    if a == 5:
        flag = False'''

#TRY - Except


try:
    num1 = int(input("Ingrese un Número: "))
    num2 = int(input("Ingrese Otro Número: "))
    x = num1 / num2
    print(x)
    print("")
except ZeroDivisionError:
    print("No es posible dividir en 0")
except TypeError:
    print("¡¡¡No puede ejecutar una operación entre Int y STR¡¡¡")  
except ValueError:
    print("¡¡¡No puede dividir por décimales¡¡¡")  
