#agustina_aguilera_tp2_05_2.py
import math

def calcular_area_circulo(radio):
    return math.pi*(radio**2)
   
area= calcular_area_circulo(int(input("Ingrese un radio: ")))

print(str(area))
