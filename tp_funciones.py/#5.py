#5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas (segundos):
    segundos = float(input("Ingrese los segundos y le devolveremos la cantidad de horas : "))
    horas = segundos/60
    print(f"La cantidad de horas es de : {horas}")
segundos_a_horas(0)