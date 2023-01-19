from logicYatzy import Yatzy
from printDice import printDice
from keepDice import keepDice
from randomNumbers import firstRoll, otherRolls
import os

os.system("clear")

print("Welcome to Yahtzee! \n")
print("If this is your first time I recommend you to read the rules of the game that you can find in the README of the project. \n")

# Tabla de puntuaciones
playerOne = {"Ones": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0,
             "ThreeOfAKind": 0, "FourOfAKind": 0, "FullHouse": 0, "smallStraight": 0,
             "largeStraight": 0, "Yatzy": 0, "Chance": 0}
 

# Bucle para tener un control de los turnos.
for roll in range(1,14):

    print("Turn number " + str(roll) + "!")

    # Lista en la que se van a almacenar los dados de la primera tirada.
    diceRollOne = []

    # Llamamos a la función FirstRoll para conseguir los primeros 5 dados.
    firstRoll(diceRollOne)

    # Mostramos dados de la primera tirada.
    print("Roll 1: ", end="")
    printDice(diceRollOne)

    # Dados que guarda el jugador para la segunda tirada.
    keep = input("Qué números de la tirada te gustaría mantener?")

    # Lista en la que se van a almacenar los dados de la segunda tirada.
    diceRollTwo = []

    # Llamamos a función KeepDice para guardar dados, en el caso en que se guarden.
    keepDice(keep, diceRollTwo)

    # Llamamos a la función otherRolls para juntar los dados guardados de jugadas anteriores y los nuevos.
    otherRolls(diceRollTwo, keep)
    
    # Llamamos función printDice para imprimir los dados de la segunda tirada.
    print("Roll 2: ", end ="")
    printDice(diceRollTwo)

    # Dados que guarda el jugador para la tercera tirada.
    keep = input("Qué números de la tirada te gustaría mantener?")

    # Lista en la que se van a almacenar los dados de la tercera tirada.
    diceRollThree = []

    # Llamamos a función KeepDice para guardar dados, en el caso en que se guarden.
    keepDice(keep, diceRollThree)

    # Llamamos a la función otherRolls para juntar los dados guardados de jugadas anteriores y los nuevos.
    otherRolls(diceRollThree, keep)

    # Bucle para imprimir los resultados del tercer y último Roll.
    print("Roll 3: ", end ="")
    printDice(diceRollThree)

    
    print("Ahora de anotar la puntuación \n")

    answer = input("Dónde quieres puntuar? En Top o en Bot?")

    # Top Score
    if answer == "Top":

        score_choice = input("Dónde quieres anotar los puntos? Ones, Twos, etc.? ")
        
        if score_choice == "Ones":
            playerOne.update({"Ones": Yatzy.ones(*diceRollThree)})
        elif score_choice == "Twos":
            playerOne.update({"Twos": Yatzy.twos(*diceRollThree)})
        elif score_choice == "Threes":
            playerOne.update({"Threes": Yatzy.threes(*diceRollThree)})
        elif score_choice == "Fours":
            playerOne.update({"Fours": Yatzy.fours(*diceRollThree)})
        elif score_choice == "Fives":
            playerOne.update({"Fives": Yatzy.fives(*diceRollThree)})
        elif score_choice == "Sixes":
            playerOne.update({"Sixes": Yatzy.sixes(*diceRollThree)})
        
    # Bot Score
    elif answer == "Bot":

        score_choice = input("Dónde quieres anotar los puntos? Three of a Kind, Four of a Kind, Full House etc.? ")
        if score_choice == "Three":
            playerOne.update({"ThreeOfAKind": Yatzy.three_of_a_kind(*diceRollThree)})
        if score_choice == "Four":
            playerOne.update({"FourOfAKind": Yatzy.four_of_a_kind(*diceRollThree)})
        if score_choice == "Full House":
            playerOne.update({"FullHouse": Yatzy.fullHouse(*diceRollThree)})
        if score_choice == "Small":
            playerOne.update({"smallStraight": Yatzy.smallStraight(*diceRollThree)})
        if score_choice == "Large":
            playerOne.update({"largeStraight": Yatzy.largeStraight(*diceRollThree)})
        if score_choice == "Yatzy":
            playerOne.update({"Yatzy": Yatzy.yatzy(*diceRollThree)})
        if score_choice == "Chance":
            playerOne.update({"Chance": Yatzy.chance(*diceRollThree)})
    
    else:
        print("Respuesta no valida.")

    totalScore = sum(playerOne.values())

    print(totalScore)