#Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
nombre_usuario = str(input("Ingrese su nombre por favor:"))
opcion = int(input("Ingrese la opcion deseada: 1 - si desea imprimir su nombre en mayusculas, 2- si desea imprimir su nombre en minusculas, 3- si desea imprimir solo la primer letra en mayuscula"))
mayusculas = nombre_usuario.upper()
minusculas= nombre_usuario.lower()
primera_mayuscula = nombre_usuario.title()
if opcion == 1:
    print (mayusculas)
if opcion == 2:
    print (minusculas)
if opcion == 3:
    print(primera_mayuscula)
pass
