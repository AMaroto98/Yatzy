import random
class RandomNumbers:

    @staticmethod
    def firstRoll(diceRoll):

        for roll in range(5):
        
            diceRoll.append(random.randint(1,6))

        return diceRoll

    @staticmethod
    def otherRolls(diceRoll, keep):

        if len(keep) > 0:

            keep = keep.split(',')

            for i in range(0, len(keep)):
                keep[i] = int(keep[i])

        for i in range(5 - len(keep)):

            randomDice = random.randint(1,6)
            diceRoll.append(randomDice)

        return diceRoll