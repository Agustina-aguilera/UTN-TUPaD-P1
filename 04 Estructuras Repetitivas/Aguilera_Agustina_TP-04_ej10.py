"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""


#Declaramos las variables que usaremos
num = int(input("Ingrese un para invertiri: "))
num_revez = 0


#Mientras num sea mayor que 0 se puede seguir haciendo divisiones. Vamos a guardar el resto de la division y luego lo sumamos y le sacamos la parte decimal. 
#Asi el numero se arma de nuevo pero al revez.

while num > 0:
    
    digito = num % 10
    num_revez = num_revez * 10 + digito
    num //= 10

print("El numero invertido es: ", num_revez)