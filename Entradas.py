#!usr/bin/python3.8

# Entrada de texto

tweet = input ("Que esta pasando? ")
# print(tweet)

# Salida 

print ("Esta es la salida") 
print ("Su comentario es ", tweet)


# Control de flujo 

creditos = ("Juan Romero", "HACKROCK" , 2020)

tweet2= None 
likes2 = 0
retweets2 = 0
infotweet = {}

print ("Bienvenido a la aplicacion")

usuario= input ("Cual es tu usuario ")
tweet2 = input ("Que esta pasando? ")
likes2 = input ("Cuantos likes? ")
retweets2 = input ("Cuantos retweets? ")
infotweet = {"Autor": usuario, "Mensaje": tweet2 , "likes": likes2 , "retweets": retweets2 } 

# Declare una variable porque no me funciona imprimir directamente. 
valorinfotweet = str (infotweet)
print (valorinfotweet)

# Error JR01 Esta salida no me funciona> print ("\n" str(infotweet))













