"""7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por 
pantalla. """


Frase= input("Ingrese una frase u oracion: ")


if Frase[-1] == "a" or Frase[-1] == "e" or Frase[-1] == "i" or Frase[-1] == "o" or Frase[-1] == "u":
    print(f"{Frase}!")
else:
    print(Frase)