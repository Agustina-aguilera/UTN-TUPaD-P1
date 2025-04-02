"""Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano. """

print("Para saber en que estacion esta responda: \n")

Hemisferio= int(input("Elija una opcion. En que hemisferio se encuentra? norte= 1  sur= 2 : "))
Mes= int(input("En que mes del año? Seleccione del 1 al 12 segun corresponda: "))
Fecha= int(input("En que fecha? 1 a 31 segun corresponda: "))

## Para saber si es invierno en el hemisferio norte:
if Mes == 12 and 31 >= Fecha >= 21 and Hemisferio == 1:
    print ("Es invierno")
elif Mes == 1 or Mes == 2 and 1 <= Fecha <= 31 and Hemisferio == 1:
    print ("Es invierno")
elif Mes == 3 and 1 <= Fecha <= 20 and Hemisferio == 1:
    print ("Es invierno")

## Para saber si es primavera en el hemisferio norte:
if Mes == 3 and 31 >= Fecha >= 21 and Hemisferio == 1:
    print ("Es primavera")
elif Mes == 4 or Mes == 5 and 1 <= Fecha <= 31 and Hemisferio == 1:
    print ("Es primavera")
elif Mes == 6 and 1 <= Fecha <= 20 and Hemisferio == 1:
    print ("Es primavera")
    
## Para saber si es verano en el hemisferio norte:
if Mes == 6 and 31 >= Fecha >= 21 and Hemisferio == 1:
    print ("Es verano")
elif Mes == 7 or Mes == 8 and 1 <= Fecha <= 31 and Hemisferio == 1:
    print ("Es verano")
elif Mes == 9 and 1 <= Fecha <= 20 and Hemisferio == 1:
    print ("Es verano")

    ## Para saber si es otoño en el hemisferio norte:
if Mes == 9 and 31 >= Fecha >= 21 and Hemisferio == 1:
    print ("Es otoño")
elif Mes == 10 or Mes == 11 and 1 <= Fecha <= 31 and Hemisferio == 1:
    print ("Es otoño")
elif Mes == 12 and 1 <= Fecha <= 20 and Hemisferio == 1:
    print ("Es otoño")

##------------------------------------------------------------------------------------

## Para saber si es invierno en el hemisferio sur:
if Mes == 12 and 31 >= Fecha >= 21 and Hemisferio == 2:
    print ("Es verano")
elif Mes == 1 or Mes == 2 and 1 <= Fecha <= 31 and Hemisferio == 1:
    print ("Es verano")
elif Mes == 3 and 1 <= Fecha <= 20 and Hemisferio == 2:
    print ("Es verano")

## Para saber si es otoño en el hemisferio sur:
if Mes == 3 and 31 >= Fecha >= 21 and Hemisferio == 2:
    print ("Es otoño")
elif Mes == 4 or Mes == 5 and 1 <= Fecha <= 31 and Hemisferio == 2:
    print ("Es otoño")
elif Mes == 6 and 1 <= Fecha <= 20 and Hemisferio == 2:
    print ("Es otoño")
    
## Para saber si es invierno en el hemisferio sur:
if Mes == 6 and 31 >= Fecha >= 21 and Hemisferio == 2:
    print ("Es invierno")
elif Mes == 7 or Mes == 8 and 1 <= Fecha <= 31 and Hemisferio == 2:
    print ("Es invierno")
elif Mes == 9 and 1 <= Fecha <= 20 and Hemisferio == 2:
    print ("Es invierno")

    ## Para saber si es primavera en el hemisferio sur:
if Mes == 9 and 31 >= Fecha >= 21 and Hemisferio == 2:
    print ("Es primavera")
elif Mes == 10 or Mes == 11 and 1 <= Fecha <= 31 and Hemisferio == 2:
    print ("Es primavera")
elif Mes == 12 and 1 <= Fecha <= 20 and Hemisferio == 2:
    print ("Es primavera")