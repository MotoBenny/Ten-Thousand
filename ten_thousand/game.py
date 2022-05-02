import sys
from ten_thousand.game_logic import GameLogic, Banker


class Game:

    def __init__(self):
        self.bank = Banker()
        self.game_total = 0  # used in logging
        self.round_total = 0  # used in logging
        self.round_num = 1
        self.dice_num = 6
        self.roll = []  # [1,5,6,3,2,1]
        self.in_round = False
        self.in_game = True
        self.round_lost = False
        self.user_kept = []
        self.roller = 0
        self.zilch = False
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
        self.in_round = False
        self.roller = roller
        self.game_lost = False
        while self.in_game:
            self.welcome_to_game()
            while True:
                self.play_turn()
                self.increment_round_nun()
        print("game over")

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
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")
        if response == 'n':
            print("OK. Maybe another time")
            sys.exit()
        elif response == 'y':
            self.in_round = True
        elif response != 'n' or not 'y':
            print("sorry, that isnt a valid input")
            print("(y)es to play or (n)o to decline")
            response = input("> ")

    def thanks_for_playing(self):
        """
        Thanks player for playing, displays points earned in gameplay
        :return:
        """
        print(f"Thanks for playing. You earned {self.game_total} points")
        sys.exit()

    def print_start_round(self):
        """
        displays to the console on new round start
        :return:
        """
        print(f"Starting round {self.round_num}")

    def handle_zilch(self):
        """
        Checks users roll for zilch and handles results of zilch
        :return:
        """
        if GameLogic.calculate_score(self.roll) == 0:
            self.bank.clear_shelf()
            print("****************************************")
            print("**        Zilch!!! Round over         **")
            print("****************************************")

            self.round_total = 0
            self.bank.clear_shelf()
            self.handle_bank()
            self.zilch = True

    def handle_roll(self):
        """
        rolls die, and displays new roll in formatted print, also sets self.roll to output of roller
        and saves attribute self.roll_string as formatted roll.
        :return:
        """
        self.roll = self.roller(self.dice_num)
        self.roll_string = ' '.join(map(str, self.roll))
        print(f"Rolling {self.dice_num} dice...")
        print(f"*** {self.roll_string} ***")

    def continue_round(self):
        """

        :return:
        """
        print(f"You have {self.round_total} unbanked points and {self.dice_num} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")

    def get_dice_to_keep(self):
        print("Enter dice to keep, or (q)uit:")
        response = input("> ")
        if response == 'q':
            self.thanks_for_playing()
        user_kept = []
        for char in response:
            if char.isnumeric():
                user_kept.append(int(char))
        self.user_kept = user_kept
        return self.validate_kept()

    def validate_kept(self):
        if GameLogic.validate_keepers(self.roll, self.user_kept):
            self.round_total += GameLogic.calculate_score(self.user_kept)
            self.dice_num = self.dice_num - len(self.user_kept)
            return self.user_kept
        else:
            print("Cheater!!! Or possibly made a typo...")
            print(f"*** {self.roll_string} ***")
            self.get_dice_to_keep()

    def handle_bank(self):
        """"""
        print(f"You banked {self.round_total} points in round {self.round_num}")
        self.bank.shelf(self.round_total)
        self.bank.bank()
        self.game_total += self.round_total
        print(f"Total score is {self.bank.balance} points")
        self.round_total = 0

    def play_turn(self):

        self.dice_num = 6
        self.print_start_round()
        self.round_lost = False
        self.zilch = False

        while self.round_lost is False:
            while True:
                self.handle_roll()
                self.handle_zilch()
                if self.zilch is True:
                    self.round_lost = True
                    break

                self.get_dice_to_keep()

                self.continue_round()
                if self.dice_num == 0:
                    self.dice_num = 6

                response = input("> ")
                if response == 'q':
                    self.thanks_for_playing()
                elif response == 'b':
                    self.handle_bank()
                    return

if __name__ == "__main__":
    game = Game()
    game.play()
