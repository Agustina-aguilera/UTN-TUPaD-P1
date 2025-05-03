#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores

#Pedimos al usuario ambos valores y los guardamos en las variables
primer_num= int(input("Ingrese un numero para iniciar la sumatoria: "))
segun_num= int(input("Ingrese otro numero para iniciar la sumatoria: "))
sumatoria=0
contador=0

#Comprobamos que el primer numero sea menor que el segundo para sumar, de lo contrario el programa termina

if primer_num > segun_num:
    print("Valores incorrectos, el primero debe ser menor que el segundo.")
else: #hacemos un ciclo for para hacer la sumatoria
    for i in range((primer_num),(segun_num-1)):
        contador= i + 1
        sumatoria+= contador
        print("Numero: ", contador, "Sumatoria: ", sumatoria)


