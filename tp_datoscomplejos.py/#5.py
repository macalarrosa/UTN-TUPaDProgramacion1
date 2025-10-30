#5 Solicita al usuario una frase e imprime

frase = input("Escribí una frase: ")
palabras = frase.split()

print("Palabras únicas:", set(palabras))

recuento = {}
for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1
print("Recuento:", recuento)
