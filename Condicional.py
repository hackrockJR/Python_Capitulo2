# Control de flujo 

creditos = ("Juan Romero", "HACKROCK" , 2020)

tweet2= None 
likes2 = 0
retweets2 = 0
infotweet = {}

print ("Bienvenido a la aplicacion")

usuario= input ("Cual es tu usuario ")
tweet2 = input ("Que esta pasando? ")
likes2 = int (input ("Cuantos likes? ")) 
retweets2 = input ("Cuantos retweets? ")
infotweet = {"Autor": usuario, "Mensaje": tweet2 , "likes": likes2 , "retweets": retweets2 } 

# Declare una variable porque no me funciona imprimir directamente. 
valorinfotweet = str (infotweet)
print (valorinfotweet)

#Condicional 

# Los condicionales se ejecutan dentro del espacio que tabula el IF y/o el else

if likes2 == 1:
    print("Su tweet tiene su primer me gustas")
#elif es un if anidado 
elif likes2 > 1:
        print ("Tiene varios me gusta")
else:
    print("Aun no tiene me gustas :( ")

print ("\nEsta salida se ejecuta fuera del if")



