import sys
import random

# from enum import Enum


def guess_number(name="playerone"):
    game_count = 0
    player_win = 0
    # winning_percentage = 50

    def play_guess_number():
        nonlocal name
        nonlocal player_win
        # nonlocal winning_percentage

        # class GN(Enum):
        #     1
        #     2
        #     3

        player_choice = input(
            f"\n {name} Guess which number I am thinking of ... 1, 2, or 3 "
        )
        if player_choice not in ["1", "2", "3"]:
            print(f"{name} Please Enter 1, 2, or 3")
            return play_guess_number

        player = int(player_choice)
        computerchoice = random.choice("123")
        computer = int(computerchoice)

        # print(f"{name}, you choce {str(GN(player)).replace('GN', ' ')}. ")
        print(f"\n{name}, you choce {player_choice}. ")
        # print(
        #     f"I was thinking about the number {str(GN(computer)).replace('GN', ' ')}. \n"
        # )
        print(f"I was thinking about the number {computerchoice}. \n")

        def decide_winner(player, computer):
            nonlocal player_win
            nonlocal name

            if player == computer:
                player_win += 1
                return f"{name}, 🎉 You win!"
            # elif player == 2 and computer == 2:
            #     player_win += 1
            #     return f"{name}, 🎉 You win!"
            # elif player == 3 and computer == 3:
            #     player_win += 1
            #     return f"{name}, 🎉 You win!"
            # elif player != computer:
            #     return
            else:
                return f"Sorry {name}. Better luck next time.  😎"

        game_result = decide_winner(player, computer)
        print(game_result)

        # nonlocal winning_percentage
        nonlocal game_count
        game_count += 1
        print(f"\nGame count:  {game_count}")
        print(f"\n{name}'s win:  {player_win}")
        print(f"\nYour winning Pecentage: {player_win/game_count: .2%}")

        print(f"\n Play Agian {name}?")

        while True:
            play_again = input("\n Y for yes or \nQ to quit \n ")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break
        if play_again.lower() == "y":
            return play_guess_number()
        else:
            print(f"\n🎉🧇🎉🧇")
            print("Thank you for Playing \n")
            if __name__ == "__main__":
                sys.exit("\n Good Bye {name}  👋")
            else:
                return

    return play_guess_number


if __name__ == "__main__":

    import argparse

    parses = argparse.ArgumentParser(description="Provide personalized gamne experince")

    parses.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game",
    )

    args = parses.parse_args()

    guess_my_number = guess_number(args.name)
    guess_my_number()
