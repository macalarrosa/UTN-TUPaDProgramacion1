#4) Dada una lista con valores repetidos:
# 1, 3 ,5 , 3,7,1,9,5,3
# # Crear una nueva lista sin elementos repetidos.
# Mostrar el resultado.
datos = [1 , 3, 5, 3, 7, 1, 9, 5, 3]
sinduplicar = []
for d in datos:
    if d not in sinduplicar:
        sinduplicar.append(d)
print()
print("Lista con elementos duplicados: ")
for d in datos:
    print(d, end="")
print()
print ("Lista sin elementos duplicados: ")
for d in sinduplicar:
    print(d,end="") 