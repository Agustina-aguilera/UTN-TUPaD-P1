#agustina_aguilera_tp2_05_2.py

def informacion_personal():
    nombre = input("inserte un nombre: ")
    apellido = input("inserte un apellido: ")
    edad = input("inserte un edad: ")
    residencia= input("inserte un residencia: ")

    return  f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

print(informacion_personal())