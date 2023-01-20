from logicYatzy import Yatzy

playerOne = {"Ones": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0,
             "ThreeOfAKind": 0, "FourOfAKind": 0, "FullHouse": 0, "smallStraight": 0,
             "largeStraight": 0, "Yatzy": 0, "Chance": 0}

def score(answer, diceRollThree):

    if answer == "Top" or answer == "top":

        scoreChoice = input("\n" + "Dónde quieres anotar los puntos? Ones, Twos, etc.? ")
        
        if scoreChoice == "Ones" or scoreChoice == "ones":
            playerOne.update({"Ones": Yatzy.ones(*diceRollThree)})

        elif scoreChoice == "Twos" or scoreChoice == "twos":
            playerOne.update({"Twos": Yatzy.twos(*diceRollThree)})

        elif scoreChoice == "Threes" or scoreChoice == "threes":
            playerOne.update({"Threes": Yatzy.threes(*diceRollThree)})

        elif scoreChoice == "Fours" or scoreChoice == "fours":
            playerOne.update({"Fours": Yatzy.fours(*diceRollThree)})

        elif scoreChoice == "Fives" or scoreChoice == "fives":
            playerOne.update({"Fives": Yatzy.fives(*diceRollThree)})

        elif scoreChoice == "Sixes" or scoreChoice == "sixes":
            playerOne.update({"Sixes": Yatzy.sixes(*diceRollThree)})
            
        else:
            print("Respuesta no valida.")
    
    if answer == "Bot" or answer == "bot":

        scoreChoice = input("\n" + "Dónde quieres anotar los puntos? Three of a Kind, Four of a Kind, Full House etc.? ")

        if scoreChoice == "Three" or scoreChoice == "three":
            playerOne.update({"ThreeOfAKind": Yatzy.three_of_a_kind(*diceRollThree)})

        elif scoreChoice == "Four" or scoreChoice == "four":
            playerOne.update({"FourOfAKind": Yatzy.four_of_a_kind(*diceRollThree)})

        elif scoreChoice == "Full House" or scoreChoice == "full house" or scoreChoice == "fh":
            playerOne.update({"FullHouse": Yatzy.fullHouse(*diceRollThree)})

        elif scoreChoice == "Small" or scoreChoice == "small":
            playerOne.update({"smallStraight": Yatzy.smallStraight(*diceRollThree)})

        elif scoreChoice == "Large" or scoreChoice == "large":
            playerOne.update({"largeStraight": Yatzy.largeStraight(*diceRollThree)})

        elif scoreChoice == "Yatzy" or scoreChoice == "yatzy":
            playerOne.update({"Yatzy": Yatzy.yatzy(*diceRollThree)})

        elif scoreChoice == "Chance" or scoreChoice == "chance":
            playerOne.update({"Chance": Yatzy.chance(*diceRollThree)})
    
        else:
            print("Respuesta no valida.")

    totalScore = sum(playerOne.values())

    print("\n" + "PUNTUACIÓN" + "\n")

    for clave, valor in playerOne.items():
        print(clave + ": " + str(valor))

    print("\n" + "La puntuación total es de: " + str(totalScore) + "\n")
