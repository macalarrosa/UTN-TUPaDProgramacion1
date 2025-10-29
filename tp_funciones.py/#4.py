#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
#Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

import math

def calcular_area_circulo(radio_area):
    radio_area = float(input("Ingrese el radio y le devolveremos el área del círculo: "))
    area1 = math.pi * (radio_area ** 2)
    print(f"El área del círculo es: {area1}")

def calcular_perimetro_circulo(radio_perimetro):
    radio_perimetro = float(input("Ingrese el radio y le devolveremos el perímetro del círculo: "))
    perimetro = 2 * math.pi * radio_perimetro
    print(f"El perímetro del círculo es: {perimetro}")
calcular_area_circulo(0)
calcular_perimetro_circulo(0)
