#10 Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
#Las capitales sean las claves.
# Los países sean los valores.
capitales= {  'Argentina': 'Buenos Aires' ,'Chile':'Santiago de Chile','Perú':'Lima', 'Estados Unidos': 'Washington D.C'}
invertidas= { 'Buenos Aires':'Argentina', 'Santiago de Chile':'Chile','Lima':'Perú','Washington D.C':'Estados Unidos'}
print(f"Las capitales con sus paises: {invertidas}")
print(f"Los paises con sus capitales: {capitales}")