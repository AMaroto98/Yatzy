from logicYatzy import Yatzy
import random

print("Welcome to Yahtzee! \n")
print("If this is your first time I recommend you to read the rules of the game that you can find in the README of the project. \n")

# Tabla de puntuaciones
playerOne = {"Ace": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0,
             "ThreeOfAKind": 0, "FourOfAKind": 0, "FullHouse": 0, "smallStraight": 0,
             "largeStraight": 0, "Yathzee": 0, "Chance": 0}
 
totalScore: 0


# Bucle para tener un control de los turnos. Poner range de 14 de nuevo
for roll in range(1,2):
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
    if len(keep) < 0:
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

    if len(keep) < 0:
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
    
    # Bucle para Imprimir los resultados del segundo Roll.
    for i in range(len(diceRollThree)):
        
        if i < len(diceRollThree) - 1:
            print(diceRollThree[i], end =" ")
        else:
            print(diceRollThree[i])

