#Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa 
#debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos 
#y cuántos son positivos.
pares=0
impares=0
positivos=0
negativos=0
for i in range (10):
    numero = int(input("Ingresa un numero entero: "))
    if numero % 2 == 0 :
        pares += 1
    else: 
        impares += 1
    if numero > 0 :
        positivos += 1
    else:
        impares += 1
print(f"Numeros pares: " ,pares)
print(f"Numeros impares: " , impares)
print(f"Numeros positivos: ", positivos)
print(f"Numeros impares:", impares)