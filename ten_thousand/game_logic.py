
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
    def validate_keepers(roll, user_input): # if we take in roll_input it will be a clean string
        roll_stripped = roll.replace(' ','')
        roll_list = [int(char) for char in roll_stripped] # "5 2 3 5 4 2" > [ 5, 2, 3, 5, 4, 2 ]
        user_input_list = [int(char) for char in user_input if char.isdigit()]  # 555 > [ 5, 5, 5] [(5, 3)]
        for char in user_input_list:
            count_input = user_input_list.count(char)
            count_roll = roll_list.count(char)
            if count_input > count_roll:
                print("Cheater!!! Or possibly made a typo...")
                return False # if response invalid flip flag.
            else:
                return True

    @staticmethod
    def calculate_score(roll):
        """
        Calculates the score based on a given dice roll.
        """
        # Borrowed this code from Eden to test my functionality
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
        # End of borrowed code




        # my code below this line
        # score = 0
        # counts = Counter(roll)
        # fives_used = False
        # ones_used = False
        #
        # for num in range(1, 6 + 1):
        #     occurance_count = counts[num]
        #
        #     if len(counts) == 6:
        #         score += 1500
        #         return score
        #
        #     if len(counts) == 3:
        #         score += 1500
        #         return score
        #
        #     if len(counts) == 2:
        #         score += 1200
        #         return score
        #
        #     if occurance_count >= 3:
        #
        #         value_add = num * 100
        #         score = value_add
        #         bonus_occurances = occurance_count - 3
        #         score += bonus_occurances * value_add
        #
        #         if num == 1:
        #             ones_used = True
        #             score *= 10
        #
        #         if num == 5:
        #             fives_used = True
        #     # use this
        # if not ones_used:
        #     score += counts[1] * 100
        #
        # if not fives_used:
        #     score += counts[5] * 50
        # return score


class Banker(GameLogic):

    def __init__(self):
        self.balance = 0 # 200
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