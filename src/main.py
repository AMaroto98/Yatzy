from logicYatzy import Yatzy
from printDice import printDice
from keepDice import keepDice
from score import score
from randomNumbers import firstRoll, otherRolls
import os

os.system("clear")

print("Welcome to Yahtzee! \n")
print("If this is your first time I recommend you to read the rules of the game that you can find in the README of the project. \n")
 
# Bucle para tener un control de los turnos.
for roll in range(1,14):

    print("Turn number " + str(roll) + "!" + "\n")

    # Lista en la que se van a almacenar los dados de la primera tirada.
    diceRollOne = []

    # Llamamos a la función FirstRoll para conseguir los primeros 5 dados.
    firstRoll(diceRollOne)

    # Mostramos dados de la primera tirada.
    print("Roll 1: ", end="")
    printDice(diceRollOne)

    # Dados que guarda el jugador para la segunda tirada.
    keep = input("Qué números de la tirada te gustaría mantener? ")

    # Lista en la que se van a almacenar los dados de la segunda tirada.
    diceRollTwo = []

    # Llamamos a función KeepDice para guardar dados, en el caso en que se guarden.
    keepDice(keep, diceRollTwo)

    # Llamamos a la función otherRolls para juntar los dados guardados de jugadas anteriores y los nuevos.
    otherRolls(diceRollTwo, keep)
    
    # Llamamos función printDice para imprimir los dados de la segunda tirada.
    print("\n" + "Roll 2: ", end ="")
    printDice(diceRollTwo)

    # Dados que guarda el jugador para la tercera tirada.
    keep = input("Qué números de la tirada te gustaría mantener? ")

    # Lista en la que se van a almacenar los dados de la tercera tirada.
    diceRollThree = []

    # Llamamos a función KeepDice para guardar dados, en el caso en que se guarden.
    keepDice(keep, diceRollThree)

    # Llamamos a la función otherRolls para juntar los dados guardados de jugadas anteriores y los nuevos.
    otherRolls(diceRollThree, keep)

    # Bucle para imprimir los resultados del tercer y último Roll.
    print("\n" + "Roll 3: ", end ="")
    printDice(diceRollThree)

    print("Hora de anotar la puntuación \n")

    answer = input("Dónde quieres puntuar? En Top o en Bot? ")

    # Llamamos a la funcion score para anotar la puntuación de la ronda.
    score(answer, diceRollThree)
    
    # Print para saber que el turno acaba
    print("Final del turno!")