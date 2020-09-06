#!/usr/bin/python3

# Estrcutura con funciones , bucles y condicionales 

creditos = ("Alberto Gonzlez", "oforte", 2016 )
infotweet = {}
listatweet = []
print("Bienvenidos a la aplicacion.")
usuario= input("Cual es tu usuario")
otro= "s"
i = 1 

def pedirtweet():
    tweet = None
    tweet = input("Que esta pasando")
    likes= 0
    retweets= 0 
    likes= int(input("Cuantos likes?"))
    retweets= int(input("Cuantos retweets"))
    infotweet= {"Autor": usuario,"Mensaje": tweet, "Likes": likes, "Retweets": retweets}
    return infotweet

def flistatweets(listatweet):
    for tweet in listatweet:
        print(str(tweet))
        likes = tweet['Likes']
        retweets = tweet['Retweets']
        if likes > 2:
            print("Su tweet tiene 'me gustas'")
        elif likes == 1:
            print("Su tweet solo tiene un me gusta")
        elif likes == 2:
            print("Su tweet solo tiene dos me gustas")
        else:
            print("Su tweet no tiene 'me gustas'")
        
        if (retweets > 0): print("Este tweet tiene retweets")

while otro == "s":
    print("Tweet numero:", i)
    i += 1
    infotweet= pedirtweet()
    listatweet.append(infotweet)
    otro = input ("Desea introducir un nuevo tweet? s/n:")

flistatweets(listatweet)
print("Esta instuccion se va ejecutar siempre")
