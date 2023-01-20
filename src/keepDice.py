def keepDice(keep,diceRoll):

    if len(keep) > 0:

        keep = keep.split(',')

        for i in range(0, len(keep)):
            keep[i] = int(keep[i])
    
        diceRoll.extend(keep)
        
    return diceRoll