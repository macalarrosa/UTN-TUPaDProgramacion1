#5.Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto.
# Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.
productos = []

with open('productos.txt', 'r') as file:
    for line in file:
        partes = line.strip().split(',')
        
        if len(partes) == 3:
            producto, precio, cantidad = partes
            productos.append({
                'nombre': producto.strip(),
                'precio': float(precio),
                'cantidad': int(cantidad)
            })
        else:
            print(f"Línea no válida: {line}")

print(productos)
