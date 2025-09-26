#1) Crear una lista con las notas de 10 estudiantes.
# Mostrar la lista completa.
# Calcular y mostrar el promedio.
# Indicar la nota más alta y la más baja
notas= [3,7,5,8,6,10,9,8,2,6]
print ("Notas : ")
for n in notas:
    print(n, end=" ")
promedio=sum(notas) / len(notas)
print()
print("El promedio de las notas es de: " , promedio)
print("nota mas alta:", max(notas))
print ("nota mas baja:", min(notas))