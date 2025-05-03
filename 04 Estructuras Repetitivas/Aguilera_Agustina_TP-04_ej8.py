"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""
contador=0
num= 0
cont_negativo=0
cont_positivo=0
cont_impar=0
cont_par=0

#Iniciamos el ciclo con un tope definido anteriormente, cuando ese valor sea 100 el ciclo se cierra
while contador<100:

    num= int(input("Ingrese 100 numeros: "))
	
    contador+=1

    if num > 0:
        cont_positivo += 1
    elif num < 0:
        cont_negativo += 1
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1
			
print("pares: ",cont_par, " impares: ",cont_impar," negativos: ",cont_negativo," positivos: ", cont_positivo)
