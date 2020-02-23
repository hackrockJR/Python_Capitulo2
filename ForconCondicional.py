# Control de flujo 

creditos = ("Juan Romero", "HACKROCK" , 2020)

tweet2= None 
likes2 = 0
retweets2 = 0
infotweet = {}
listatweet2 = [] 

print ("Bienvenido a la aplicacion")

usuario= input ("Cual es tu usuario ")
for i in [1,2,3]:
    print("Tweet numero: ", i)
    tweet2 = input ("Que esta pasando? ")
    likes2 = int (input ("Cuantos likes? ")) 
    retweets2 = int (input ("Cuantos retweets? "))
    infotweet = {"Autor": usuario, "Mensaje": tweet2 , "likes": likes2 , "retweets": retweets2 } 
    listatweet2.append(infotweet)
    # Declare una variable porque no me funciona imprimir directamente. 
    #valorinfotweet = str (infotweet)
    #print (valorinfotweet)

    #Condicional 

    # Los condicionales se ejecutan dentro del espacio que tabula el IF y/o el else

    # Cuando agregas if distintos de sus condiciones se debe dejar fuera del anterior , en este caso likes2 y retweets2
    # Pudeo agregar la condicion antes o despues de otro if : if retweets2>0: print("Este tweets tiene Retweets")

    if likes2 == 1:
        print("Su tweet tiene su primer me gustas")
    #elif es un if anidado 
    elif likes2 > 1:
            print ("Tiene varios me gusta")

    else:
        print("Aun no tiene me gustas :( ")

    if retweets2>0: print("Este tweets tiene Retweets")
#Con cualquier valor de la lista (likes2 o tweet2) listatweet2 se puede mandar a imprimir el diccionario infotweet 
for tweet2 in listatweet2:
    print(str(tweet2))
print ("\nEsta salida se ejecuta fuera del if")

# Salida del bucle y condicional> 

#Bienvenido a la aplicacion
#Cual es tu usuario Romero1
#Tweet numero:  1
#Que esta pasando? Nada
#Cuantos likes? 2
#Cuantos retweets? 2
#Tiene varios me gusta
#Este tweets tiene Retweets
#Tweet numero:  2
#Que esta pasando? nada
#Cuantos likes? 3
#Cuantos retweets? 3
#Tiene varios me gusta
#Este tweets tiene Retweets
#Tweet numero:  3
#Que esta pasando? nada
#Cuantos likes? 4
#Cuantos retweets? 4
#Tiene varios me gusta
#Este tweets tiene Retweets
#{'Autor': 'Romero1', 'Mensaje': 'Nada', 'likes': 2, 'retweets': 2}
#{'Autor': 'Romero1', 'Mensaje': 'nada', 'likes': 3, 'retweets': 3}
#{'Autor': 'Romero1', 'Mensaje': 'nada', 'likes': 4, 'retweets': 4}






