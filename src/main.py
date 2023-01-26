from randomNumbers import RandomNumbers
from prints import printDice, printTitle, printWarning, printEndTurn, timeToScore
from keepDice import keepDice
from score import score
import time
import os

os.system("clear")

printTitle()

time.sleep(2)

printWarning()

time.sleep(4)
 
# Bucle para tener un control de los turnos.
for roll in range(1,14):

    print("Turn number " + str(roll) + "!" + "\n")

    time.sleep(2)

    # Lista en la que se van a almacenar los dados de la primera tirada.
    diceRollOne = []

    # Llamamos a la función FirstRoll para conseguir los primeros 5 dados.
    RandomNumbers.firstRoll(diceRollOne)

    # Mostramos dados de la primera tirada.
    print("Roll 1: ", end="")
    printDice(diceRollOne)

    time.sleep(3)

    # Dados que guarda el jugador para la segunda tirada.
    keep = input("What dice would you like to keep? ")

    # Lista en la que se van a almacenar los dados de la segunda tirada.
    diceRollTwo = []

    # Llamamos a función KeepDice para guardar dados, en el caso en que se guarden.
    keepDice(keep, diceRollTwo)

    # Llamamos a la función otherRolls para juntar los dados guardados de jugadas anteriores y los nuevos.
    RandomNumbers.otherRolls(diceRollTwo, keep)
    
    # Llamamos función printDice para imprimir los dados de la segunda tirada.
    print("\n" + "Roll 2: ", end ="")
    printDice(diceRollTwo)

    time.sleep(3)

    # Dados que guarda el jugador para la tercera tirada.
    keep = input("What dice would you like to keep? ")

    # Lista en la que se van a almacenar los dados de la tercera tirada.
    diceRollThree = []

    # Llamamos a función KeepDice para guardar dados, en el caso en que se guarden.
    keepDice(keep, diceRollThree)

    # Llamamos a la función otherRolls para juntar los dados guardados de jugadas anteriores y los nuevos.
    RandomNumbers.otherRolls(diceRollThree, keep)

    # Bucle para imprimir los resultados del tercer y último Roll.
    print("\n" + "Roll 3: ", end ="")
    printDice(diceRollThree)

    time.sleep(3)

    timeToScore()

    time.sleep(2)

    try:
        answer = input("Where do you want to score? Top or Bot? ").lower()
        if answer != "top" and answer != "bot":
            raise TypeError
            
    except TypeError:
        print("Only 'top' or 'bot' values are allowed.")

    # Llamamos a la funcion score para anotar la puntuación de la ronda.
    score(answer, diceRollThree)

    time.sleep(2)

    printEndTurn()

print("End of game")