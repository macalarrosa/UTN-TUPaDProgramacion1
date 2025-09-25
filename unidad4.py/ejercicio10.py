#Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario
num=input("Ingrese el numero: ")
invertido=""
i=len(num) -1
while i >= 0:
    invertido += num [i]
    i -= 1
print (f"El numero invertido es : {invertido}")