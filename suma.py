# Programa suma por Juan Romero 

# Importar funcion que permite mantener en pantalla
import msvcrt

print ("Programa que suma dos numeros que se digitan\n")

print ("Digite el valor de A")
a= input("Valor de A= ")

print ("\n Digite el valor de B")
b= input("Valor de B= ")

valora = int (a)
valorb = int (b) 

c= valora + valorb

print("\nSuma= ",c)

print (" \n Digite Enter para finalizar")

# Mantener en pantalla hasta que le de enter
# msvcrt.getch() Solo para windows 

# Para todo sistema operativo
raw_input()


