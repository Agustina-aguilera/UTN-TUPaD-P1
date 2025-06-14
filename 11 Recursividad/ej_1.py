""" Crea una función recursiva que calcule el factorial de un número. 
Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números 
enteros entre 1 y el número que indique el usuario """

def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num-1)*num

num_fin= int(input("Ingrese un numero para encontrar lo factoriales entre el 1 y él: "))

print(factorial(num_fin))