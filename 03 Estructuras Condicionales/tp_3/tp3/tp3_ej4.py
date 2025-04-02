"""4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
siguientes categorías pertenece: 
● Niño/a: menor de 12 años. 
● Adolescente: mayor o igual que 12 años y menor que 18 años. 
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
● Adulto/a: mayor o igual que 30 años."""

Edad= int(input("Ingrese su edad: "))

if Edad < 12:
    print("Categoria: niño/a")
elif 12 <= Edad < 18:
    print("Categoria: Adolescente")
elif 18 <= Edad < 30:
    print("Categoria: Adulto/a joven")
elif Edad>= 30:
    print("Categoria: Adulto/a")

