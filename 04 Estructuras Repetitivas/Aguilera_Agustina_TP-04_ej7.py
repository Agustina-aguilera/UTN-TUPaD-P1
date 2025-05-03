"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero 
 positivo indicado por el usuario."""

#Pedimos al usuario un valor y los guardamos
num=int(input("Ingrese un numero limite para sumar: "))
#sumamos un 1 al numero porque sino el numero ingresado quedara fuera del range
num+=1
comprendido=0

#como tenemos un numero definido de vueltas, podemos usar for, guardamos el numero sumado
for i in range(0,num):
    comprendido+=i

#imprimimos el resultado
print("La suma es:"+str(comprendido))