from logicYatzy import Yatzy

playerOne = {"Ones": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0,
             "ThreeOfAKind": 0, "FourOfAKind": 0, "FullHouse": 0, "smallStraight": 0,
             "largeStraight": 0, "Yatzy": 0, "Chance": 0}

def score(answer, diceRollThree):

    if answer == "Top" or answer == "top":

        scoreChoice = input("Dónde quieres anotar los puntos? Ones, Twos, etc.? ")
        
        if scoreChoice == "Ones":
            playerOne.update({"Ones": Yatzy.ones(*diceRollThree)})

        elif scoreChoice == "Twos":
            playerOne.update({"Twos": Yatzy.twos(*diceRollThree)})

        elif scoreChoice == "Threes":
            playerOne.update({"Threes": Yatzy.threes(*diceRollThree)})

        elif scoreChoice == "Fours":
            playerOne.update({"Fours": Yatzy.fours(*diceRollThree)})

        elif scoreChoice == "Fives":
            playerOne.update({"Fives": Yatzy.fives(*diceRollThree)})

        elif scoreChoice == "Sixes":
            playerOne.update({"Sixes": Yatzy.sixes(*diceRollThree)})
            
        else:
            print("Respuesta no valida.")
    
    if answer == "Bot" or answer == "bot":

        scoreChoice = input("Dónde quieres anotar los puntos? Three of a Kind, Four of a Kind, Full House etc.? ")

        if scoreChoice == "Three":
            playerOne.update({"ThreeOfAKind": Yatzy.three_of_a_kind(*diceRollThree)})

        elif scoreChoice == "Four":
            playerOne.update({"FourOfAKind": Yatzy.four_of_a_kind(*diceRollThree)})

        elif scoreChoice == "Full House":
            playerOne.update({"FullHouse": Yatzy.fullHouse(*diceRollThree)})

        elif scoreChoice == "Small":
            playerOne.update({"smallStraight": Yatzy.smallStraight(*diceRollThree)})

        elif scoreChoice == "Large":
            playerOne.update({"largeStraight": Yatzy.largeStraight(*diceRollThree)})

        elif scoreChoice == "Yatzy":
            playerOne.update({"Yatzy": Yatzy.yatzy(*diceRollThree)})

        elif scoreChoice == "Chance":
            playerOne.update({"Chance": Yatzy.chance(*diceRollThree)})
    
        else:
            print("Respuesta no valida.")

    totalScore = sum(playerOne.values())

    print("La puntuación total es de: " + str(totalScore))