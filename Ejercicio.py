#!/usr/bin/python3

# Inicializar lista 

numeros = []

# Recorrer numeros del 1 al 100

for i in range (1,101):
    if (i%3==0 and i%4==0):
        # Añadir elemento a la lista
        numeros.append(i)

#Visualizar lista
print(str(numeros))


        

