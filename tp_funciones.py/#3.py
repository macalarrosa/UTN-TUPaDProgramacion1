#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima:“Soy[nombre] [apellido], tengo [edad] años y vivo en [residencia]”.
#  Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal() :
   
    nombre = input("Escriba su NOMBRE por favor: ")
    apellido = input("Escriba su APELLIDO por favor: ")
    edad = int(input("Escriba su EDAD por favor: "))
    residencia = input("Escriba su lugar de RESIDENCIA por favor: ")
    print(f"Soy{nombre} {apellido} , tengo {edad} años y vivo en {residencia}.") 

informacion_personal()