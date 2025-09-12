# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál categoría pertenece#
edad = int(input("Ingrese su edad y le diremos a que categoria pertenece: "))
if edad < 12:
    print("CATEGORIA NIÑOS/AS")
if edad >= 12 and edad < 18 :
    print("CATEGORIA ADOLESCENTES")
if edad >= 18 and edad < 30:
    print("CATEGORIA ADULTO JOVEN")
elif edad >= 30:
    print ("CATEGORIA ADULTOS") 
