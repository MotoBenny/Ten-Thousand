
from random import randint, sample
from collections import Counter


class GameLogic:

    def __init__(self):
        pass

    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1,6) for _ in range(0,num_dice))
        # or
        # return tuple(sample(range(1, 6 + 1), num_dice))

    @staticmethod
    def calculate_score(roll):
        """
        this makes me wanna vomit
        """
        count = Counter(roll).most_common()
        score = 0

        if len(count) is 6:  # covers us for straight
            score += 1500
            return score

        if count == [(5, 2)]:
            return 100

        if count == [(1, 2)]:
            return 200

        if count == [(1, 3),(5, 1)]:
            return 1050

        if count == [(1, 3),(2, 3)]:
            return 1200

        if (1, 3) or (2, 3) or (3, 3) or (4, 3) or (5, 3) or (6, 3) in count:
            if (1, 3) in count:
                return 1000
            if (2, 3) in count:
                return 200
            if (3, 3) in count:
                return 300
            if (4, 3) in count:
                return 400
            if (5, 3) in count:
                return 500
            if (6, 3) in count:
                return 600

        if (1, 6) or (2, 6) or (3, 6) or (4, 6) or (5, 6) or (6, 6) in count:
            if count == [(1, 6)]:
                return 4000
            if count == [(2, 6)]:
                return 800
            if count == [(3, 6)]:
                return 1200
            if count == [(4, 6)]:
                return 1600
            if count == [(5, 6)]:
                return 2000
            if count == [(6, 6)]:
                return 2400

        if (1, 4) or (2, 4) or (3, 4) or (4, 4) or (5, 4) or (6, 4) in count:
            if count == [(1, 4)]:
                return 2000
            if count == [(2, 4)]:
                return 400
            if count == [(3, 4)]:
                return 600
            if count == [(4, 4)]:
                return 800
            if count == [(5, 4)]:
                return 1000
            if count == [(6, 4)]:
                return 1200

        if (1, 5) or (2, 5) or (3, 5) or (4, 5) or (5, 5) or (6, 5) in count:
            if count == [(1, 5)]:
                return 3000
            if count == [(2, 5)]:
                return 600
            if count == [(3, 5)]:
                return 900
            if count == [(4, 5)]:
                return 1200
            if count == [(5, 5)]:
                return 1500
            if count == [(6, 5)]:
                return 1800

        if count == [(2, 2),(3, 2),(6, 2)]:
            return 1500

        if roll == (5,): # (5,)
            return 50

        if roll == (1,): # (5,)
            return 100

        if 1 and 5 in roll:
            return 150
        # put all non scoring rolls in else.
        if (2, 2) or (6, 2) or (3, 2) or (4, 2) in count:  # covers us for non-scoring pairs
            return 0

        if count == [(4, 1),(6, 1),(3, 2),(2, 2)]: # test this weird roll
            return 0

        if len(count) is 0:  # covers us for ziltch
            return 0


class Banker():

    def shelf(self, points):
        pass

    def bank():
        pass

    def clear_shelf(self):
        pass