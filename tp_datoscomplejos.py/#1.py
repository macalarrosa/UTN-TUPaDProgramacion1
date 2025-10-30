#1) Dado el diccionario precios_frutas, añadir las siguientes frutas con sus respectivos precios
precios_frutas ={'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] =1500
precios_frutas['Pera'] =2300

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
frutas_sin_precio ={'Banana','Anana', 'Melón','Uva','Naranja','Manzana','Pera'}
print(f"Las frutas disponibles son: {frutas_sin_precio}")
print(f"Los precios de las frutas disponibles son: {precios_frutas}")