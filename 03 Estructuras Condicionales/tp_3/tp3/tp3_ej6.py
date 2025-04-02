"""Escribir un programa que tome la lista 
numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la 
mediana es mayor que la moda. 
● Sesgo negativo o a la izquierda: cuando la media es menor que la mediana y, a su vez, 
la mediana es menor que la moda. 
● Sin sesgo: cuando la media, la mediana y la moda son iguales """

from statistics import mode, median, mean
import random

Numeros_aleatorio= [random.randint(1,100) for i in range (50)]

Moda= mode(Numeros_aleatorio)
Mediana= median(Numeros_aleatorio)
Media= mean(Numeros_aleatorio)

print(f"Moda: {Moda}, Mediana: {Mediana}, Media: {Media}")

if Media >= Mediana and Mediana > Moda:
    print("Sesgo positivo")
elif Media < Mediana and Mediana < Moda:
    print ("Sesgo negativo")
elif Moda == Mediana == Media:
    print ("Sin sesgo")