# DEVELOPING GAME

import sys

# This module will allow to randome out put
import random

# This is to import Enum only not the entire module
from enum import Enum


def rps(name="playerone"):
    # globalScope
    game_count = 0
    player_win = 0
    python_win = 0

    # Passing Class this is to capitalise constant veriables
    def play_rps():
        nonlocal name
        nonlocal player_win
        nonlocal python_win

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

            # 1ST THING TO DEVELOP
            # This code is for players choice when playing the game.

        playerchoice = input(
            f"\n{name} please enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        player = int(playerchoice)
        # This code help for random selection by thecomputer
        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, you chose  {str(RPS(player)).replace('RPS.', '')}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '')}.\n")

        # This code shows the variouce options of win and
        # tie game for the player. (decesion tree)
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_win
            nonlocal python_win
            if player == 1 and computer == 3:
                player_win += 1
                return f"🎉{name}, you win!"
            elif player == 2 and computer == 1:
                player_win += 1
                return f"🎉{name}, you win!"
            elif player == 3 and computer == 2:
                player_win += 1
                return f"🎉{name}, you win!"
            elif player == computer:
                return "😲 Tie Game!"
            else:
                python_win += 1
                return f"🐍 Python wins!\nSorry, {name}..😢"

        Game_result = decide_winner(player, computer)
        print(Game_result)

        # using the scope lesson
        nonlocal game_count
        game_count += 1
        print(f"\n Game count:  {game_count}")
        print(f"\n {name}'s win:  {player_win}")
        print(f"\n python win:  {python_win}")

        print(f"\n play again, {name}?")

        while True:

            playagain = input(" \nY for Yes or \nQ to quit \n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🙌🥂")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye! {name} 👋")
            else:
                return

    return play_rps


if __name__ == "__main__":

    import argparse

    parses = argparse.ArgumentParser(
        description="Provide a personalize Game expirience!."
    )

    parses.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the Game",
    )

    arg = parses.parse_args()

    rock_paper_scissors = rps(arg.name)
    rock_paper_scissors()
