import sys
from rps import rps
from guess_number import guess_number


def play_game(name="playerone"):
    Welcom_back = False

    while True:
        if Welcom_back == True:
            print(f"\n{name}, Wlecome back to Arcade Manu.")

        playerchoice = input(
            '\nPlease choce a game: \n1 = Rock Paper Scissors \n2 = Guess My Number \n\n or press "x" to exit the Arcade\n\n'
        )

        if playerchoice not in ["1", "2", "x"]:
            print(f"\n{name}, Please enter 1, 2, or x.")
            return play_game(name)

        Welcom_back = True

        if playerchoice == "1":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif playerchoice == "2":
            guess_my_number = guess_number(name)
            guess_my_number()
        else:
            print("\nSee you next time\n")
            sys.exit(f"Bye {name}!👋")


if __name__ == "__main__":
    import argparse

    parses = argparse.ArgumentParser(
        description="Provide a personalized game experience"
    )

    parses.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game",
    )

    args = parses.parse_args()
    print(f"\n{args.name}, Welcome to the Arcade! 😎")

    play_game(args.name)
