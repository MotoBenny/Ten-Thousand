import sys
from ten_thousand.game_logic import GameLogic, Banker


class Game:

    def __init__(self):
        self.bank = Banker()

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
        valid_response = False
        round_num += 1

        print(f"Starting round {round_num}") # starting round one
        print(f"Rolling {die} dice...")
        roll_input = ' '.join(map(str, (roller(die))))

        while valid_response is False:
            print(f"*** {roll_input} ***")
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")
            valid_response = GameLogic.validate_keepers(roll_input, response)

        if response == "q":
            print(f"Thanks for playing. You earned {total} points")
            sys.exit()
        else:
            kept_die = [int(x) for x in str(response)]
            dice = die - len(kept_die)
            dice_to_keep = tuple(kept_die)
            local_total += GameLogic.calculate_score(dice_to_keep)
            print(f"You have {local_total} unbanked points and {dice} dice remaining")
            print("(r)oll again, (b)ank your points or (q)uit:")
            response = input("> ")

            if response == "r":
                self.play_round(local_total, local_total, round_num, dice, roller)
                # (self, total, local_total, round_num, die, roller)
            elif response == "b":
                self.bank.shelf(local_total)
                local_total = self.bank.bank()
                total += local_total
                print(f"You banked {local_total} points in round {round_num}")
                print(f"Total score is {total} points")
                local_total = 0
                die = 6
                self.play_round(total, local_total, round_num, die, roller)
            else:
                print("Thank you for playing Ten thousand > Powered by AWS")
                sys.exit()

    def play(self, roller=GameLogic.roll_dice, validate_keepers=GameLogic.validate_keepers):
        round_num = 0
        total = 0
        die = 6
        local_total = 0

        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")

        if response == "n":
            print("OK. Maybe another time")
        if response == 'y':
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