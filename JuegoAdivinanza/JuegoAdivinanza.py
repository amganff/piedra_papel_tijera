

import random


numero_secreto= random.randint(1,100)
cant_intentos=0
cant_max_int=5
adivinado=False

print("Welcome to the adivinanza game")

while not adivinado:
    if not cant_intentos < cant_max_int:
        print ("Game over! te quedaste sin chancess!")
        break

    numero=int(input("Introduce un número del 1 al 99: ")) #TODO: Convertir a Numero
    
    if numero== numero_secreto:
        print("Congrats,you adivinaste the secret numeber!!")
        adivinado= True
    elif numero < numero_secreto:
        print("The number is higher than you ingresed")
    else:
        print("El numero es menor al ingresado")
        cant_intentos+=1

      