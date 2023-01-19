import random

def firstRoll(diceRoll):

    for roll in range(5):
        # Añade a la lista un número aleatorio entre 1 y 6.
    
        roll = diceRoll.append(random.randint(1,6))

    return roll

def otherRolls(diceRoll, keep):

    if len(keep) > 0:

        keep = keep.split(',')

        for i in range(0, len(keep)):
            keep[i] = int(keep[i])

    for i in range(5 - len(keep)):

        # Más adelante refactorizar esto, de momento se queda así para tener un control de lo que ocurre
        randomDice = random.randint(1,6)
        roll = diceRoll.append(randomDice)

    return roll
