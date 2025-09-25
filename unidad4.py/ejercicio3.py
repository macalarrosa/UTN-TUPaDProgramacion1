#3) Escribe un programa que sume todos los números enteros comprendidos
#  entre dos valores dados por el usuario, excluyendo esos dos valores.
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
suma = 0
if num1 > num2 :
    num1, num2 = num2,num1
for suma in range (num1+1, num2):
    suma += suma
print("La suma es de ",suma)

