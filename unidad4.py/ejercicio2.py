#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
numero_entero = int(input("Ingrese un numero entero por favor: "))
cadena_numeros = str (numero_entero)
digitos = len(cadena_numeros)
print("El  numero tiene",digitos ,"digitos. ")