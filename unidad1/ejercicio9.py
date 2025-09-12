#Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla#
magnitud = float(input("Ingrese la magnitud del terremoto y le diremos su clasificacion: "))
if magnitud < 3 :
    print ("Muy leve (imperceptible)")
if magnitud >= 3 and magnitud < 4 :
    print ("Leve(ligeramente perceptible)")
if magnitud >= 4 and magnitud < 5 :
    print ("Moderado (sentido por personas, pero generalmente no causa daños)")
if magnitud >= 5 and magnitud < 6:
    print ("Fuerte (puede causar daños en estructuras débiles")
if magnitud >= 6 and magnitud <7 :
    print ("Muy fuerte(puede causar daños significativos)")
if magnitud >= 7 :
    print ("Extremo(puede causar graves daños a gran escala)")