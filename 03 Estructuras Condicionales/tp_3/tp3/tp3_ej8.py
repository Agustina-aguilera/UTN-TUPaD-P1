"""8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
dependiendo de la opción que desee: 
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
lower() y title() de Python para convertir entre mayúsculas y minúsculas. """

Nombre= input("Ingrese su nombre: ")
Pedido1= Nombre.upper()
Pedido2= Nombre.lower()
Pedido3= Nombre.title()

Pedido_usuario= int(input("Ingrese:\n 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.  \n"
"2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.  \n"
"3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. \n"
"Su respuesta:  "))

if Pedido_usuario == 1:
    print(Pedido1)
elif Pedido_usuario== 2:
    print(Pedido2)
elif Pedido_usuario== 3:
    print(Pedido3)
else:
    print("Numero incorrecto")