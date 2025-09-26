#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#Crear una lista con los pares y otra con los impares.
# Mostrar cuántos números tiene cada lista.
import random
num=[]
for i in range (15):
    num_aleatorio= random.randint(1,100)
    num.append(num_aleatorio)
print("Lista : ", num)
pares=[]
impares=[]
for numero in num :
    if numero %2 == 0:
        pares.append(num)
else:
    impares.append(num)
print("numeros pares:", pares)
print("cantidad de pares", len(pares))
print("numeros impares:",impares)
print("cantidad de impares:", len(impares))