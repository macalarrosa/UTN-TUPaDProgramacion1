#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numAleatorio= random.randint(0,9)
intentos=0
print(" Bienvenidos al juego de adivinanzas, estoy pensando en un numero entre el 0 y el 9")
while True:
    numNuevo=(int(input("Ingrese el numero : ")))
    intentos = intentos + 1
    if (numNuevo == numAleatorio):
        print("Felicitaciones, acertaste!! Usted ha hecho un total de intentos de :" ,intentos )
        break  