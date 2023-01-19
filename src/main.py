from logicYatzy import Yatzy
import random
import os

os.system("clear")

print("Welcome to Yahtzee! \n")
print("If this is your first time I recommend you to read the rules of the game that you can find in the README of the project. \n")

# Tabla de puntuaciones
playerOne = {"Ones": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0,
             "ThreeOfAKind": 0, "FourOfAKind": 0, "FullHouse": 0, "smallStraight": 0,
             "largeStraight": 0, "Yatzy": 0, "Chance": 0}
 

# Bucle para tener un control de los turnos. Poner range de 14 de nuevo
for roll in range(1,3):
    print("Turn number " + str(roll) + "!")
    # Lista en la que se van a almacenar las tiradas de los dados
    diceRollOne = []
    for roll in range(5):
        # Añade a la lista un número aleatorio entre 1 y 6.
        diceRollOne.append(random.randint(1,6))

    # Mostramos dados de la primera tirada
    print("Roll 1: ", end="")
    for i in range(len(diceRollOne)):
        if i < len(diceRollOne) - 1:
            print(diceRollOne[i], end =" ")
        else:
            print(diceRollOne[i])

    # Dados que guarda el jugador para la próxima tirada.
    # Faltan más condiciones, por si no quiere guardar ninguno.
    keep = input("Qué números de la tirada te gustaría mantener?")

    diceRollTwo = []
    if len(keep) > 0:
        keep = keep.split(',')

        # Bucle para transformar los String de los dados guardados a Integers.
        for i in range(0, len(keep)):
            keep[i] = int(keep[i])
        
        # Añadimos los dados guardados a la siguiente jugada.
        diceRollTwo.extend(keep)

    print("Roll 2: ", end ="")
    for i in range(5 - len(keep)):

        # Más adelante refactorizar esto, de momento se queda así para tener un control de lo que ocurre
        randomDice = random.randint(1,6)
        diceRollTwo.append(randomDice)
    
    # Bucle para Imprimir los resultados del segundo Roll.
    for i in range(len(diceRollTwo)):
        
        if i < len(diceRollTwo) - 1:
            print(diceRollTwo[i], end =" ")
        else:
            print(diceRollTwo[i])

    # Dados que guarda el jugador para la próxima tirada.
    # Faltan más condiciones, por si no quiere guardar ninguno.
    keep = input("Qué números de la tirada te gustaría mantener?")

    diceRollThree = []

    if len(keep) > 0:
        keep = keep.split(',')

         # Bucle para transformar los String de los dados guardados a Integers.
        for i in range(0, len(keep)):
            keep[i] = int(keep[i])
        
        # Añadimos los dados guardados a la siguiente jugada.
        diceRollThree.extend(keep)

    print("Roll 3: ", end ="")
    for i in range(5 - len(keep)):

        # Más adelante refactorizar esto, de momento se queda así para tener un control de lo que ocurre
        randomDice = random.randint(1,6)
        diceRollThree.append(randomDice)
    
    # Bucle para imprimir los resultados del tercer Roll.
    for i in range(len(diceRollThree)):
        
        if i < len(diceRollThree) - 1:
            print(diceRollThree[i], end =" ")
        else:
            print(diceRollThree[i])

    print("Hora de anotar la puntuación \n")

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
        elif score_choice == "Four":
            playerOne.update({"FourOfAKind": Yatzy.four_of_a_kind(*diceRollThree)})
        elif score_choice == "Full":
            playerOne.update({"FullHouse": Yatzy.fullHouse(*diceRollThree)})
        elif score_choice == "Small":
            playerOne.update({"smallStraight": Yatzy.smallStraight(*diceRollThree)})
        elif score_choice == "Large":
            playerOne.update({"largeStraight": Yatzy.largeStraight(*diceRollThree)})
        elif score_choice == "Yatzy":
            playerOne.update({"Yatzy": Yatzy.yatzy(*diceRollThree)})
        elif score_choice == "Chance":
            playerOne.update({"Chance": Yatzy.chance(*diceRollThree)})
    
    else:
        print("Respuesta no valida.")

    totalScore = sum(playerOne.values())

    print(totalScore)