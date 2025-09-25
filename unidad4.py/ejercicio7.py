#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
n=(int(input("Ingrese un numero entero positivo por favor: ")))
suma=0
for i in range (0, n +1):
    suma = suma + i
print("La suma de todos los numeros es de:", suma)