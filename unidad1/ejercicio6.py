# escribir un programa que tome la lista Nmeros_aleatorios, calcule su moda, su mediana y su media #
import random
numeros_aleatorios = [random.randint(1,100) for i in range (50)]
mi_lista = numeros_aleatorios
print(mi_lista)
from statistics import mode, median, mean
media = mean (mi_lista)
moda= mode (mi_lista)
mediana= median(mi_lista)
print(f"La media es {media}, la moda es {moda} y la mediana es {mediana}")

if media > mediana and mediana > moda:
    print("Sesgo positivo")
if media  < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana and media==moda: 
    print ("Sin sesgo")