#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. 
# El programa debe detenerse y mostrar el total acumulado cuando el usuario ingreseun 0.
num = int(input( "Ingrese los numeros que desea ir sumando, si desea parar el programa, ingrese 0 :"))
suma = 0 
while num != 0 :
    suma += num
    num = int(input( "Ingrese otro numero que desee sumar, si desea parar el programa, ingrese 0 :"))
print ("La suma total es de :" , suma)