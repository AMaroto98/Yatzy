from logicYatzy import Yatzy
import os
import time

os.system("clear")

palyerName = input("Introduce el nombre del jugador: ")

playerScore = {"Ones": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0,
             "ThreeOfAKind": 0, "FourOfAKind": 0, "FullHouse": 0, "smallStraight": 0,
             "largeStraight": 0, "Yatzy": 0, "Chance": 0}

def score(answer, diceRollThree):

    if answer == "Top" or answer == "top":

        scoreChoice = input("\n" + "Dónde quieres anotar los puntos? Ones, Twos, etc.? ")
        
        if scoreChoice == "Ones" or scoreChoice == "ones":
            playerScore.update({"Ones": Yatzy.ones(*diceRollThree)})

        elif scoreChoice == "Twos" or scoreChoice == "twos":
            playerScore.update({"Twos": Yatzy.twos(*diceRollThree)})

        elif scoreChoice == "Threes" or scoreChoice == "threes":
            playerScore.update({"Threes": Yatzy.threes(*diceRollThree)})

        elif scoreChoice == "Fours" or scoreChoice == "fours":
            playerScore.update({"Fours": Yatzy.fours(*diceRollThree)})

        elif scoreChoice == "Fives" or scoreChoice == "fives":
            playerScore.update({"Fives": Yatzy.fives(*diceRollThree)})

        elif scoreChoice == "Sixes" or scoreChoice == "sixes":
            playerScore.update({"Sixes": Yatzy.sixes(*diceRollThree)})
            
        else:
            print("Respuesta no valida.")

    # Puntuación de Top
    totalTop = 0
    bonusAdded = False

    for key in playerScore:
        if key in ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]:
            totalTop += playerScore[key]

        if totalTop >= 63 and not bonusAdded:
            totalTop += 35
            bonusAdded = True

    print("\n" + "Puntuación total de Top: " + str(totalTop))
 
    
    if answer == "Bot" or answer == "bot":

        scoreChoice = input("\n" + "Dónde quieres anotar los puntos? Three of a Kind, Four of a Kind, Full House etc.? ")

        if scoreChoice == "Three" or scoreChoice == "three":
            playerScore.update({"ThreeOfAKind": Yatzy.three_of_a_kind(*diceRollThree)})

        elif scoreChoice == "Four" or scoreChoice == "four":
            playerScore.update({"FourOfAKind": Yatzy.four_of_a_kind(*diceRollThree)})

        elif scoreChoice == "Full House" or scoreChoice == "full house" or scoreChoice == "fh":
            playerScore.update({"FullHouse": Yatzy.fullHouse(*diceRollThree)})

        elif scoreChoice == "Small" or scoreChoice == "small":
            playerScore.update({"smallStraight": Yatzy.smallStraight(*diceRollThree)})

        elif scoreChoice == "Large" or scoreChoice == "large":
            playerScore.update({"largeStraight": Yatzy.largeStraight(*diceRollThree)})

        elif scoreChoice == "Yatzy" or scoreChoice == "yatzy":
            playerScore.update({"Yatzy": Yatzy.yatzy(*diceRollThree)})

        elif scoreChoice == "Chance" or scoreChoice == "chance":
            playerScore.update({"Chance": Yatzy.chance(*diceRollThree)})
    
        else:
            print("Respuesta no valida.")

    # Puntuación de Bot
    totalBot = 0
    
    for key in playerScore:
        if key in ["ThreeOfAKind", "FourOfAKind", "FullHouse", "smallStraight", "largeStraight", "Yatzy", "Chance"]:
            totalBot += playerScore[key]

    print("\n" + "Puntuación total de Bot: " + str(totalBot))
 
    totalScore = totalTop + totalBot

    time.sleep(3)

    print("\n" + "Puntuación de " + str(palyerName) + "\n")

    for clave, valor in playerScore.items():
        print(clave + ": " + str(valor))

    time.sleep(2)

    print("\n" + "La puntuación total es de: " + str(totalScore) + "\n")

    time.sleep(2)

    print("Final del turno!" + "\n")