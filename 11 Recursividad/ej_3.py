"""3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
utilizando la fórmula n a la 𝑚 =n*n(** m-1) Prueba esta función en un algoritmo general. """

def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m - 1)
    
print(potencia(2,3))