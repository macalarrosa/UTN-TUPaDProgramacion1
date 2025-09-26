#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de unasemana.
# Calcular el promedio de las mínimas y el de las máximas.
# Mostrar en qué día se registró la mayor amplitud térmica.
temperaturas = [
     [7, 16],
     [13, 20],
     [16, 24],
     [18, 26],
     [11, 22],
     [9, 17],
     [5, 14] 
]
min = [fila[0] for fila in temperaturas]
maximo = [fila[1] for fila in temperaturas]
prom_min = sum(min)/len(min)
prom_max = sum(maximo)/len(maximo)
amplitudes = [fila[1] - fila[0] for fila in temperaturas]
dia_mayor_amplitud= amplitudes.index(max(amplitudes))+1
print("El dia con mayor amplitud es :", dia_mayor_amplitud)