#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#• Mostrar la lista final actualizada
estudiantes=["veronica", "ana", "cinthia", "milton", "pablo", "jere", "tobi", "sami"]
print("Asistencia de los estudiantes de hoy: ")
for e in estudiantes : 
    print (e)
opcion = input("Si desea agregar a un estudiante ingrese (A), si desea eliminarlo ingrese (E)").upper()
if opcion == "A" :
    nuevo = input("Ingrese el nombre")
    estudiantes.append(nuevo)
elif opcion == "E":
    eliminar = input("Ingrese el nombre : ")
    if  eliminar in estudiantes:
        estudiantes.remove(eliminar)
    else:
        print("Este estudiante no esta en la lista. ")
print ("Lista actualizada : ")
for e in estudiantes:
    print(e)