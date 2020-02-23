Python capitulo 2 

INDICE>> 

clase 0 

{
""" comentar 
varias
lineas """

# o comentar una soloa linea

}

1- Clase1.py
{

# Clase 1 de Operadores y Entrada y salida de datos. 
# Operadores 
# Aritmeticos + - * / % ** //
# Asignacion = ; likes = 4
# Sumar += (cantidad) o Multiplicar *= (cantidad)
# Operador comparacion == != <>
# Operador pertenencia , regresa valor True or False ; 2 in [2,3,4]
# Operador identidad is , is not
}

2- entradas.py

{

# Entrada de texto ; input
# Salida ; print 
# Control de flujo 
# Error JR01 Esta salida no me funciona> print ("\n" str(infotweet))
# Esta si funciona para imprimir con otra variable valorinfotweet = str (infotweet)
print (valorinfotweet)

}

3- suma.py 

{
# Pruebas de entrada y salida de datos
# Programa para ejecutar en una shell de windows o linux
# Importar funcion que permite mantener en pantalla
import msvcrt
# Mantener en pantalla hasta que le de enter
# Segun solo para windows 
# se deja al final de la linea
 msvcrt.getch()  
}

4 - Condicional.py
{
# Control de flujo 
# Declare una variable porque no me funciona imprimir directamente. 
# Los condicionales se ejecutan dentro del espacio que tabula el IF y/o el else
# Cuando agregas if distintos de sus condiciones se debe dejar fuera del anterior , en este caso likes2 y retweets2
# Pudeo agregar la condicion antes o despues de otro if : if retweets2>0: print("Este tweets tiene Retweets")
# elif es un if anidado

}

5- Bucle_interacion.py

{
# Uso de for
# For imprime numeros de una lista 
# For imprime caracteres de una lista 
# Podemos finalizar con un condicional (if) el bucle y usando el parametro break para deifir que ahi terminara.
# Se debe tener cuidado con la posicion de break en el if si no queda fuera y no aplica. 
# break # Salir del bucle e imprime lo que se define en el condicional.
# continue # realizara un salto , para continuar sin imprimir la letra del condicional(if), hasta finalizar el bucle.

}

6- ForconCondicional.py

{

# Solicitar al usuario agregar mas de un formulario a llenar
# uso de append para agregar informacion contenida en un diccionario en una lista y luego imprimir.
listatweet2.append(infotweet)
# Declaracion del ciclo for 
for i in [1,2,3]:
# todo lo que este dentro de la tabulacion del for o espacio caera en el ciclo. 
# el cliclo de vida del for se puede definir como una lista
[1,2,3] 
# Imprimir el resultado
#Con cualquier variable de la lista (likes2 o tweet2) listatweet2 se puede mandar a imprimir el diccionario infotweet 
for tweet2 in listatweet2:
    print(str(tweet2))
# Imprimir fuera del for o if ,else , while 
# se debe colocar fuera de la tabulacion o espacio definido
print ("\nEsta salida se ejecuta fuera del if")

7- while.py

{
# Inicializar una variable  num = 0
# definir la condicion para finalizar <= 10 
# Imprimir 
# definir el incremento num += 1

}

8- whileconCondicional.py
{
# Definir variable de incremento
# Definir el valor de la variable igual a True tipo booleano
# Para imprimir mantenemos el for del programa ForconCondicional.py


}

9- whileconCondicionalsintrue

{
# Definir variable de incremento
# Definir el valor de la variable igual a True tipo booleano   
# En la siguiente linea debera decidir si declarar una variable con valor booleano o con una cadena
# Si se declara cadena , solo basta con que el usuario digite el valor que hace terminar el bucle
# En este caso usaremos la cadena s  
# definir la condicion para cuando la entrada sea s volver entrar al bucle
if retweets2>0: print("Este tweets tiene Retweets")
    otro = input("Desea introducir un nuevo tweet? s/n: ")
    if otro == "s": 
        otrotweet2 = True
    else:    
        otrotweet2 = False
}

10- Funcion_range.py 

{

# Devuelve una lista con un rango de numero 
# Sintaxis range(n) genera una lista desde 0 hasta n-1 
# Definir rango de inicio y final-1 (n,m)
# Desde 1 al 10 , con saltos o incrementos de 2 (n,m,s)

}









