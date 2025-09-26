#2) Pedir al usuario que cargue 5 productos en una lista.
# Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# Preguntar al usuario qué producto desea eliminar y actualizar la lista.
productos = []
for i in range (5):
    item = input(f"Ingrese el producto por favor {i+1} :")
    productos.append(item)
print("La lista de productos es la siguiente: " , productos)
print("La lista ordenada alfabeticamente es la siguiente: ", (sorted(productos)))
print()
eliminar=input("Ingrese el producto que desee elimminar : ")

if eliminar in productos:
    productos.remove(eliminar)
    print(f"n\'{eliminar}' fue eliminado de la lista.")
else:
    print("El producto no se encuentra en la lista, ingrese uno valido. ")

print ( "La lista actualizada es la siguiente: " , productos)