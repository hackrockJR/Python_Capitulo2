#!/usr/bin/env python
#_*_ coding: utf8 _*_

# Uso de for 

total=0 

for numero in [1,3,5]:
    print("numero",numero)
    total += numero
    print ("total= ",total)

print ("La suma total es de= ",total)

# Salida del programa , numero toma el valor de la cadena y tota suma ese valor hasta que se llegue al ultimo numero

#numero 1
#total=  1
#numero 3
#total=  4
#numero 5
#total=  9
# La suma total es de=  9

# For imprime caracteres 

print("\nImprimir caracteres")
for letra in "ROMERO":
    print("Letra: ",letra)

# Salida > 

#Imprimir caracteres
#Letra:  R
#Letra:  O
#Letra:  M
#Letra:  E
#Letra:  R
#Letra:  O

#Podemos finalizar con un condicional el bucle y usando el parametro break para deifir que ahi terminara.
# Se debe tener cuidado con la posicion de break en el if si no queda fuera y no aplica. 
print("\nImprimir caracteres")
for letra in "ROMEROMEJIA":
    if letra == "J":
        break # Salir del bucle 
    print("Letra: ",letra)

print("\nImprimir caracteres")
for letra in "FERNANDOMEJIA":
    if letra == "J":
        continue # realizara un salto , para continuar sin imprimir la letra del condicional. 
    print("Letra: ",letra)



