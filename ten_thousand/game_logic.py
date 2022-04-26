
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
        Calculates the score based on a given dice roll.
        """
        score = 0
        counts = Counter(roll)
        fives_used = False
        ones_used = False

        for num in range(1, 6 + 1):
            occurance_count = counts[num]

            if len(counts) is 6:
                score += 1500
                return score

            if len(counts) is 3:
                score += 1500
                return score

            if len(counts) is 2:
                score += 1200
                return score

            if occurance_count >= 3:

                value_add = num * 100
                score = value_add
                bonus_occurances = occurance_count - 3
                score += bonus_occurances * value_add

                if num == 1:
                    ones_used = True
                    score *= 10

                if num == 5:
                    fives_used = True
            # use this
        if not ones_used:
            score += counts[1] * 100

        if not fives_used:
            score += counts[5] * 50
        return score


class Banker(GameLogic):
    shelf_holding = 0
    total = 0

    def __init__(self):
        self.shelved = 0
        self.balance = 0

    def shelf(self, score):
        self.shelved += score
        return

    def bank(self):
        self.balance = self.shelved
        self.shelved = 0

    def clear_shelf(self):
        self.shelved = 0