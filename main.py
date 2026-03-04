import random
import time


class CrapsGame:
    WIN_NUMBERS = (7, 11)
    CRAPS_NUMBERS = (2, 3, 12)

    def __init__(self):
        self.point = None

    def roll_dice(self):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        total = dice_1 + dice_2

        time.sleep(1)
        print(f"\nRolling the dice...")
        time.sleep(1)
        print(f"{dice_1} + {dice_2} = {total}")

        return total

    def start_game(self):
        while True:
            start = input('If you are ready, type "start": ').lower()

            if start == "start":
                break
            print("Invalid input. Please type 'start' to begin.")

        first_roll = self.roll_dice()

        if first_roll in self.WIN_NUMBERS:
            return "You Won instantly!"

        if first_roll in self.CRAPS_NUMBERS:
            return "Craps! Casino Wins!"

        self.point = first_roll
        print(f"\nYour point is now {self.point}")
        return self.continue_game()

    def continue_game(self):
        while True:
            roll = self.roll_dice()

            if roll == self.point:
                return "You hit your point! You won!"

            if roll == 7:
                return "You rolled a 7! Casino Wins!"


def main():
    print("-------- Welcome to CRAPS --------")

    while True:
        game = CrapsGame()
        result = game.start_game()
        print(f"\n{result}")

        while True:
            again = input("\nDo you want to play again? (y/n): ").lower()

            if again in ("y", "n"):
                break
            print("Please enter 'y' or 'n'.")

        if again == "n":
            print("\nThanks for playing!")
            break


if __name__ == "__main__":
    main()