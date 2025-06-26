n1 =input("ingrese primer numero ") 
n2 =input("ingrese segundo numero ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
munti = n1 * n2
div = n1 / n2

mensaje = f"""los resultados son para los numeros {n1} y {n2} es: 
{suma}
{resta}
{munti}
{div}"""
print(mensaje)