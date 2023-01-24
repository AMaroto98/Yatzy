def printDice(diceRoll):

    for i in range(len(diceRoll)):
        
        if i < len(diceRoll) - 1:
            print(diceRoll[i], end =" ")
        else:
            print(str(diceRoll[i]) + "\n")

def printTitle():

    print(
''' __        __   _                            _         __   __    _             
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   \ \ / /_ _| |_ _____   _ 
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \   \ V / _` | __|_  / | | |
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) |   | | (_| | |_ / /| |_| |
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/    |_|\__,_|\__/___|\__, |
                                                                          |___/  ''' + "\n")

def printWarning():

    print("If this is your first time I recommend you to read the rules of the game that you can find in the README of the project. \n")


def printEndTurn():

    print("End of shift" + "\n")

def timeToScore():

    print("Time to score: \n")