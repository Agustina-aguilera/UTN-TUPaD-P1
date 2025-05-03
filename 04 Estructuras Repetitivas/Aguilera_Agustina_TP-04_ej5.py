#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

#pedimos al usuario que ingrese un numero del 0 al 9

import random


numero=int(input("Adivina el numero: "))
intentos=0
numero_aleatorio= random.randint(0,9)
#verificamos
while numero_aleatorio!=numero:
    if numero >= 0 and numero <= 9:
        while numero_aleatorio!=numero:
            print("Ese no es!")
            intentos+=1
            numero=int(input("Adivina el numero: "))
    else:
        numero=int(input("El numero debe estar entre 0 y 9!: "))

if numero==numero_aleatorio:
    print("Acertaste! Cantidad de intentos fallidos: ", intentos)

    
    
        
