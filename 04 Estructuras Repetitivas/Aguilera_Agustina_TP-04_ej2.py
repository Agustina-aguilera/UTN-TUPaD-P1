#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene. 

#Le pedimos al usuario un numero entero
numero = input("ingrese un numero para saber cuantos digitos tiene: ")
digitos=0

#Verificamos si es negativo. Si lo es, se restara el signo a la cantidad de digitos

if numero.startswith("-"):
    digitos= len(numero-1)
else:
    digitos= len(numero)

print ("La cantidad de digitos en el numero es: " + str(digitos))