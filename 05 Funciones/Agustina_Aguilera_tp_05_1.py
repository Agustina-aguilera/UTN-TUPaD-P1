lista = list(range(1,101))
lista_multiplo=[]

for i in lista:
    if i % 4 == 0 :
        lista_multiplo.append(i)

print(lista_multiplo)
