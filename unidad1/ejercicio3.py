# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar#
numero = int(input("Ingrese el numero por favor"))
if numero % 2 == 0: 
    print (f"El numero es par")
else:
    print (f"El numero es impar")