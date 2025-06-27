import os
import time
os.system("cls")
print("Bienvenido a Empresa XY")
user = input("Ingrese Nombre de Usuario \t:")
contra = input("Ingrese Contraseña \t\t:")
user_1 = "pedro"

user_2 = "angel"
pass_1 = "1234"
pass_2 = "a4s1"
time.sleep(2)
if(user == user_1 and contra == pass_1) or (user == user_2 and contra == pass_2):
    print("Usuario conectado correctamente en la empresa")
    
else:
    print("Usuario no se encuentra en la empresa")
os.system("Pause")