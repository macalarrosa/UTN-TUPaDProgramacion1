#9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
def convertir_a_fahrenheit(c):
    return c * 9/5 + 32

def convertir_a_kelvin(c):
    return c + 273.15

def menu_conversion():
    opcion = input("¿Convertir a (F)ahrenheit o (K)elvin? ")
    if opcion in ["F", "K"]:
        return opcion
    else:
        return None

c = float(input("Ingrese la temperatura en grados Celsius: "))
op = menu_conversion()
if op == "F":
    print(c, "°C =", convertir_a_fahrenheit(c), "°F")
elif op == "K":
    print(c, "°C =", convertir_a_kelvin(c), "K")
else:
    print("Opción incorrecta")