"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor)."""

#Declaramos las variables que vamos a usar
contador=0
sumatoria=0
maximo=100

#Usamos el ciclo que va a terminar en 100, cuando llega se detiene. Se suma el numero al total que sera sumatoria y se suma una vuelta al contador

while contador<maximo:
    num = int(input("Ingrese 100 numeros para encontrar la media: "))
    sumatoria += num
    contador += 1

#Imprimimos la sumatoria divido el contador, q sera el total de numeros sumado divido la cantidad    
print ("La media de estos valores es: "+ str(sumatoria/contador))
