class Yatzy:

    # Usamos el *args para poder para el número que queramos de parámetros.
    @staticmethod
    def chance(*args):
        total = 0
        for i in args:
            total += i
        return total

    @staticmethod
    def yatzy(*args):
        if len(set(args)) == 1:
            return 50
        else:
            return 0

    @staticmethod
    def ones(*args):
        total = 0
        for i in args:
            if i == 1:
                total += i
        return total

    @staticmethod
    def twos(*args):
        total = 0
        for i in args:
            if i == 2:
                total += i
        return total

    @staticmethod
    def threes(*args):
        total = 0
        for i in args:
            if i == 3:
                total += i
        return total

    @staticmethod
    def fours(*args):
        total = 0
        for i in args:
            if i == 4:
                total += i
        return total
    
    @staticmethod
    def fives(*args):
        total = 0
        for i in args:
            if i == 5:
                total += i
        return total
    
    @staticmethod
    def sixes(*args):
        total = 0
        for i in args:
            if i == 6:
                total += i
        return total
    
    @staticmethod
    def score_pair(*args):
        for i in range(6, 0, -1):
            if args.count(i) == 2:
                return i * 2
        return 0
    
    @staticmethod
    def two_pair(*args):
        counts = []
        score = 0
        for i in args:
            if args.count(i) > 1:
                if i not in counts:
                    counts.append(i)
                    i = i * args.count(i)
                    score += i
                    if len(counts) == 2:
                        return score
                    else:   
                        pass
        return 0

    @staticmethod
    def three_of_a_kind(*args):
        for i in args:
            if args.count(i) == 3:
                return i * 3
            else:
                return 0
    
    @staticmethod
    def four_of_a_kind(*args):
        for i in args:
            if args.count(i) == 4:
                return i * 4
            else:
                return 0
     

    @staticmethod
    def smallStraight(*args):
        for i in range(1,6):
            count = args.count(i)
            if count != 1:
                return 0
        return 15
    
    @staticmethod
    def largeStraight(*args):
        for i in range(2,6):
            count = args.count(i)
            if count != 1:
                return 0
        return 20

    @staticmethod
    def fullHouse(*args):

        score_pair = Yatzy.score_pair(*args)
        three_of_a_kind = Yatzy.three_of_a_kind(*args)
        maybeFullhouse = score_pair and three_of_a_kind

        if maybeFullhouse:
            return score_pair + three_of_a_kind
        else:
            return 0

    
