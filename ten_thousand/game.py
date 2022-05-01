import logging
import sys
from ten_thousand.game_logic import GameLogic, Banker

# logging.basicConfig(level=logging.INFO, filename="Game.log", filemode='w')


class Game:

    def __init__(self):
        self.bank = Banker()
        self.game_total = 0  # used in logging
        self.round_total = 0  # used in logging
        self.round_num = 1
        self.dice_num = 6
        self.roll = []
        self.roll_string = ""
        self.roller = ""
        self.user_kept = []

    # def log_vars(self, function):
    #     """ Logging function to track state of variables/attributes as game runs """
    #     logging.INFO(f"{function} function called")
    #     logging.INFO(f"self.game_total is: {self.game_total}")
    #     logging.INFO(f"self.round_total is: {self.round_total}")
    #     logging.INFO(f"self.roll is {self.roll}")
    #     logging.INFO(f"self.roll_string is {self.roll_string}")

    def play(self, roller=GameLogic.roll_dice):
        """
        Docstring:
        :param roller:
        :return:
        """
        # self.log_vars("play game")
        self.roller = roller
        self.welcome_to_game()
        self.print_start_round()
        self.handle_roll()
        self.get_user_kept()

    def increment_round_nun(self):
        """
        increments the round num attribute
        :return:
        """
        self.round_num += 1

    def welcome_to_game(self):
        """
        invites player to play game,
        exits application if user inputs n for no
        :return:
        """
        # self.log_vars("welcome to game")
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")
        if response == 'n':
            # begin a round
            print("OK. Maybe another time")
            sys.exit()
        elif response == 'y':
            pass
        elif response != 'n' or not 'y':
            print("sorry, that isnt a valid input")
            print("(y)es to play or (n)o to decline")
            response = input("> ")

    def thanks_for_playing(self):
        """
        Thanks player for playing, displays points earned in gameplay
        :return:
        """
        print(f"Thanks for playing. You earned {self.game_total}")
        sys.exit()
        # self.log_vars("thanks for playing")

    def print_start_round(self):
        """
        displays to the console on new round start
        :return:
        """
        # self.log_vars("print round")
        print(f"Starting round {self.round_num}")

    def end_current_round(self):
        """
        performs bank of points, shows end of round message with round and game total
        :return:
        """
        # self.log_vars("end current round")
        round_points = self.bank.bank()
        print(f"You banked {round_points} points in round {self.round_num}")
        print(f"Total score is {self.bank.balance} points")
        self.game_total += round_points

    def play_round(self):
        """

        :return:
        """
        # self.log_vars("Play round")
        self.print_start_round()

    def handle_zilch(self):
        """
        Checks users roll for zilch and handles results of zilch
        :return:
        """
        # self.log_vars("handle zilch")
        if GameLogic.calculate_score(self.roll) == 0:
            # roll is a zilch
            self.bank.clear_shelf() # user loses all unbanked points from round
            print("****************************************")
            print("**        Zilch!!! Round over         **")
            print("****************************************")

    def handle_roll(self):
        """
        rolls die, and displays new roll in formatted print, also sets self.roll to output of roller
        and saves attribute self.roll_string as formatted roll.
        :return:
        """
        # self.log_vars("handle roll")
        self.roll = self.roller(self.dice_num)
        self.roll_string = ' '.join(map(str, self.roll))
        print(f"Rolling {self.dice_num} dice...")
        print(f"*** {self.roll_string} ***")

    def continue_round(self):
        """

        :return:
        """
        print(f"you have {self.round_total} and {self.dice_num} remaining")
        print("(r)oll again, (b)ank your points or (q)uit")

    def get_user_kept(self):
        """

        :return:
        """
        # self.log_vars("get user kept")
        user_kept = self.validate_kept()
        self.round_total = GameLogic.calculate_score(user_kept)
        self.bank.shelf(self.round_total)
        self.dice_num = self.dice_num - len(user_kept)

    def validate_kept(self):
        """

        :return:
        """
        # self.log_vars("validate kept")
        print("Enter dice to keep, or (q)uit:")
        response = input("> ")
        if response == "q":
            self.thanks_for_playing()
        user_kept = []
        for char in response:
            if char.isnumeric():
                user_kept.append(int(char))

        if GameLogic.validate_keepers(self.roll, user_kept):
            return user_kept
        else:
            print("Cheater!!! Or possibly made a typo...")
            print(f"*** {self.roll_string} ***")

    def handle_bank(self):
        """"""
        print(f)

        self.bank.bank(self.round_total)
        self.round_total = 0


if __name__ == "__main__":
    game = Game()
    game.play()
