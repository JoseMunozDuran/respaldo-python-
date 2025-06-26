while True:
    try:
        num1 = int(input("Ingrese un Número 1: "))
        num2 = int(input("Ingrese un Número 2: "))
        x = num1 / num2
        print(x)
        break
    except Exception as e:
        print(f"Error Inesperado: {e}")