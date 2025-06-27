"""🔸 5. Sistema de Usuarios con Contraseña Segura
Datos: nombre usuario, contraseña.

Funciones:

Crear usuario.

Consultar contraseña por nombre.

Eliminar usuario.

Validaciones de contraseña:

Al menos 6 caracteres.

Al menos una mayúscula.

Al menos un número.

Sin espacios."""

def main():
    usuarios = {}
    while True:
        print("\n🔐 GESTIÓN DE USUARIOS")
        print("1. Crear usuario")
        print("2. Consultar contraseña")
        print("3. Eliminar usuario")
        print("4. Salir")

        op = input("Opción: ")
        if op == "1":
            crear(usuarios)
        elif op == "2":
            consultar(usuarios)
        elif op == "3":
            eliminar(usuarios)
        elif op == "4":
            break
        else:
            print("Inválido")

def crear(usuarios):
    nombre = input("Usuario: ")
    if nombre in usuarios:
        print("Ya existe.")
        return
    contraseña = input("Contraseña: ")
    if (len(contraseña) >= 6 and
        any(c.isupper() for c in contraseña) and
        any(c.isdigit() for c in contraseña) and
        " " not in contraseña):
        usuarios[nombre] = contraseña
        print("Usuario creado.")
    else:
        print("Contraseña insegura (6+ caracteres, 1 mayúscula, 1 número, sin espacios).")

def consultar(usuarios):
    nombre = input("Usuario: ")
    if nombre in usuarios:
        print(f"Contraseña: {usuarios[nombre]}")
    else:
        print("No encontrado.")

def eliminar(usuarios):
    nombre = input("Eliminar usuario: ")
    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado.")
    else:
        print("No existe.")

if __name__ == "__main__":
    main()
