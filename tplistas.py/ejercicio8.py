#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#• Mostrar el promedio de cada estudiante.
#• Mostrar el promedio de cada materia
notas = [
    [3,5,7],
    [4,7,6],
    [7,8,9],
    [9,7,8],
    [4,9,7],
]
print("notas de los estudiantes: ")
for fila in notas:
    for nota in fila:
        print(nota, end="")
    print("promedio de cada estudiante: ") 

for i in range (5):
    suma = 0
    for j in range (3):
        suma += notas[i][j]
    promedio = suma / 3
    print(f"El estudiante {i+1}:"),(" {promedio} ")

for j in range (3):
    suma = 0
for i in range (5): 
    suma += notas [i][j]
promedio= suma/5
print(f"El promedio de la materia es de {j+1}")

