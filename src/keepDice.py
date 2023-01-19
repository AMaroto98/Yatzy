def keepDice(keep,diceRoll):

    if len(keep) > 0:
        keep = keep.split(',')

         # Bucle para transformar los String de los dados guardados a Integers.
        for i in range(0, len(keep)):
            keep[i] = int(keep[i])
        
    return diceRoll.extend(keep)