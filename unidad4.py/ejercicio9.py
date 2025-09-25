#Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor). 
suma=0
media=0

for i in range (10):
    n=int(input("Ingresa un numero entero: "))
    suma += n 
    media= suma/2
print("La suma de todos los numeros es de:", suma)
print("La media de todos los numeros es de:", media)