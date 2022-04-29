
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
    def get_scorers(dice):
        dice_list = []
        for num in dice:
            if num == 1:
                dice_list.append(num)
            elif num == 5:
                dice_list.append(num)
        return tuple(dice_list)

    @staticmethod # if we take in roll_input it will be a clean string
    def validate_keepers(roll, user_input):
        striped_roll = roll.replace(" ",'')
        roll_most_common = Counter(striped_roll).most_common()
        input_most_common = Counter(user_input).most_common()
        for i in range(len(input_most_common)):
            if input_most_common[i][1] > roll_most_common[i][1]:
                print("Cheater!!! Or possibly made a typo...")
                return False
            else:
                return True

    @staticmethod
    def calculate_score(roll):
        """
        Calculates the score based on a given dice roll.
        """
        score = 0
        counts = Counter(roll)
        counts_pairs = Counter(roll).most_common()
        if len(roll) == 0:
            return score

        if len(counts_pairs) == 6:
            GameLogic.how_many = 6
            return 1500

        pair = 0
        if len(roll) == 6 and len(counts_pairs) == 3:
            for i in range(3):
                if counts_pairs[i][1] == 2:
                    pair += 1
        if pair == 3:
            GameLogic.how_many = 6
            return 1500

        else:
            for i in range(len(counts_pairs)):
                number = counts_pairs[i][0]
                common = counts_pairs[i][1]
                base = number * 100
                if number == 1:
                    if common > 2:
                        base = number * 1000
                    else:
                        score += base * common
                if number == 5:
                    if common < 3:
                        score += number * 10 * common
                if common > 2:
                    score += base * (common - 2)
        return score


class Banker(GameLogic):

    def __init__(self):
        self.balance = 0 #
        self.shelved = 0 # 200

    def bank(self):
        amount_deposited = self.shelved # 200
        self.balance += self.shelved # 200
        self.shelved = 0
        return amount_deposited # 200

    def shelf(self, amt): # for amt = 200
        self.shelved += amt

    def clear_shelf(self):
        self.shelved = 0