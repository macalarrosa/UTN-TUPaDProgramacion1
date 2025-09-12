#Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres(incluyendo 8 y 14).
contraseña = str(input("Escriba la contraseña"))

if len(contraseña) >= 8 and len(contraseña) <= 14:
        print("Ha ingresado una contraseña correcta")
else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")