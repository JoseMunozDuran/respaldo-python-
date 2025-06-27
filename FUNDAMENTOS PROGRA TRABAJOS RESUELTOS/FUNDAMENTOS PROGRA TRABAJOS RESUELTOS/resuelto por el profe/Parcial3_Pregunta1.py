while True:
    try:
        cant = int(input("Ingrese la cantidad de números a verificar: "))
        break
    except:
        print("Debe ingresar un número entero.")
num_primos = 0
num_no_primos = 0
for c in range(cant):
    while True:
        try:
            n = int(input('Ingrese numero: '))
            break
        except:
            print("Debe ingresar un número entero.")      
    i = 2
    flag = True
    while i<=n/2:
      if n%i == 0:
        print('No es primo.')
        num_no_primos += 1
        flag = False
        break
      i+=1
    if flag:
      print('Es primo.')
      num_primos += 1
print("Se ingresaron", num_primos, "numeros primos.")
print("Se ingresaron", num_no_primos, "numeros no primos.")