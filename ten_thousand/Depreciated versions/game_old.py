import sys
from ten_thousand.game_logic import GameLogic, Banker
import logging

basicConfig(level=logging.INFO, filename="Game.log", filemode='w')


class Game:

    def __init__(self):
        self.bank = Banker()
        self.kept_total = 0
        self.valid_response = False
        self.new_round = True
        self.roll_input = ""

    # def check_for_zilch(self, dice):
    #     zilch_print = (
    #     """
    #     ****************************************
    #     **        Zilch!!! Round over         **
    #     ****************************************
    #     """)
    #     if GameLogic.calculate_score(tuple(dice)) == 0:
    #         return print(zilch_print)

    def play_round(self, total, local_total, round_num, die, roller):
        """
        Function handles the users input, to play another round.

        :param total: The total running total
        :param round_num: The round the player is on
        :param die: The number of dice to roll, is reset to 6 each time function is called
        :param roller: The Gamelogic method that rolls the dice
        :param local_total: users local total - total not yet banked
        :return: No return for this function
        """
        # Could I use Args in my function declaration so i dont have to be so specific on my params?
        # running total when the user banks their score or keeps dice gets added incorrectly.
        # example. user rolls > keeps 15 for 150 unbanked points > rolls again, stores 551 for 350pts,
        # banked points is now 500pts, but shows as 350 in print after second roll,py
        # if banked correctly banks 500pts
        self.valid_response = False # setting valid response to false so user is prompted to keep some dice

        local_total = 0

        while self.new_round is True:

            print(f"Starting round {round_num}")

            print(f"Rolling {die} dice...")

            self.roll_input = ' '.join(map(str, (roller(die))))

            self.new_round = False


        while self.valid_response is False:

            print(f"*** {self.roll_input} ***")

            print("Enter dice to keep, or (q)uit:")

            response = input("> ")

            self.new_round = False

            self.valid_response = GameLogic.validate_keepers(self.roll_input, response)


        if response == "q":

            print(f"Thanks for playing. You earned {total} points")

            sys.exit()


        else:

            kept_die = [int(x) for x in str(response)]

            if len(kept_die) == 6:

                dice = 6

            else:

                dice = die - len(kept_die)

            local_total += GameLogic.calculate_score(tuple(kept_die))

            local_total += self.kept_total
            print(kept_die)
            print(dice)
            print(f"You have {local_total} unbanked points and {dice} dice remaining")

            print("(r)oll again, (b)ank your points or (q)uit:")

            response = input("> ")


            if response == "r":

                self.kept_total = local_total

                self.valid_response = False

                self.roll_input = ' '.join(map(str, (roller(dice))))

                self.play_round(total, self.kept_total, round_num, dice, roller)


            elif response == "b":

                self.bank.shelf(local_total)

                local_total = self.bank.bank()

                total += local_total

                self.new_round = True

                print(f"You banked {local_total} points in round {round_num}")

                print(f"Total score is {total} points")

                local_total = 0

                self.kept_total = 0

                die = 6

                round_num += 1

                self.play_round(total, local_total, round_num, die, roller)

            else:

                print(f"Thanks for playing. You earned {total} points")

                sys.exit()

    def play(self, roller=GameLogic.roll_dice):
        # Sets variable values at game start
        round_num = 1
        total = 0
        die = 6
        local_total = 0

        # Gets user input to start game or not.
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")

        if response == "n":
            print("OK. Maybe another time")
        if response == 'y':
            # Calls play_round function beginning gameplay
            self.play_round(total, local_total, round_num, die, roller)


if __name__ == "__main__":
    game = Game()
    game.play()


"""
play method > welcome to 10K and checks response
if Y pass start round() function which takes in round nums
start round 
tracks num dice and round total

checks if response is B
if b shelf round total,
ends the round passing the banked points into the round function
which goes again.

"""