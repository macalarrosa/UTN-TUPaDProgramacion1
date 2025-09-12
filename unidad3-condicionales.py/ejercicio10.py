#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es.#
hemisferio = int(input("Ingrese la opcion 1 si usted vive en el norte y la opcion 2 si usted vive en el sur del hemisferio : "))
dia = int(input("Ingrese que dia es hoy: "))
mes = int(input("Ingrese en numeros el mes de hoy"))

if dia == 21 and mes == 12 and hemisferio == 1 :
    print ("ESTACION INVIERNO")
if dia >= 1 and mes == 1 and hemisferio == 1 :
    print ("ESTACION INVIERNO")
if dia >= 1 and mes == 2 and hemisferio == 1 :
    print ("ESTACION INVIERNO")
if dia >= 1 and dia<=20 and mes == 3 and hemisferio == 1 :
    print ("ESTACION INVIERNO")
if dia == 21 and mes == 12 and hemisferio == 2 :
    print ("ESTACION VERANO")
if dia >= 1 and mes == 1 and hemisferio == 2 :
    print ("ESTACION VERANO")
if dia >= 1 and mes == 2 and hemisferio == 2 :
    print ("ESTACION VERANO")
if dia >= 1 and dia<=20 and mes == 3 and hemisferio == 2 :
    print ("ESTACION VERANO")

if dia == 21 and mes == 3 and hemisferio == 1 :
    print ("ESTACION PRIMAVERA")
if dia >= 1 and mes == 4 and hemisferio == 1 :
    print ("ESTACION PRIMAVERA")
if dia >= 1 and mes == 5 and hemisferio == 1 :
    print ("ESTACION PRIMAVERA")
if dia >= 1 and dia<=20 and mes == 3 and hemisferio == 1 :
    print ("ESTACION PRIMAVERA")

if dia == 21 and mes == 3 and hemisferio == 2 :
    print ("ESTACION OTOÑO")
if dia >= 1 and mes == 4 and hemisferio == 2 :
    print ("ESTACION OTOÑO")
if dia >= 1 and mes == 5 and hemisferio == 2:
    print ("ESTACION OTOÑO")
if dia >= 1 and dia<=20 and mes ==6 and hemisferio == 2:
    print ("ESTACION OTOÑO")

if dia == 21 and mes == 6 and hemisferio == 1 :
    print ("ESTACION VERANO")
if dia >= 1 and mes == 7 and hemisferio == 1 :
    print ("ESTACION VERANO")
if dia >= 1 and mes == 8 and hemisferio == 1 :
    print ("ESTACION VERANO")
if dia >= 1 and dia<=20 and mes == 9 and hemisferio == 1 :
    print ("ESTACION VERANO")

if dia == 21 and mes == 6 and hemisferio == 2 :
    print ("ESTACION INVIERNO")
if dia >= 1 and mes == 7 and hemisferio == 2 :
    print ("ESTACION INVIERNO")
if dia >= 1 and mes == 8 and hemisferio == 2 :
    print ("ESTACION INVIERNO")
if dia >= 1 and dia<=20 and mes == 9 and hemisferio == 2 :
    print ("ESTACION INVIERNO")
    
if dia == 21 and mes == 9 and hemisferio == 1 :
    print ("ESTACION OTOÑO")
if dia >= 1 and mes == 10 and hemisferio==1 :
    print ("ESTACION OTOÑO")
if dia >= 1 and mes == 11 and hemisferio == 1 :
    print ("ESTACION OTOÑO")
if dia >= 1 and dia<=20 and mes ==12 and hemisferio == 1:
    print ("ESTACION OTOÑO")

if dia == 21 and mes == 9 and hemisferio == 2 :
    print ("ESTACION PRIMAVERA")
if dia >= 1 and mes == 10 and hemisferio==2 :
    print ("ESTACION PRIMAVERA")
if dia >= 1 and mes == 11 and hemisferio == 2 :
    print ("ESTACION PRIMAVERA")
if dia >= 1 and dia<=20 and mes ==12 and hemisferio == 2:
    print ("ESTACION PRIMAVERA")
    
pass