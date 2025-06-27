#Supermercado

sw = 1
listaSuper = []
valorSuper = []

print("Presione 1 para ingresar los productos del Supermercado: ")
print("Presione Cualquier tecla para salir¡¡¡")
op = int(input("Seleccione opción: "))
if(op == 1):
    while sw == 1:
        try:
            print("---------------------------------------")
            producto = input("Ingrese su producto, para salir, presione 0: ")
            if(producto != "0"):
                listaSuper.append(producto)
                valorProducto = int(input(f"Ingrese el valor del {producto}"))
                valorSuper.append(valorProducto)
                print("---------DETALLE BOLETA--------")
                print(f"Sus productos comprados son: {listaSuper}")
                print(f"La Cantidad de productos comprados son: {len(listaSuper)}")
                print(f"Tiene un total a Pagar de: {sum(valorSuper)}")
            else:
                print("Adiós¡¡")
                sw=0
        except:
            print("Ingreso Erróneo¡¡")
else:
    print("Adiós")