def printDice(diceRoll):

    for i in range(len(diceRoll)):
        
        if i < len(diceRoll) - 1:
            print(diceRoll[i], end =" ")
        else:
            print(diceRoll[i])

    pass