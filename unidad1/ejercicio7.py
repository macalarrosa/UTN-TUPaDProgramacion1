# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado  termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
cadena = str(input("Ingrese la palabra o frase: "))
longitud = len(cadena)

if (cadena[-1]) ==  "a" or (cadena[-1]) =="e"or(cadena[-1]) =="i"or(cadena[-1]) =="o"or(cadena[-1]) =="u"or(cadena[-1]) =="A"or(cadena[-1]) =="E"or(cadena[-1]) =="I"or(cadena[-1]) =="O"or(cadena[-1]) =="U" :
    print ( cadena , "!" )
else:
    print (cadena)