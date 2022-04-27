from ten_thousand.game_logic import GameLogic, Banker


class Game:
    def play(self, roller=GameLogic.roll_dice):

        round_num = 0
        score = 0
        die = 6

        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")

        if response == "n":
            print("OK. Maybe another time")
        else:
            round_num += 1
            print(f"Starting round {round_num}")
            print(f"Rolling {die} dice...")
            roll_input = ' '.join(map(str, (roller(die)))) # roll_input = "4 2 6 4 6 5"
            print(f"*** {roll_input} ***") # *** 4 2 6 4 6 5 ***
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")

            if response == "q":
                print(f"Thanks for playing. You earned {score} points")
            else: # were getting a 5, send this 5 into our calculate score function as a tupple
                kept_die = [int(response)]
                dice = die - len(kept_die)
                score = GameLogic.calculate_score(tuple(kept_die))
                print(f"You have {score} unbanked points and {dice} dice remaining")
                print("(r)oll again, (b)ank your points or (q)uit:")
                response = input("> ")

                if response == "b":
                    score += Banker.bank(score)
                    print(f"You banked {score} points in round {round_num}")
                    round_num += 1
                    print(f"Total score is {score} points")


if __name__ == "__main__":
    game = Game()
    game.play()