"""🔸 4. Gestión de Productos en una Tienda
Datos: nombre producto, precio, stock.

Funciones:

Agregar producto.

Consultar producto.

Modificar stock.

Eliminar producto.

Validaciones:

Precio y stock positivos.

Nombre único"""

def main():
    productos = {}
    while True:
        print("\n🛒 MENÚ PRODUCTOS")
        print("1. Agregar producto")
        print("2. Consultar producto")
        print("3. Modificar stock")
        print("4. Eliminar producto")
        print("5. Mostrar todos")
        print("6. Salir")

        opcion = input("Opción: ")
        if opcion == "1":
            agregar(productos)
        elif opcion == "2":
            consultar(productos)
        elif opcion == "3":
            modificar(productos)
        elif opcion == "4":
            eliminar(productos)
        elif opcion == "5":
            mostrar(productos)
        elif opcion == "6":
            print("Adiós.")
            break
        else:
            print("Opción inválida.")

def agregar(productos):
    nombre = input("Nombre del producto: ").strip()
    if nombre in productos:
        print("Ya existe.")
        return
    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))
        if precio > 0 and stock >= 0:
            productos[nombre] = {"precio": precio, "stock": stock}
            print("Producto agregado.")
        else:
            print("Precio o stock inválido.")
    except:
        print("Error en entrada de datos.")

def consultar(productos):
    nombre = input("Producto: ")
    if nombre in productos:
        print(productos[nombre])
    else:
        print("No existe.")

def modificar(productos):
    nombre = input("Producto a modificar: ")
    if nombre in productos:
        try:
            nuevo_stock = int(input("Nuevo stock: "))
            if nuevo_stock >= 0:
                productos[nombre]["stock"] = nuevo_stock
                print("Stock actualizado.")
            else:
                print("Stock inválido.")
        except:
            print("Error.")
    else:
        print("No encontrado.")

def eliminar(productos):
    nombre = input("Producto a eliminar: ")
    if nombre in productos:
        del productos[nombre]
        print("Producto eliminado.")
    else:
        print("No existe.")

def mostrar(productos):
    if not productos:
        print("Sin productos.")
    for nombre, info in productos.items():
        print(f"{nombre} - Precio: ${info['precio']}, Stock: {info['stock']}")

if __name__ == "__main__":
    main()
