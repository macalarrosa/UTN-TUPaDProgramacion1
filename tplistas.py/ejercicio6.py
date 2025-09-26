#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
#último pasa a ser el primero).
numeros = [1,2,3,4,5,6,7]
ultimo = numeros[-1]
resto=numeros[:-1]
rotado=[ultimo]+ resto
print(rotado)