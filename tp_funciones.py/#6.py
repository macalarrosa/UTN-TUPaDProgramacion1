#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero):
    numero=int(input("Ingrese un numero del 1 al 10 y le imprimiremos su tabla de multiplicar"))
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
tabla_multiplicar(0)