nombre1= input ("Como se llama el jugador 1?: ")
nombre2= input ("Como se llama el jugador 2?: ")


jugador1 = input("Hi "+ nombre1+ " What will you choose? piedra,papel or tijera?: ").strip().lower()

while jugador1 != "piedra" and jugador1 != "papel" and jugador1 != "tijera":
    jugador1 = input("Heey "+ nombre1+ " esa opcion no es valida!!, podes elegir piedra,papel or tijera?: ").strip().lower()



jugador2 = input("Hi "+ nombre2+ " What will you choose? piedra,papel or tijera?: ").strip().lower()

while jugador2 != "piedra" and jugador2 != "papel" and jugador2 != "tijera":
    jugador2 = input("Heey "+ nombre2+ " esa opcion no es valida!!, podes elegir piedra,papel or tijera?: ").strip().lower()

condicion1= jugador1== "piedra" and jugador2 == "tijera"
condicion2= jugador1== "papel" and jugador2 == "piedra"
condicion3= jugador1== "tijera" and jugador2 == "papel"

if jugador1 == jugador2:
    print("Empate")
elif condicion1 or condicion2 or condicion3:
    print("Gana ", nombre1)
else:
    print("Gana ",nombre2)