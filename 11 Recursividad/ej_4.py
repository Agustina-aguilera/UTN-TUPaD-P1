"""Crear una función recursiva en Python que reciba un número entero positivo en base 
decimal y devuelva su representación en binario como una cadena de texto. """

def binaria(num):
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    else:
        return binaria(num//2) +str(num%2)

num= int(input("num: "))

print(binaria(num))