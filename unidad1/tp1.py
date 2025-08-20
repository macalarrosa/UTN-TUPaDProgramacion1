#1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.#
print ("Hola mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.#
nombre = input("Ingrese su nombre: " )
print (f"Hola " + nombre )

#3)Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.#
nombre = input ("Ingrese su nombre por favor: ")
apellido = input ("Ingrese su apellido por favor: ")
edad = input ("Ingrese su edad por favor: ")
residencia = input ("Ingrese el lugar de residencia por favor: ")
print (f"Soy " + nombre + apellido , "tengo " + edad , " años, y vivo en " + residencia )


# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.#
radio = float(input("Ingrese el radio de un circulo:" ))
area = 3.14*radio**2
perimetro=2*3.14*radio

print ("El area del circulo es:" , area, " y el perimetroes:", perimetro)


#5)Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.#
segundos = int(input("Ingrese la cantidad de segundos que quiera transformar a horas:"))
horas = segundos // 3600
print("La cantidad de horas es", horas )


#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla demultiplicar de dicho número.#
numero = int(input("Hola, ingrese por favor un numero y le diremos la tabla del mismo: "))
for contador in range (1,11) :
    print (numero ,"x", contador, ":" , (numero*contador) )

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestrelos por pantalla el resultado de sumarlos, dividirlos, multiplicar y restarlos#
numero1 = int (input("Ingrese el primer numero entero, que no sea 0 por favor"))
numero2 = int (input("Ingrese el segundo numero entero, que no sea 0 por favor"))
suma = numero1 + numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
resta = numero1 - numero2
print ("La suma de ambos numeros es de", suma )
print ("La multiplicacion de ambos numeros da como resultado:" ,multiplicacion)
print ("La division de ambos numeros da como resultado:" ,division)
print("La resta de ambos numeros da como resultado:", resta)


#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguientemodo:#
altura= float (input("Ingrese cual es su altura por favor: "))
peso = float (input ("Ingrese cual es su peso en kg por favor: "))
IMC= peso // (altura) ** 2
print (" Su IMC indice de masa corporal, es de : " , IMC )


#9)Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.#
grados_celsius = float(input("Ingrese los grados Celsius: " ))
grados_fahrenheit = 9/5 * grados_celsius + 32
print ("Son" , grados_fahrenheit, " °F")


#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.#
nota1=float(input("Ingrese la primer nota:"))
nota2= float(input("Ingrese la segund nota:"))
nota3= float(input("Ingrese la tercer nota:"))
promedio = (nota1 + nota2 + nota3 ) / 3
print ("El promedio es de:" , promedio )
