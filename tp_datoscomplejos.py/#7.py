#7 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1y Parcial 2:
# Mostrá los que aprobaron ambos parciales.
# Mostrá los que aprobaron solo uno de los dos.
# Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
parcial1 = {1, 2, 3, 4, 5, 6}
parcial2 = {4, 5, 6, 7, 8}

ambos = parcial1 & parcial2
solo_parcial1 = parcial1 - parcial2

solo_parcial2 = parcial2 - parcial1
al_menos_uno = parcial1 | parcial2
print("Aprobaron ambos:", ambos)
print("Solo Parcial 1:", solo_parcial1)
print("Solo Parcial 2:", solo_parcial2)
print("Aprobaron al menos uno:", al_menos_uno)
